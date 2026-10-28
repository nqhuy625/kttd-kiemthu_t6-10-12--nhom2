# Tuần 6 — Nhóm App A4

## Nội dung đã chuẩn bị

- [Demo đăng nhập](NguyenQuangHuy/test_login.py): đăng nhập hợp lệ và assertion PRODUCTS.
- [Demo riêng A4](NguyenQuangHuy/test_session_menu.py): tạo session, in session_id/capabilities, đăng nhập nếu cần, mở Menu, Android Back và đóng session.
- [Hướng dẫn đăng nhập](NguyenQuangHuy/DEMO_MANUAL.md).
- [Hướng dẫn demo A4 và giải thích code](NguyenQuangHuy/DEMO_A4_SESSION_MENU.md).
- Hai script Python đã kiểm tra cú pháp. Demo A4 đã có kết quả chạy PASS trước đó, gồm Windows PowerShell độc lập; không chạy lại demo trong lượt chuẩn bị nộp này.

## Slide và ghi chú

- Bản thiết kế: https://www.canva.com/design/DAHYvDhVMf4/ffGqpu9jUhV1YwV7kKC_Gg/edit
- [slides.pdf](slides.pdf): bản PDF 14 trang xuất từ Canva, đã bổ sung ngày 28/10/2026; giữ nguyên nội dung, thứ tự và chất lượng file tải về.
- Nhóm quyết định giữ đủ 14 trang. Timeline ghi tối đa 8 slide; bản PDF này giữ 14 trang theo yêu cầu của trưởng nhóm, chưa phải xác nhận giảng viên đã chấp thuận vượt giới hạn.
- `notes.md` sẽ bổ sung sau khi nhận góp ý thực tế, theo quyết định của trưởng nhóm; chưa tạo ghi chú hoặc góp ý giả.

## Chạy lại

Các lệnh môi trường trên máy demo nằm trong hai hướng dẫn phía trên. Sau khi Emulator và Appium sẵn sàng, từ thư mục gốc repository:

```powershell
& '.\.venv-app\Scripts\python.exe' '.\tuan-06\NguyenQuangHuy\test_session_menu.py'
$LASTEXITCODE
```

Để trình diễn cả nhập tài khoản, chọn Menu → LOGOUT trên app trước khi chạy. Không đưa môi trường ảo, cache, APK hoặc SDK vào Git.
