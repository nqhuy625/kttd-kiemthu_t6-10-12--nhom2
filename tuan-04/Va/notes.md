# Ghi chú kiểm thử tuần 4

## 1. Mục tiêu
Thực hành kiểm thử tự động bằng Selenium và pytest. Ngoài kiểm tra trang chủ, bài làm bổ sung kiểm thử thao tác chọn checkbox.

## 2. Công cụ sử dụng
- Python
- Selenium WebDriver
- pytest
- Google Chrome

## 3. Các trường hợp kiểm thử
- `test_smoke`: kiểm tra trang chủ mở được và có tiêu đề mong đợi.
- `test_checkbox_toggle`: kiểm tra số lượng checkbox, trạng thái ban đầu và việc chọn checkbox thứ nhất.

## 4. Cách chạy
Tại thư mục gốc của dự án, chạy:

```bash
python -m pytest -v tuan-04/test_smoke.py
```

## 5. Kết quả thực tế
Ghi số lượng kiểm thử thành công hoặc thất bại sau khi chạy pytest. Nếu có lỗi, nêu nguyên nhân và cách khắc phục.

## 6. Điều đã học
Tự ghi lại điều bạn hiểu về Selenium, pytest, cách xác nhận trạng thái checkbox và cách sử dụng `assert`.

## 7. Câu hỏi đọc tài liệu
Bổ sung câu trả lời cho 1–2 câu hỏi được giao trong tài liệu tuần 4.

## 8. Sử dụng AI
Ghi rõ bạn có sử dụng AI hỗ trợ hay không; nếu có, nêu phần được hỗ trợ và phần bạn đã tự kiểm tra, chỉnh sửa.
