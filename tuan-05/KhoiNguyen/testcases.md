TEST CASE KIỂM THỬ CHỨC NĂNG ĐĂNG NHẬP

TC01: Đăng nhập thành công

Mục đích: Kiểm tra đăng nhập khi nhập đúng tài khoản và mật khẩu.

Các bước thực hiện:
1. Mở chức năng đăng nhập.
2. Nhập tên đăng nhập: admin.
3. Nhập mật khẩu: 123456.
4. Nhấn nút Đăng nhập.

Dữ liệu kiểm thử:
- Tên đăng nhập: admin
- Mật khẩu: 123456

Kết quả mong đợi:
- Hệ thống thông báo "Đăng nhập thành công".
- Người dùng được phép truy cập hệ thống.

TC02: Đăng nhập sai mật khẩu

Mục đích: Kiểm tra hệ thống khi người dùng nhập sai mật khẩu.

Các bước thực hiện:
1. Mở chức năng đăng nhập.
2. Nhập tên đăng nhập: admin.
3. Nhập mật khẩu sai: 123.
4. Nhấn nút Đăng nhập.

Dữ liệu kiểm thử:
- Tên đăng nhập: admin
- Mật khẩu: 123

Kết quả mong đợi:
- Hệ thống thông báo "Sai tài khoản hoặc mật khẩu".
- Người dùng không thể đăng nhập vào hệ thống.

TC03: Đăng nhập khi bỏ trống thông tin

Mục đích:Kiểm tra hệ thống khi người dùng không nhập tài khoản và mật khẩu.

Các bước thực hiện:
1. Mở chức năng đăng nhập.
2. Để trống ô tên đăng nhập.
3. Để trống ô mật khẩu.
4. Nhấn nút Đăng nhập.

Dữ liệu kiểm thử:
- Tên đăng nhập: "" (trống)
- Mật khẩu: "" (trống)

Kết quả mong đợi:
- Hệ thống thông báo "Vui lòng nhập đầy đủ thông tin".
- Người dùng không thể đăng nhập vào hệ thống.