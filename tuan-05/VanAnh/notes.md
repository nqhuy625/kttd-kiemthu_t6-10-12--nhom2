# Notes - Week 5: Kiểm thử chức năng đăng nhập

## 1. Những gì đã học được

- Biết sử dụng Selenium WebDriver để tự động mở trình duyệt Chrome và truy cập trang web.
- Biết dùng `find_element()` để tìm phần tử trên trang web bằng ID hoặc CSS Selector.
- Biết dùng `send_keys()` để nhập dữ liệu vào ô Username và Password.
- Biết dùng `click()` để nhấn nút Login.
- Biết sử dụng `assert` trong pytest để kiểm tra kết quả thực tế có đúng như mong đợi hay không.
- Biết sử dụng `WebDriverWait` để chờ phần tử xuất hiện trước khi kiểm tra.
- Đã viết và chạy thành công 3 test case: đăng nhập thành công, nhập sai mật khẩu và để trống thông tin đăng nhập.

## 2. Câu hỏi đọc tài liệu

### Câu 1: Selenium locator là gì? Có thể tìm phần tử bằng những cách nào?

Locator là cách xác định một phần tử HTML trên trang web để Selenium có thể tương tác với phần tử đó. Một số cách phổ biến là `By.ID`, `By.NAME`, `By.CSS_SELECTOR`, `By.XPATH` và `By.CLASS_NAME`.

Trong bài này, em sử dụng `By.ID` để tìm ô Username và Password, và `By.CSS_SELECTOR` để tìm nút Login.

### Câu 2: `assert` trong pytest có tác dụng gì?

`assert` dùng để so sánh kết quả thực tế với điều kiện mong đợi. Nếu điều kiện đúng, test tiếp tục chạy; nếu điều kiện sai, pytest đánh dấu test thất bại và hiển thị thông tin giúp xác định nguyên nhân.

## 3. Tự đánh giá và việc sử dụng AI

Em đã sử dụng AI để hỗ trợ hiểu yêu cầu bài tập, giải thích Selenium và pytest, hướng dẫn viết test case, sửa lỗi khi chạy test và hoàn thiện nội dung ghi chú. Em đã trực tiếp thực hiện các lệnh trên máy, kiểm tra phần tử HTML bằng Chrome DevTools và chạy lại test để xác nhận cả 3 test đều thành công.

Qua bài này, em hiểu rằng cần kiểm tra kết quả thực tế của website thay vì chỉ viết test theo kết quả mình dự đoán. Em cũng cần đọc và hiểu mã nguồn kiểm thử để có thể giải thích được cách hoạt động của từng bước.