#TC01: ĐĂNG NHẬP THÀNH CỐNG
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_success():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # Mở trang đăng nhập
        driver.get("https://the-internet.herokuapp.com/login")

        # Tìm ô Username và nhập tên đăng nhập
        driver.find_element(By.ID, "username").send_keys("tomsmith")

        # Tìm ô Password và nhập mật khẩu
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        # Tìm nút Login và nhấn
        driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        ).click()

        # Chờ thông báo kết quả xuất hiện
        thong_bao = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        # Kiểm tra thông báo có nội dung đăng nhập thành công
        assert "You logged into a secure area!" in thong_bao.text

        # Kiểm tra đã chuyển đến trang secure
        assert "/secure" in driver.current_url

    finally:
        # Đóng trình duyệt kể cả khi test bị lỗi
        driver.quit()
#TCO2
def test_login_wrong_password():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # Mở trang đăng nhập
        driver.get("https://the-internet.herokuapp.com/login")

        # Nhập username đúng
        driver.find_element(By.ID, "username").send_keys("tomsmith")

        # Nhập mật khẩu sai
        driver.find_element(By.ID, "password").send_keys("WrongPassword123")

        # Nhấn nút Login
        driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        ).click()

        # Chờ thông báo lỗi xuất hiện
        thong_bao = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        # Kiểm tra thông báo cho biết đăng nhập thất bại
        assert "Your password is invalid!" in thong_bao.text

    finally:
        # Đóng trình duyệt
        driver.quit()


def test_login_empty_fields():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # Mở trang đăng nhập, không nhập thông tin
        driver.get("https://the-internet.herokuapp.com/login")

        # Nhấn Login khi cả hai ô đều để trống
        driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]'
        ).click()

        # Chờ thông báo phản hồi xuất hiện
        thong_bao = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        # Kiểm tra hệ thống không cho đăng nhập thành công
        assert "Your username is invalid!" in thong_bao.text

    finally:
        # Đóng trình duyệt
        driver.quit()

