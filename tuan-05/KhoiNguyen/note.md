Notes - Week 5: Kiểm thử chức năng đăng nhập
1. Những gì đã học được
Biết sử dụng Selenium WebDriver để tự động mở trình duyệt Chrome và truy cập trang web.
Biết dùng find_element() để tìm phần tử trên trang web bằng ID hoặc CSS Selector.
Biết dùng send_keys() để nhập dữ liệu vào ô Username và Password.
Biết dùng click() để nhấn nút Login.
Biết sử dụng assert trong pytest để kiểm tra kết quả thực tế có đúng như mong đợi hay không.
Biết sử dụng WebDriverWait để chờ phần tử xuất hiện trước khi kiểm tra.
Đã viết và chạy thành công 3 test case: đăng nhập thành công, nhập sai mật khẩu và để trống thông tin đăng nhập.

2. Câu hỏi đọc tài liệu
Câu 1: assert trong pytest có tác dụng gì?
Trong pytest, assert dùng để kiểm tra kết quả thực tế có đúng với kết quả mong đợi hay không. Nếu đúng, bài kiểm thử vượt qua (PASSED). Nếu sai, bài kiểm thử thất bại (FAILED).