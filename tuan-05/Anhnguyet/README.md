\# Tuần 5 - Kiểm thử chức năng đăng nhập



\## 1. Mục tiêu

Viết và chạy 3 bài kiểm thử chức năng đăng nhập bằng Selenium và pytest.



\## 2. Các trường hợp kiểm thử

\- Đăng nhập thành công với thông tin hợp lệ.

\- Đăng nhập thất bại khi tên đăng nhập sai.

\- Đăng nhập thất bại khi mật khẩu sai.



\## 3. Cài đặt

Mở CMD tại thư mục chứa file và chạy:



```bash

python -m pip install -r requirements.txt

```



\## 4. Chạy kiểm thử

Chạy lệnh:



```bash

python -m pytest test\_login.py -v

```



\## 5. Kết quả

Cả 3 bài kiểm thử đã chạy thành công. Tổng kết quả: 3 passed.

