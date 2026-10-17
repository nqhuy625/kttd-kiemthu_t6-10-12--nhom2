TEST CASES - LOGIN 

TC01 - ĐĂNG NHẬP THÀNH CÔNG

Mục tiêu: Kiểm tra người dùng có thể đăng nhập bằng thông tin hợp lệ.

\-Steps:

&#x20; 1. Mở trang https://the-internet.herokuapp.com/login.

&#x20; 2. Nhập username `tomsmith`.

&#x20; 3. Nhập password `SuperSecretPassword!`.

&#x20; 4. Nhấn nút Login.

\-Test data:

&#x20; - Username: `tomsmith`

&#x20; - Password: `SuperSecretPassword!`

\-Expected result: Trang chuyển đến trang bảo vệ sau đăng nhập và hiển thị thông báo đăng nhập thành công.

TC02 - ĐĂNG NHẬP VỚI MẬT KHẨU SAI

\-Mục tiêu:Kiểm tra hệ thống xử lý khi người dùng nhập sai mật khẩu.

\-Steps:

&#x20; 1. Mở trang https://the-internet.herokuapp.com/login.

&#x20; 2. Nhập username `tomsmith`.

&#x20; 3. Nhập password `WrongPassword123`.

&#x20; 4. Nhấn nút Login.

\-Test data:

&#x20; - Username: `tomsmith`

&#x20; - Password: `WrongPassword123`

\-Expected result:Người dùng không đăng nhập thành công và trang hiển thị thông báo lỗi đăng nhập.



TC03 - ĐĂNG NHẬP KHI BỎ TRỐNG THÔNG TIN

\-Mục tiêu:Kiểm tra hệ thống xử lý khi người dùng không nhập username và password.

\-Steps:

&#x20; 1. Mở trang https://the-internet.herokuapp.com/login.

&#x20; 2. Để trống ô username.

&#x20; 3. Để trống ô password.

&#x20; 4. Nhấn nút Login.

\- Test data:

&#x20; - Username: để trống

&#x20; - Password: để trống

\- Expected result: Người dùng không đăng nhập thành công và trang hiển thị thông báo phù hợp với dữ liệu thiếu.



