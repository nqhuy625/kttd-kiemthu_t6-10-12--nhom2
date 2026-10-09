# Kiểm thử tự động - Tuần 4

## 1. Giới thiệu

Dự án thực hành kiểm thử tự động trên trình duyệt web bằng Selenium và pytest.

Bài kiểm thử đầu tiên truy cập trang The Internet và kiểm tra tiêu đề trang web.

## 2. Công cụ sử dụng

- Python chạy chương trình kiểm thử.
- Selenium tự động điều khiển trình duyệt.
- pytest thực thi bài kiểm thử và hiển thị kết quả.
- Google Chrome trình duyệt được kiểm thử.

## 3. Cài đặt môi trường

Cài đặt Python và Google Chrome trên máy tính.

Mở CMD và chạy lệnh cài đặt thư viện

```bash
python -m pip install selenium pytest
```

Kiểm tra các thư viện đã được cài đặt

```bash
python -m pip show selenium
python -m pip show pytest
```

## 4. Cấu trúc thư mục

```text
kiem_thu_tu_dong
├── README.md
└── tuan04
    ├── test_smoke.py
    └── anh
```

Thư mục `anh` dùng để lưu ảnh chụp kết quả kiểm thử.

## 5. Cách chạy bài kiểm thử

Mở thư mục `Ckiem_thu_tu_dongtuan04` bằng File Explorer.

Bấm vào thanh địa chỉ, nhập `cmd` rồi nhấn Enter.

Chạy lệnh

```bash
python -m pytest test_smoke.py -v
```

Nếu kiểm thử thành công, kết quả sẽ hiển thị `PASSED` và tổng kết `1 passed`.

## 6. Nội dung bài kiểm thử

- Mở trang web httpsthe-internet.herokuapp.com
- Lấy tiêu đề trang bằng Selenium.
- Kiểm tra tiêu đề có bằng `The Internet` hay không.
- Đóng trình duyệt sau khi hoàn thành bài kiểm thử.

## 7. Kết quả

Ghi nhận kết quả chạy kiểm thử và lưu ảnh minh chứng trong thư mục `tuan04anh`.