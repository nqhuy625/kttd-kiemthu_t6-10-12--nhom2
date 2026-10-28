$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$localCache = 'C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache'
$sdkRoot = Join-Path $localCache 'Local\Android\Sdk'
$adbExe = Join-Path $sdkRoot 'platform-tools\adb.exe'
$emulatorExe = Join-Path $sdkRoot 'emulator\emulator.exe'
$nodeExe = 'C:\Program Files\nodejs\node.exe'
$npmPrefix = Join-Path $localCache 'Roaming\npm'
$appiumEntry = Join-Path $npmPrefix 'node_modules\appium\index.js'
$pythonExe = Join-Path $repoRoot '.venv-app\Scripts\python.exe'
$testFile = Join-Path $PSScriptRoot 'test_login.py'
$apkFile = 'C:\MobileTesting\apps\swaglabs-2.7.1.apk'
$logDir = Join-Path $repoRoot 'build\appium-demo'

foreach ($file in @($adbExe, $emulatorExe, $nodeExe, $pythonExe, $testFile, $apkFile)) {
    if (-not (Test-Path -LiteralPath $file -PathType Leaf)) {
        throw "Missing required file: $file"
    }
}

$env:ANDROID_HOME = $sdkRoot
$env:ANDROID_SDK_ROOT = $sdkRoot
$env:ANDROID_AVD_HOME = 'C:\Users\admin\.android\avd'
$env:APPIUM_HOME = 'C:\Users\admin\.appium'
$env:JAVA_HOME = 'C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot'
$env:Path = "$(Join-Path $sdkRoot 'platform-tools');C:\Program Files\nodejs;$env:Path"

Write-Host 'Checking Android emulator...'
& $adbExe start-server | Out-Null
$deviceList = (& $adbExe devices) -join "`n"
if ($deviceList -notmatch '(?m)^emulator-5554\s+device\s*$') {
    $avdList = (& $emulatorExe -list-avds) -join "`n"
    if ($avdList -notmatch '(?m)^A4_API33\s*$') {
        throw 'AVD A4_API33 is not available.'
    }
    Write-Host 'Starting A4_API33. Keep its window open.'
    Start-Process -FilePath $emulatorExe -ArgumentList @('-avd', 'A4_API33', '-sysdir', (Join-Path $sdkRoot 'system-images\android-33\google_apis\x86_64'), '-no-snapshot', '-gpu', 'auto')
}

$booted = $false
for ($attempt = 0; $attempt -lt 90; $attempt++) {
    $deviceList = (& $adbExe devices) -join "`n"
    if ($deviceList -match '(?m)^emulator-5554\s+device\s*$') {
        $bootValue = (& $adbExe -s emulator-5554 shell getprop sys.boot_completed 2>$null | Out-String).Trim()
        if ($bootValue -eq '1') {
            $booted = $true
            break
        }
    }
    Start-Sleep -Seconds 2
}
if (-not $booted) {
    throw 'Emulator did not boot within 3 minutes. Check its window and run adb devices.'
}
Write-Host 'Android ready: emulator-5554'

function Test-AppiumReady {
    try {
        $status = Invoke-RestMethod -Uri 'http://127.0.0.1:4723/status' -TimeoutSec 3
        return [bool]$status.value.ready
    } catch {
        return $false
    }
}

if (-not (Test-AppiumReady)) {
    if (-not (Test-Path -LiteralPath $appiumEntry -PathType Leaf)) {
        throw "Original Appium Server was not found at $appiumEntry. See DEMO_MANUAL.md."
    }
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    Write-Host 'Starting Appium Server on 127.0.0.1:4723...'
    Start-Process -FilePath $nodeExe -ArgumentList @($appiumEntry, '--address', '127.0.0.1', '--port', '4723') -WindowStyle Hidden -RedirectStandardOutput (Join-Path $logDir 'appium.log') -RedirectStandardError (Join-Path $logDir 'appium-error.log')
    for ($attempt = 0; $attempt -lt 15; $attempt++) {
        if (Test-AppiumReady) { break }
        Start-Sleep -Seconds 2
    }
}
if (-not (Test-AppiumReady)) {
    throw "Appium did not become ready. Check logs in $logDir"
}
Write-Host 'Appium ready.'

Write-Host 'Running login test...'
Push-Location $repoRoot
try {
    & $pythonExe $testFile
    if ($LASTEXITCODE -ne 0) {
        throw "Login test failed with exit code $LASTEXITCODE"
    }
} finally {
    Pop-Location
}
