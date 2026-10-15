# GHI CHÚ THỰC HÀNH TUẦN 5

**Họ và tên:** Nguyễn Quang Huy  
**Nhóm:** 2  
**Chủ đề:** Viết bài kiểm thử tự động cho chức năng Đăng nhập  
**Công cụ:** Python, Selenium, pytest, Google Chrome, VS Code  
**Website kiểm thử:** https://the-internet.herokuapp.com/login

---

## 1. Nội dung thực hành

Trong tuần 5, em tiếp tục thực hành kiểm thử tự động Web bằng Selenium và pytest, tập trung vào chức năng đăng nhập.

Các nội dung thực hiện bao gồm:

- Tìm hiểu cách xác định phần tử trên giao diện Web bằng ID, Name, CSS Selector và XPath.
- Sử dụng Chrome DevTools để kiểm tra cấu trúc HTML và xác định locator của ô Username, Password và nút Login.
- Xây dựng ba test case trước khi viết code, gồm đăng nhập thành công, đăng nhập sai mật khẩu và đăng nhập sai tên tài khoản.
- Viết chương trình kiểm thử bằng Python kết hợp Selenium WebDriver và pytest.
- Sử dụng các thao tác `send_keys()`, `click()` để mô phỏng hành động của người dùng.
- Sử dụng `WebDriverWait` để chờ phần tử xuất hiện và `assert` để đối chiếu kết quả thực tế với kết quả mong đợi.
- Thực hiện chạy kiểm thử và kiểm tra kết quả trong Terminal của VS Code.

## 2. Kiến thức học được

### 2.1. Cách xác định phần tử (Locator)

Selenium cung cấp nhiều cách tìm phần tử trên trang Web như ID, Name, CSS Selector và XPath.

Khi một phần tử có ID duy nhất và ổn định, ưu tiên sử dụng ID vì cú pháp ngắn gọn, dễ hiểu và ít phụ thuộc vào cấu trúc HTML. CSS Selector được sử dụng khi cần xác định phần tử dựa trên thẻ HTML, class hoặc thuộc tính.

Ví dụ:

```python
driver.find_element(By.ID, "username")
driver.find_element(By.ID, "password")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
```

### 2.2. Thao tác với phần tử

- `send_keys()`: Nhập dữ liệu vào ô nhập liệu.
- `click()`: Thực hiện thao tác nhấn nút.
- `find_element()`: Tìm một phần tử trên trang Web.
- `WebDriverWait()`: Chờ phần tử đáp ứng điều kiện xác định trong khoảng thời gian cho phép.

Ví dụ:

```python
username_input.send_keys("tomsmith")
login_button.click()
```

### 2.3. Kiểm tra kết quả bằng assert

Câu lệnh `assert` dùng để xác nhận kết quả thực tế có đáp ứng điều kiện mong đợi hay không.

Ví dụ:

```python
assert "You logged into a secure area!" in message
```

Nếu điều kiện đúng, bài kiểm thử tiếp tục và có thể đạt PASS. Nếu điều kiện sai, pytest báo `AssertionError` và đánh dấu bài kiểm thử FAILED.

## 3. Trả lời câu hỏi sau khi đọc tài liệu

**Câu hỏi 1: Vì sao nên ưu tiên sử dụng ID khi tìm phần tử trên giao diện Web?**

ID thường giúp xác định phần tử một cách trực tiếp, cú pháp ngắn gọn và dễ bảo trì. Nếu ID là duy nhất và không thường xuyên thay đổi, bài kiểm thử sẽ ít bị ảnh hưởng bởi các thay đổi về bố cục HTML. Tuy nhiên, nếu ID được tạo động hoặc không ổn định thì nên cân nhắc sử dụng locator khác.

**Câu hỏi 2: Nếu kết quả thực tế khác kết quả mong đợi thì pytest báo gì?**

Khi điều kiện `assert` không đúng, pytest đánh dấu bài kiểm thử là FAILED và hiển thị lỗi `AssertionError`, kèm theo thông tin về điều kiện kiểm tra không đạt. Điều này giúp xác định nguyên nhân thất bại để kiểm tra lại code, dữ liệu hoặc hành vi của website.

## 4. Kết quả thực hành

Xây dựng ba trường hợp kiểm thử chức năng đăng nhập:

| Mã | Trường hợp kiểm thử | Kết quả mong đợi |
|---|---|---|
| TC01 | Đăng nhập với tài khoản và mật khẩu hợp lệ | Đăng nhập thành công, chuyển đến trang `/secure`. |
| TC02 | Đăng nhập đúng tài khoản nhưng sai mật khẩu | Hiển thị thông báo `Your password is invalid!`. |
| TC03 | Đăng nhập sai tên tài khoản | Hiển thị thông báo `Your username is invalid!`. |

**Kết quả chạy thực tế:** PASS

**Ảnh minh chứng:** `anh/Tuan05_3PASS.png`

Qua việc thực hành, em hiểu rằng một test case đăng nhập thất bại vẫn được đánh giá PASS nếu hệ thống từ chối đăng nhập đúng với kết quả mong đợi.


## 5. Khó khăn và cách giải quyết

Trong quá trình chuẩn bị bài kiểm thử, em đã chạy lệnh pytest khi file `test_login.py` chưa có các hàm kiểm thử hoàn chỉnh. Vì vậy, Terminal hiển thị:

```text
collected 0 items
no tests ran
```

Sau khi tìm hiểu, xác định được pytest cần có các hàm kiểm thử được khai báo đúng quy tắc, chẳng hạn tên hàm bắt đầu bằng `test_`, để có thể nhận diện và thực thi.

**Cách xử lý:** Hoàn thiện nội dung file `test_login.py`, lưu file bằng `Ctrl + S`, kiểm tra khả năng nhận diện các hàm kiểm thử và chạy lại bằng lệnh:

```powershell
python -m pytest tuan-05/NguyenQuangHuy/test_login.py -v
```

**Kết quả sau khi xử lý:** 3 mục đều PASS

## 6. Sử dụng AI trong quá trình học tập

- **Công cụ sử dụng:** ChatGPT.
- **Mục đích:** Hỗ trợ tìm hiểu cách xây dựng test case, giải thích Selenium locator, thao tác với phần tử, cú pháp pytest và cách kiểm tra kết quả bằng assert.
- **Nội dung hỗ trợ:** Tham khảo cấu trúc bài kiểm thử, giải thích các đoạn code và hướng dẫn xử lý lỗi khi thực hành.
- **Phần tự thực hiện:** Thao tác trên VS Code, kiểm tra code, chạy thử trên môi trường cá nhân và đối chiếu kết quả thực tế. Các hoạt động theo cặp và kiểm tra chéo được ghi nhận theo quá trình thực hiện thực tế.

## 7. Kết luận

Bài thực hành Tuần 5 giúp em hiểu rõ hơn quy trình xây dựng một bài kiểm thử tự động cho chức năng đăng nhập, từ việc xác định yêu cầu, viết test case, tìm phần tử trên giao diện đến thực hiện thao tác và kiểm tra kết quả.

Qua đó, em nhận thấy việc xây dựng điều kiện kiểm tra chính xác bằng `assert` và lựa chọn locator phù hợp có vai trò quan trọng trong việc đảm bảo chất lượng bài kiểm thử tự động.