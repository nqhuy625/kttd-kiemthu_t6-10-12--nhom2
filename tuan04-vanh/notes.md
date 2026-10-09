# Ghi chú học tập - Tuần 4

## 1. Nội dung đã học

Trong tuần 4, em thực hành kiểm thử tự động website bằng Python, Selenium và pytest.

Em đã tạo file `test_smoke.py`, sử dụng Selenium để mở trình duyệt Chrome và truy cập trang web https://the-internet.herokuapp.com/.

Sau đó, em sử dụng pytest để chạy bài kiểm thử và kiểm tra tiêu đề trang web có đúng là `The Internet` hay không.

## 2. Cách chạy bài kiểm thử

Mở CMD tại thư mục `C:\kiem_thu_tu_dong\tuan04` và chạy lệnh:

```bash
python -m pytest test_smoke.py -v
```

Kết quả thành công hiển thị `PASSED` và `1 passed`.

## 3. Kiến thức rút ra

- Selenium giúp tự động điều khiển trình duyệt.
- pytest giúp chạy các hàm kiểm thử và hiển thị kết quả.
- Tên file kiểm thử cần đúng với tên được sử dụng trong lệnh chạy.
- Khi gặp lỗi, cần đọc thông báo lỗi và kiểm tra đường dẫn file, môi trường Python và trình duyệt.

## 4. Câu hỏi tự ôn tập

**Câu 1: Selenium dùng để làm gì?**

Trả lời: Selenium được sử dụng để tự động hóa thao tác trên trình duyệt web, chẳng hạn như mở trang web và lấy tiêu đề trang.

**Câu 2: pytest dùng để làm gì?**

Trả lời: pytest là công cụ chạy kiểm thử Python, giúp phát hiện và báo cáo các bài kiểm thử thành công hoặc thất bại.

**Câu 3: `PASSED` có nghĩa là gì?**

Trả lời: Bài kiểm thử đã chạy và tất cả các điều kiện kiểm tra trong bài đó đều đạt yêu cầu.

## 5. Quá trình sử dụng AI

Em đã sử dụng AI để được hướng dẫn tạo file kiểm thử, chạy pytest và tìm nguyên nhân lỗi. Em đã thực hành các lệnh trên máy tính và quan sát kết quả chạy kiểm thử.

## 6. Kết quả thực hành

Bài kiểm thử `test_smoke.py` đã chạy thành công với kết quả `1 passed`.

