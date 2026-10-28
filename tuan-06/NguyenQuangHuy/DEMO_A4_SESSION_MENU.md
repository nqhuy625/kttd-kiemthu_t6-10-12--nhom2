# Demo riêng A4 tuần 6 — Appium session và Menu

## 1. Nội dung cần thể hiện

Python → Appium Server → UiAutomator2 → Swag Labs trên Android Emulator.

Demo tạo session bằng `webdriver.Remote` và `UiAutomator2Options`; in `session_id`, `capabilities`; đăng nhập nếu cần; xác nhận PRODUCTS; mở Menu bằng Accessibility ID; gọi `driver.back()`; xác nhận Menu đóng, PRODUCTS còn hiển thị, vẫn cùng session; cuối cùng `driver.quit()`.

Đây là phần riêng A4 trong sheet phân công, bổ sung cho slide và bài đăng nhập chung đã làm. Không triển khai Toggle tuần 7, giỏ hàng hay các chức năng khác. `test_login.py` và `run-demo.ps1` cũ vẫn dùng cho demo đăng nhập; demo mới chạy bằng `test_session_menu.py`.

## 2. Trước khi chạy

1. Mở VS Code → File → Open Folder → `C:\Users\admin\kttd-kiemthu_t6-10-12--nhom2`.
2. Chọn Terminal → New Terminal; chọn PowerShell. Bấm dấu `+` để có ba terminal.
3. Đóng Appium Inspector session nếu đang dùng. Không chạy hai bài Python đồng thời.
4. Nếu Emulator/Appium đã chạy thì dùng lại, không khởi động thêm bản thứ hai. Đường dẫn bên dưới là đường dẫn vật lý LocalCache đã dùng trên máy này, không thay bằng AppData logic.
5. APK phải tồn tại ở `C:\MobileTesting\apps\swaglabs-2.7.1.apk`.

## 3. Terminal 1 — Android Emulator

```powershell
$sdk = 'C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Local\Android\Sdk'
$env:ANDROID_HOME = $sdk
$env:ANDROID_SDK_ROOT = $sdk
$env:ANDROID_AVD_HOME = 'C:\Users\admin\.android\avd'
& "$sdk\emulator\emulator.exe" -avd A4_API33 -sysdir "$sdk\system-images\android-33\google_apis\x86_64" -no-snapshot -gpu auto
```

Chờ điện thoại vào màn hình Android. Terminal có thể tiếp tục hiện log vì Emulator đang chạy, đó không phải lỗi. Nếu điện thoại đã mở, bỏ qua lệnh khởi động.

## 4. Terminal 2 — Appium Server

Kiểm tra trước: `Invoke-RestMethod http://127.0.0.1:4723/status`. Nếu `value.ready=True`, dùng server đang chạy. Nếu kết nối bị từ chối thì khởi động:

```powershell
$env:ANDROID_HOME = 'C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Local\Android\Sdk'
$env:ANDROID_SDK_ROOT = $env:ANDROID_HOME
$env:JAVA_HOME = 'C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot'
$env:APPIUM_HOME = 'C:\Users\admin\.appium'
$env:Path = "C:\Program Files\nodejs;$env:ANDROID_HOME\platform-tools;$env:Path"
$entry = 'C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Roaming\npm\node_modules\appium\index.js'
& 'C:\Program Files\nodejs\node.exe' $entry --address 127.0.0.1 --port 4723
```

Đợi log server lắng nghe cổng 4723 và UiAutomator2 tải được. Giữ terminal mở. Không cần chạy lệnh `npm` hay cài lại Appium.

## 5. Terminal 3 — Kiểm tra và chạy demo

```powershell
Set-Location 'C:\Users\admin\kttd-kiemthu_t6-10-12--nhom2'
$sdk = 'C:\Users\admin\AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Local\Android\Sdk'
& "$sdk\platform-tools\adb.exe" devices
& "$sdk\platform-tools\adb.exe" -s emulator-5554 shell getprop sys.boot_completed
Invoke-RestMethod http://127.0.0.1:4723/status
```

Chỉ tiếp tục khi thiết bị là `emulator-5554 device`, boot trả `1`, Appium trả `ready=True`.

```powershell
& '.\.venv-app\Scripts\python.exe' '.\tuan-06\NguyenQuangHuy\test_session_menu.py'
$LASTEXITCODE
```

Không cần activate venv vì đã gọi thẳng Python của venv.

Kết quả cần thấy:

```text
SESSION ID: <ID thật của mỗi lần chạy>
CAPABILITIES (server trả về): ...
PASS: PRODUCTS hiển thị.
PASS: Menu hiển thị Close, ALL ITEMS, LOGOUT.
PASS: Android Back đóng Menu; PRODUCTS hiển thị; session giữ nguyên.
Đã đóng Appium session bằng driver.quit().
PASS: DEMO A4 TUẦN 6 HOÀN TẤT.
0
```

Script dùng `noReset=True` để giữ dữ liệu. Nếu đang Login, script nhập `standard_user` / `secret_sauce`. Nếu đã ở PRODUCTS, script ghi rõ dùng phiên đăng nhập có sẵn. Muốn trình diễn cả nhập tài khoản: mở Menu trên app → LOGOUT trước khi chạy. Không bấm Reset App State hoặc xóa dữ liệu.

Ảnh và XML từng bước cùng `result.json` lưu tại `build/week06-session-menu/` (chạy lại sẽ ghi đè bằng chứng mặc định). Muốn tách từng lần:

```powershell
& '.\.venv-app\Scripts\python.exe' '.\tuan-06\NguyenQuangHuy\test_session_menu.py' --evidence-dir '.\build\week06-session-menu\my-run'
```

## 6. Các bước đã khảo sát và ý nghĩa code

### Tạo session

```python
options = UiAutomator2Options().load_capabilities(requested)
driver = webdriver.Remote(command_executor=APPIUM_SERVER, options=options)
```

`requested` mô tả Android, driver UiAutomator2, thiết bị, APK và timeout. `options` đóng gói cấu hình theo API Appium Python hiện tại. `Remote` gửi yêu cầu tạo session tới Appium Server, dù server chạy ngay trên cùng máy.

### Session ID và capabilities

```python
session_id = driver.session_id
print(driver.capabilities)
```

ID xác định session để server định tuyến các lệnh tiếp theo. `driver.capabilities` là cấu hình server trả về, có thêm API level, phiên bản Android, model, kích thước màn hình… Không nhầm dictionary cấu hình gửi đi với kết quả server trả về. Mỗi lần tạo session mới thường có ID mới; trong một lần demo ID phải giữ nguyên.

### Đăng nhập và PRODUCTS

Locator xác minh: `test-Username`, `test-Password`, `test-LOGIN`, `test-PRODUCTS`. `clear()` xóa nội dung cũ; `send_keys()` nhập; `click()` nhấn; Explicit Wait chờ phần tử sẵn sàng. Bước PRODUCTS dùng assertion để xác nhận đã vào màn hình đúng.

### Menu

```python
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'test-Menu')
```

Accessibility ID tìm theo content-desc trên Android. Menu được xác nhận bằng ba phần tử riêng: `test-Close`, `test-ALL ITEMS`, `test-LOGOUT`. Chỉ thấy PRODUCTS là chưa đủ vì nội dung PRODUCTS vẫn có thể nằm phía sau Menu.

Menu thực tế còn có WEBVIEW, QR CODE SCANNER, GEO LOCATION, DRAWING, ABOUT, RESET APP STATE. Demo chỉ xác nhận Menu mở, không nhấn các chức năng ngoài phạm vi.

### Android Back

```python
driver.back()
```

Driver UiAutomator2 cài trên máy gửi Android keyevent 4. Trên APK 2.7.1 đã khảo sát, thao tác này đóng Menu. Demo không dùng nút Close thay cho Back ở bước kiểm tra. Sau Back, script chờ cả ba marker Menu biến mất, PRODUCTS hiện, package còn là Swag Labs và session ID giữ nguyên.

Nút Close chỉ có thể được dùng ở phần chuẩn bị nếu lần thao tác thủ công trước để Menu mở.

### Assertion và đóng session

`assert` sai làm Python báo lỗi và kết thúc khác 0. `driver.quit()` đặt trong `finally` để đóng session dù test đạt hay lỗi; không đồng nghĩa tắt Appium Server hoặc Emulator. File `result.json` ghi cả kết quả và việc đóng session.

## 7. Liên hệ các mục đọc trong sheet

| Mục | Điều cần giải thích |
|---|---|
| 1. Installation | Client Python, Appium Server, UiAutomator2, SDK/Emulator là các thành phần khác nhau; đang tái sử dụng môi trường đã có |
| 2.5 Remote WebDriver | Python gửi lệnh đến server qua HTTP và session |
| 7.6 Desired Capabilities | Là cấu hình yêu cầu cho session; demo truyền qua `UiAutomator2Options`, không sao chép API desired_capabilities cũ |
| 7.17 Chrome Options | Cấu hình dành cho Chrome; không áp dụng để chạy màn hình native Swag Labs |
| 8.1 ChromeDriver | Điều khiển Chrome; demo native Android dùng UiAutomator2 nên không cần cài ChromeDriver |
| 3.6 History and location | Là điều hướng back/forward trong web; ở demo Android, Back là phím hệ thống và hành vi phụ thuộc app, không phải lịch sử phát triển Selenium |

Nguồn tham khảo: https://appium.io/docs/en/latest/quickstart/test-py/ và https://selenium-python.readthedocs.io/navigating.html#navigation-history-and-location . Tài liệu Selenium có ví dụ web và API cũ; cần phân biệt với Appium native hiện tại.

## 8. Nếu gặp lỗi

- `Connection refused`: kiểm tra Terminal 2 và `/status`.
- Không có thiết bị/offline: chờ Android boot; kiểm tra ADB; chưa chạy Python.
- Timeout trước Login/PRODUCTS: kiểm tra app có đang ở màn hình chi tiết hoặc màn hình khác; đưa về Login/PRODUCTS và đóng Inspector session.
- Không tìm thấy Menu: xem app có hộp thoại che hay dùng APK khác không; đối chiếu XML bằng chứng, không sửa assertion thành luôn đúng.
- `Address already in use`: cổng 4723 đã có server; kiểm tra `/status`, không mở thêm bản thứ hai.
- Không import được `test_login`: giữ hai file Python cùng thư mục và chạy đúng lệnh trên.
- Chữ terminal hiển thị lỗi: mở PowerShell mới; script dùng cấu hình UTF-8 từ module đăng nhập cũ.

## 9. Lời trình bày gợi ý

“Em tạo Android session bằng Remote WebDriver và UiAutomator2Options. Server trả session ID và capabilities, cho biết thiết bị Android đang được điều khiển. Sau khi vào PRODUCTS, em tìm nút Menu bằng Accessibility ID. Bài kiểm thử xác nhận các mục Menu hiện ra, rồi gọi Android Back. Assertion kiểm tra Menu đã đóng, vẫn ở PRODUCTS và session không đổi. Cuối cùng quit đóng session.”

## 10. Dừng đúng cách

Chờ Python in kết quả và đóng session. Với Appium khởi động ở Terminal 2, bấm Ctrl+C tại terminal đó. Đóng cửa sổ Emulator khi không dùng nữa. Không kết thúc toàn bộ tiến trình Node hoặc xóa AVD.

## 11. Kết quả nghiệm thu ngày 27/10/2026

| Lần | Cách chạy | Session ID | Kết quả |
|---|---|---|---|
| 1 | Python trong môi trường kiểm tra Codex, app đã đăng nhập | `43ea0a75-bdc6-4bdb-945f-11c56cafb841` | PASS, exit 0, session đóng |
| 2 | Windows PowerShell 5.1 độc lập, sau Logout để kiểm tra nhập tài khoản | `9b333803-6a7d-467d-88db-f0b01e5e3f0f` | PASS, exit 0, session đóng |

Lần 2 được khởi chạy qua Task Scheduler dưới tài khoản Windows hiện tại để tránh phụ thuộc ngữ cảnh AppData của Codex. Tác vụ tạm đã được gỡ sau khi LastTaskResult=0. Đây là bằng chứng chạy độc lập, không yêu cầu người demo phải dùng Task Scheduler.

Bằng chứng: `build/week06-session-menu/run1/result.json`, `build/week06-session-menu/run2-independent/result.json`; mỗi thư mục có ảnh và XML của ba bước. Transcript PowerShell: `build/week07-inspection/week06-independent.log`. Thư mục build được Git bỏ qua. Không commit/push trong lượt thực hiện này.
