Selenium Smoke Test

1. Cài đặt môi trường

Cài đặt Python và trình duyệt Google Chrome trên máy tính.

Mở Terminal tại thư mục dự án và cài đặt các thư viện cần thiết:

pip install selenium pytest

2. Chạy kiểm thử

Đảm bảo file kiểm thử được đặt tên là test_smoke.py. Chạy lệnh sau trong Terminal:

pytest -v test_smoke.py

3. Kết quả

PASSED: Các điều kiện kiểm thử được đáp ứng.

FAILED: Có điều kiện kiểm thử không đáp ứng, chẳng hạn tiêu đề trang không đúng.