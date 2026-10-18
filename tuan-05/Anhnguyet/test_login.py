from selenium import webdriver
from selenium.webdriver.common.by import By


# Địa chỉ trang đăng nhập cần kiểm thử
LOGIN_URL = "https://the-internet.herokuapp.com/login"


def test_dang_nhap_thanh_cong():
    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()
    try:
        # Truy cập trang đăng nhập
        driver.get(LOGIN_URL)

        # Nhập tên đăng nhập và mật khẩu hợp lệ
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        # Nhấn nút Login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Lấy thông báo sau khi đăng nhập
        thong_bao = driver.find_element(By.ID, "flash").text

        # Kiểm tra đăng nhập thành công
        assert "You logged into a secure area!" in thong_bao
    finally:
        # Đóng trình duyệt sau khi kiểm thử
        driver.quit()


def test_dang_nhap_sai_ten():
    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()
    try:
        # Truy cập trang đăng nhập
        driver.get(LOGIN_URL)

        # Nhập tên đăng nhập sai và mật khẩu đúng
        driver.find_element(By.ID, "username").send_keys("sai_ten")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

        # Nhấn nút Login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Lấy thông báo lỗi
        thong_bao = driver.find_element(By.ID, "flash").text

        # Kiểm tra thông báo tên đăng nhập không hợp lệ
        assert "Your username is invalid!" in thong_bao
    finally:
        # Đóng trình duyệt sau khi kiểm thử
        driver.quit()


def test_dang_nhap_sai_mat_khau():
    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()
    try:
        # Nhập tên đăng nhập đúng và mật khẩu sai
        driver.get(LOGIN_URL)
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("sai_mat_khau")

        # Nhấn nút Login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Lấy thông báo lỗi
        thong_bao = driver.find_element(By.ID, "flash").text

        # Kiểm tra thông báo mật khẩu không hợp lệ
        assert "Your password is invalid!" in thong_bao
    finally:
        # Đóng trình duyệt sau khi kiểm thử
        driver.quit()