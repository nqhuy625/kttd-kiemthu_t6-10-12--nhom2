Week 4 - Web Smoke Test

1. Mục tiêu
Xây dựng bài kiểm thử tự động cơ bản cho website [The Internet](https://the-internet.herokuapp.com) bằng Python, Selenium và pytest.

Bài kiểm thử thực hiện các công việc:
- Mở trình duyệt Google Chrome.
- Truy cập website cần kiểm thử.
- Lấy tiêu đề trang web.
- So sánh tiêu đề thực tế với tiêu đề mong đợi là `The Internet`.
- Hiển thị kết quả kiểm thử `PASSED` nếu đúng hoặc `FAILED` nếu sai.

2. Công cụ sử dụng
- Python
- Selenium WebDriver
- pytest
- Google Chrome
- Visual Studio Code

3. Cài đặt thư viện
Mở Terminal tại thư mục dự án và chạy lệnh: python -m pip install selenium pytest

Nếu lệnh `python` không hoạt động, có thể thử dùng `py`.

4. Cấu trúc dự án

BuiTThanhHien/
├── test_smoke.py
├── README.md
└── notes.md

5. Cách chạy kiểm thử

Mở Terminal tại thư mục dự án và chạy: python -m pytest test_smoke.py -v -s

Trong đó:
- test_smoke.py: file chứa mã kiểm thử.
- -v: hiển thị tên bài kiểm thử và kết quả chi tiết.
- -s: hiển thị các thông báo được in bằng `print()`.

6. Kết quả kiểm thử

-Trường hợp thành công:
Nếu tiêu đề website là `The Internet`, chương trình hiển thị thông báo `PASSED` và pytest đánh dấu bài kiểm thử là `PASSED`.

-Trường hợp thất bại:
Nếu tiêu đề không đúng với giá trị mong đợi, câu lệnh `assert` sẽ phát sinh lỗi và pytest đánh dấu bài kiểm thử là `FAILED`.

7. Kết luận
Bài thực hành giúp làm quen với việc kiểm thử website tự động bằng Selenium và pytest, sử dụng câu lệnh `assert` để xác minh kết quả và đọc trạng thái kiểm thử trong Terminal.