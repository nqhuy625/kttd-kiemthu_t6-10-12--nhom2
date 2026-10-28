# Demo đăng nhập Swag Labs tuần 6

Dùng nguyên Appium 3.8.0 trong LocalCache và UiAutomator2 8.7.0 trong C:\Users\admin\.appium. Nghiệm thu ngày 23/10/2026: server và Python được khởi chạy từ Windows PowerShell 5.1 độc lập qua Task Scheduler, hai lượt liên tiếp assertion PRODUCTS PASS, exit code 0 và session đóng thành công. Không cài môi trường mới.

## Chuẩn bị

Mở VS Code → File → Open Folder → C:\Users\admin\kttd-kiemthu_t6-10-12--nhom2. Mở tuan-06\NguyenQuangHuy\test_login.py để giải thích code. Mở ba cửa sổ qua Windows+R, nhập powershell.exe -NoProfile. Các biến môi trường dưới đây chỉ áp dụng trong cửa sổ hiện tại.

## PowerShell 1 — Android Emulator

Nếu A4_API33 đã chạy, giữ cửa sổ điện thoại, không mở thêm máy ảo. Nếu chưa chạy:

~~~powershell
$sdk = 'C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Local\Android\Sdk'
$env:ANDROID_HOME = $sdk
$env:ANDROID_SDK_ROOT = $sdk
$env:ANDROID_AVD_HOME = 'C:\Users\admin\.android\avd'
& "$sdk\emulator\emulator.exe" -avd A4_API33 -sysdir "$sdk\system-images\android-33\google_apis\x86_64" -no-snapshot -gpu auto
~~~

-avd chọn AVD cũ; -sysdir chỉ image API 33; -no-snapshot không dùng snapshot; -gpu auto chọn chế độ đồ họa tự động.

Trong PowerShell 3, kiểm tra:

~~~powershell
$sdk = 'C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Local\Android\Sdk'
& "$sdk\platform-tools\adb.exe" devices
& "$sdk\platform-tools\adb.exe" -s emulator-5554 shell getprop sys.boot_completed
~~~

Chỉ tiếp tục khi có emulator-5554 device và 1. Nếu trống/offline, đợi Android boot rồi kiểm tra lại. Nếu thiếu image, dùng Test-Path "$sdk\system-images\android-33\google_apis\x86_64\system.img"; không trỏ về đường dẫn SDK AppData ảo cũ.

## PowerShell 2 — Appium Server gốc

Trước khi khởi động, kiểm tra trong PowerShell 3:

~~~powershell
Invoke-RestMethod 'http://127.0.0.1:4723/status'
~~~

Nếu đã có ready: True, không mở server thứ hai. Muốn tự mở server của mình, dừng server cũ đúng cách trước. Khi server chưa chạy, nhập trong PowerShell 2:

~~~powershell
$env:ANDROID_HOME = 'C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Local\Android\Sdk'
$env:ANDROID_SDK_ROOT = $env:ANDROID_HOME
$env:JAVA_HOME = 'C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot'
$env:APPIUM_HOME = 'C:\Users\admin\.appium'
$env:Path = "C:\Program Files\nodejs;$env:ANDROID_HOME\platform-tools;$env:Path"
$appium = 'C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Roaming\npm\node_modules\appium\index.js'
& 'C:\Program Files\nodejs\node.exe' $appium --address 127.0.0.1 --port 4723
~~~

Giữ cửa sổ này mở. Appium phải tải uiautomator2@8.7.0. Trong PowerShell 3, kiểm tra /status có ready: True. Trạng thái này chỉ chứng minh server đang nghe; tạo session Android và chạy test mới chứng minh driver hoạt động.

Có thể liệt kê driver trước khi mở server, sau khi đặt các biến trên:

~~~powershell
& 'C:\Program Files\nodejs\node.exe' $appium driver list --installed
~~~

EADDRINUSE nghĩa là cổng 4723 đang được sử dụng; không mở server thứ hai. Nếu lỗi Cannot find package appium, kiểm tra junction ở mục dependency, không cài lại toàn bộ hoặc dùng --force.

## PowerShell 3 — kiểm thử đăng nhập

~~~powershell
cd 'C:\Users\admin\kttd-kiemthu_t6-10-12--nhom2'
& '.\.venv-app\Scripts\python.exe' '.\tuan-06\NguyenQuangHuy\test_login.py'
$LASTEXITCODE
~~~

Swag Labs phải tự nhập standard_user / secret_sauce, nhấn LOGIN, chuyển sang PRODUCTS. Kết quả:

~~~text
PASS: Đăng nhập thành công và PRODUCTS đã xuất hiện.
Đã đóng phiên Appium.
0
~~~

Để chạy lại, giữ emulator và server, chỉ nhập lại lệnh Python. driver.quit() trong finally đóng session, không tắt Appium Server/emulator.

Nếu HTTP 500 khi tạo session, đọc log PowerShell 2. Nếu timeout ở PRODUCTS, đó là lỗi kiểm tra thật; không bỏ assertion.

## Dependency đã sửa và cách kiểm tra

Driver nhập appium/driver.js như peer dependency. Junction có sẵn tại C:\Users\admin\.appium\node_modules\appium-uiautomator2-driver\node_modules\appium trước đây trỏ tới đường dẫn npm ảo C:\Users\admin\AppData\Roaming\npm\node_modules\appium. Nó đã được đổi sang đích vật lý:

C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Roaming\npm\node_modules\appium

Junction cũ được giữ dưới tên appium.before-localcache-fix trong cùng thư mục. Không cài/nâng cấp package. Kiểm tra:

~~~powershell
Get-Item -LiteralPath 'C:\Users\admin\.appium\node_modules\appium-uiautomator2-driver\node_modules\appium' | Format-List FullName,LinkType,Target
~~~

## Giải thích khi trình bày

- webdriver.Remote tạo session từ Python qua HTTP tới Appium 4723.
- UiAutomator2 điều khiển giao diện Android; ADB kết nối và quản lý thiết bị.
- ACCESSIBILITY_ID tìm phần tử qua content description.
- send_keys nhập dữ liệu; click nhấn LOGIN.
- WebDriverWait chờ điều kiện và tìm lại phần tử nếu ứng dụng vẽ lại giao diện.
- assert products_visible xác nhận PRODUCTS thực sự hiển thị. Nếu điều kiện chờ không đạt, timeout gây FAIL.
- driver.quit trong finally kết thúc session sau cả PASS và lỗi.

## Dừng đúng cách

Chờ Python kết thúc. Với server do mình mở trong PowerShell 2, nhấn Ctrl+C và chờ dừng. Đóng emulator bằng nút X sau cùng. Không tắt toàn bộ node.exe; không xóa AVD/SDK.

## Thay đổi trong lần sửa 23/10/2026

- Đổi đích junction dependency có sẵn sang Appium vật lý trong LocalCache; giữ junction cũ làm backup.
- Cập nhật run-demo.ps1 dùng SDK/Appium LocalCache, APPIUM_HOME cũ và -sysdir.
- Viết lại tài liệu này. test_login.py, assertion, SDK, APK và Python được giữ nguyên.
- Log kiểm chứng nằm trong build/appium-demo/ (được Git bỏ qua). Các tác vụ kiểm tra tạm thời được gỡ sau nghiệm thu.
