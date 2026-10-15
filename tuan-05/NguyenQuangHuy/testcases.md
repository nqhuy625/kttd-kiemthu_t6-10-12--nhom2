# TEST CASES – KIỂM THỬ CHỨC NĂNG ĐĂNG NHẬP

**Họ và tên:** Nguyễn Quang Huy  
**Nhóm:** 2  
**Tuần:** 05  
**Chức năng kiểm thử:** Đăng nhập (Login)  
**Loại kiểm thử:** Kiểm thử tự động Web  
**Công cụ:** Python, Selenium, pytest, Google Chrome  
**Website:** https://the-internet.herokuapp.com/login

---

## TC01 – Đăng nhập thành công với tài khoản hợp lệ

**Mục tiêu:** Kiểm tra hệ thống cho phép người dùng đăng nhập khi nhập đúng tên tài khoản và mật khẩu.

**Tiền điều kiện:**
- Website hoạt động bình thường.
- Người dùng đang ở trang đăng nhập.
- Trình duyệt Chrome đã được cài đặt.

**Dữ liệu kiểm thử:**
- Username: `tomsmith`
- Password: `SuperSecretPassword!`

**Các bước thực hiện:**

| Bước | Thao tác | Kết quả mong đợi |
|---|---|---|
| 1 | Truy cập `https://the-internet.herokuapp.com/login` | Hiển thị trang đăng nhập với hai ô Username, Password và nút Login. |
| 2 | Nhập `tomsmith` vào ô Username | Tên tài khoản được nhập vào đúng ô Username. |
| 3 | Nhập `SuperSecretPassword!` vào ô Password | Mật khẩu được nhập vào ô Password. |
| 4 | Nhấn nút Login | Hệ thống tiếp nhận và xử lý yêu cầu đăng nhập. |
| 5 | Kiểm tra thông báo và URL sau đăng nhập | Hiển thị thông báo `You logged into a secure area!` và chuyển đến trang `/secure`. |

**Kết quả mong đợi cuối cùng:** Đăng nhập thành công, hiển thị thông báo xác nhận và chuyển đến trang bảo mật.

**Kết quả thực tế:** Hiển thị thông báo thành công, chuyển đến /secure

**Trạng thái:** PASS.

---

## TC02 – Đăng nhập thất bại khi nhập sai mật khẩu

**Mục tiêu:** Kiểm tra hệ thống từ chối đăng nhập khi người dùng nhập đúng tên tài khoản nhưng sai mật khẩu.

**Tiền điều kiện:**
- Website hoạt động bình thường.
- Người dùng đang ở trang đăng nhập.
- Trình duyệt Chrome đã được cài đặt.

**Dữ liệu kiểm thử:**
- Username: `tomsmith`
- Password: `WrongPassword123`

**Các bước thực hiện:**

| Bước | Thao tác | Kết quả mong đợi |
|---|---|---|
| 1 | Truy cập `https://the-internet.herokuapp.com/login` | Hiển thị trang đăng nhập. |
| 2 | Nhập `tomsmith` vào ô Username | Tên tài khoản được nhập chính xác. |
| 3 | Nhập `WrongPassword123` vào ô Password | Mật khẩu sai được nhập vào ô Password. |
| 4 | Nhấn nút Login | Hệ thống tiếp nhận và kiểm tra thông tin đăng nhập. |
| 5 | Kiểm tra thông báo và URL sau đăng nhập | Hiển thị thông báo `Your password is invalid!` và không chuyển đến trang `/secure`. |

**Kết quả mong đợi cuối cùng:** Đăng nhập thất bại, hệ thống hiển thị thông báo mật khẩu không hợp lệ và không cho phép truy cập trang bảo mật.

**Kết quả thực tế:** Hiển thị lỗi mật khẩu, không vào /secure

**Trạng thái:** PASS.

---

## TC03 – Đăng nhập thất bại khi nhập sai tên tài khoản

**Mục tiêu:** Kiểm tra hệ thống từ chối đăng nhập khi người dùng nhập sai tên tài khoản dù mật khẩu được nhập đúng.

**Tiền điều kiện:**
- Website hoạt động bình thường.
- Người dùng đang ở trang đăng nhập.
- Trình duyệt Chrome đã được cài đặt.

**Dữ liệu kiểm thử:**
- Username: `wronguser123`
- Password: `SuperSecretPassword!`

**Các bước thực hiện:**

| Bước | Thao tác | Kết quả mong đợi |
|---|---|---|
| 1 | Truy cập `https://the-internet.herokuapp.com/login` | Hiển thị trang đăng nhập. |
| 2 | Nhập `wronguser123` vào ô Username | Tên tài khoản không hợp lệ được nhập vào ô Username. |
| 3 | Nhập `SuperSecretPassword!` vào ô Password | Mật khẩu được nhập vào ô Password. |
| 4 | Nhấn nút Login | Hệ thống tiếp nhận và kiểm tra thông tin đăng nhập. |
| 5 | Kiểm tra thông báo và URL sau đăng nhập | Hiển thị thông báo `Your username is invalid!` và không chuyển đến trang `/secure`. |

**Kết quả mong đợi cuối cùng:** Đăng nhập thất bại, hệ thống hiển thị thông báo tên tài khoản không hợp lệ và không cho phép truy cập trang bảo mật.

**Kết quả thực tế:** Hiển thị lỗi tài khoản, không vào /secure

**Trạng thái:** PASS

---

## 4. Tổng hợp kết quả kiểm thử

| Mã test case | Tên bài kiểm thử | Kết quả mong đợi | Trạng thái |
|---|---|---|---|
| TC01 | Đăng nhập thành công | Hiển thị thông báo thành công và chuyển đến `/secure` | Chờ xác nhận |
| TC02 | Đăng nhập sai mật khẩu | Hiển thị lỗi mật khẩu và từ chối đăng nhập | Chờ xác nhận |
| TC03 | Đăng nhập sai tên tài khoản | Hiển thị lỗi tài khoản và từ chối đăng nhập | Chờ xác nhận |

**Tổng số test case:** 3  
**Số test case PASS:** 3 
**Số test case FAIL:** 0  

**Lệnh thực hiện kiểm thử:**

```powershell
python -m pytest tuan-05/NguyenQuangHuy/test_login.py -v
```

**Minh chứng:** `anh/Tuan05_3PASS.png` 

## 5. Nhận xét

Bộ test case bao gồm một trường hợp đăng nhập hợp lệ và hai trường hợp đăng nhập không hợp lệ, giúp kiểm tra các thao tác nhập dữ liệu, nhấn nút đăng nhập và xác nhận thông báo phản hồi của hệ thống.

Các bài kiểm thử được xây dựng theo ba bước chính: xác định phần tử bằng Selenium locator, thực hiện thao tác bằng Selenium WebDriver và kiểm tra kết quả bằng câu lệnh `assert` trong pytest.

