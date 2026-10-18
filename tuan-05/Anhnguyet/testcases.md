\# Test Cases – Chức năng đăng nhập



\## TC01: Đăng nhập thành công



\- \*\*Mục đích:\*\* Kiểm tra người dùng đăng nhập với thông tin hợp lệ.

\- \*\*Các bước thực hiện:\*\*

&#x20; 1. Truy cập https://the-internet.herokuapp.com/login.

&#x20; 2. Nhập tên đăng nhập và mật khẩu hợp lệ.

&#x20; 3. Nhấn nút Login.

\- \*\*Dữ liệu kiểm thử:\*\*

&#x20; - Username: `tomsmith`

&#x20; - Password: `SuperSecretPassword!`

\- \*\*Kết quả mong đợi:\*\* Đăng nhập thành công và hiển thị thông báo “You logged into a secure area!”.



\## TC02: Đăng nhập với tên đăng nhập sai



\- \*\*Mục đích:\*\* Kiểm tra hệ thống khi người dùng nhập sai tên đăng nhập.

\- \*\*Các bước thực hiện:\*\*

&#x20; 1. Truy cập trang đăng nhập.

&#x20; 2. Nhập tên đăng nhập không hợp lệ và mật khẩu hợp lệ.

&#x20; 3. Nhấn nút Login.

\- \*\*Dữ liệu kiểm thử:\*\*

&#x20; - Username: `sai\_ten`

&#x20; - Password: `SuperSecretPassword!`

\- \*\*Kết quả mong đợi:\*\* Đăng nhập thất bại và hiển thị thông báo tên đăng nhập không hợp lệ.



\## TC03: Đăng nhập với mật khẩu sai



\- \*\*Mục đích:\*\* Kiểm tra hệ thống khi người dùng nhập sai mật khẩu.

\- \*\*Các bước thực hiện:\*\*

&#x20; 1. Truy cập trang đăng nhập.

&#x20; 2. Nhập tên đăng nhập hợp lệ và mật khẩu không hợp lệ.

&#x20; 3. Nhấn nút Login.

\- \*\*Dữ liệu kiểm thử:\*\*

&#x20; - Username: `tomsmith`

&#x20; - Password: `sai\_mat\_khau`

\- \*\*Kết quả mong đợi:\*\* Đăng nhập thất bại và hiển thị thông báo mật khẩu không hợp lệ.

