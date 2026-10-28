# Demo đăng nhập Swag Labs

Hướng dẫn mở VS Code và chạy thủ công theo ba terminal: [DEMO_MANUAL.md](DEMO_MANUAL.md).

Phần riêng A4 tuần 6 — session, capabilities, Menu và Android Back: [DEMO_A4_SESSION_MENU.md](DEMO_A4_SESSION_MENU.md). Chạy bằng `test_session_menu.py`; `run-demo.ps1` vẫn chạy bài đăng nhập cũ.

## Dữ liệu kiểm thử

- Username: standard_user
- Password: secret_sauce
- Kết quả mong đợi: màn hình PRODUCTS xuất hiện

## Chạy nhanh trên máy demo

Mở PowerShell trong thư mục gốc repo và chạy:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\tuan-06\NguyenQuangHuy\run-demo.ps1
```

Script sẽ kiểm tra các file cần thiết, mở `A4_API33` nếu chưa chạy, chờ Android khởi động, mở Appium Server nếu cần, rồi chạy bài test. Giữ cửa sổ emulator mở để quan sát các thao tác. Appium ghi log vào `build/appium-demo/` khi script khởi động server.

## Chạy từng bước

1. Khởi động emulator A4_API33.
2. Kiểm tra emulator bằng ADB trong SDK LocalCache, theo đường dẫn ở `DEMO_MANUAL.md`.
3. Kiểm tra Appium bằng `Invoke-RestMethod http://127.0.0.1:4723/status`. Nếu chưa chạy, dùng lệnh Node.js với Appium LocalCache và `APPIUM_HOME` cũ trong `DEMO_MANUAL.md`.
4. Chạy test bằng môi trường Python của dự án.

## Chạy test

```powershell
.\.venv-app\Scripts\python.exe `
  .\tuan-06\NguyenQuangHuy\test_login.py
```

## Kết quả mong đợi

Terminal hiển thị:

```text
PASS: Đăng nhập thành công và PRODUCTS đã xuất hiện.
Đã đóng phiên Appium.
```
