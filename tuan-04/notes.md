# Ghi chú kiểm thử tuần 4

## 1. Mục tiêu
Kiểm tra trang web https://the-internet.herokuapp.com/ có mở được và có tiêu đề đúng là "The Internet" hay không.

## 2. Công cụ sử dụng
- Python
- Selenium
- pytest
- Google Chrome

## 3. Cách chạy kiểm thử
Mở CMD tại thư mục `tuan-04` và chạy lệnh:

```bash
python -m pytest test_smoke.py -v
```

## 4. Kết quả kiểm thử
- Kiểm thử thành công: trang web mở được và tiêu đề đúng là "The Internet".
- Kiểm thử thất bại: thay đổi tiêu đề mong đợi thành một giá trị sai để kiểm tra pytest có phát hiện lỗi hay không.

## 5. Kết luận
Bài kiểm thử smoke test chạy được bằng Selenium và pytest. Sau khi thử tạo lỗi, cần khôi phục điều kiện kiểm tra ban đầu và chạy lại để bảo đảm bài kiểm thử thành công.