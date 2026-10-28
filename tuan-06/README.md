# Tuần 6 — Nhóm App A4

## Nội dung đã chuẩn bị

- [Demo đăng nhập](NguyenQuangHuy/test_login.py): đăng nhập hợp lệ và assertion PRODUCTS.
- [Demo riêng A4](NguyenQuangHuy/test_session_menu.py): tạo session, in session_id/capabilities, đăng nhập nếu cần, mở Menu, Android Back và đóng session.
- [Hướng dẫn đăng nhập](NguyenQuangHuy/DEMO_MANUAL.md).
- [Hướng dẫn demo A4 và giải thích code](NguyenQuangHuy/DEMO_A4_SESSION_MENU.md).
- Hai script Python đã kiểm tra cú pháp. Demo A4 đã có kết quả chạy PASS trước đó, gồm Windows PowerShell độc lập; không chạy lại demo trong lượt chuẩn bị nộp này.

## Slide và ghi chú

- Bản thiết kế: https://www.canva.com/design/DAHYvDhVMf4/ffGqpu9jUhV1YwV7kKC_Gg/edit
- **Chưa có `slides.pdf` trong lần đẩy này:** phiên Canva dùng để kiểm tra yêu cầu đăng nhập khi tải PDF. Link Canva không thay thế file PDF bắt buộc.
- Bản Canva hiện có 14 trang theo lựa chọn giữ đầy đủ nội dung của nhóm; yêu cầu Timeline là tối đa 8 slide. Cần xử lý giới hạn này hoặc xác nhận với giảng viên trước khi coi bài slide đạt yêu cầu.
- `notes.md` sẽ bổ sung sau khi nhận góp ý thực tế, theo quyết định của trưởng nhóm; chưa tạo ghi chú hoặc góp ý giả.

## Chạy lại

Các lệnh môi trường trên máy demo nằm trong hai hướng dẫn phía trên. Sau khi Emulator và Appium sẵn sàng, từ thư mục gốc repository:

```powershell
& '.\.venv-app\Scripts\python.exe' '.\tuan-06\NguyenQuangHuy\test_session_menu.py'
$LASTEXITCODE
```

Để trình diễn cả nhập tài khoản, chọn Menu → LOGOUT trên app trước khi chạy. Không đưa môi trường ảo, cache, APK hoặc SDK vào Git.
