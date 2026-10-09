
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_smoke():
    # Bước 1: Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # Bước 2: Truy cập website cần kiểm thử
        driver.get("https://the-internet.herokuapp.com/login")

        # Bước 3: Chờ tối đa 10 giây để tìm phần tử
        wait = WebDriverWait(driver, 10)

        # Bước 4: Nhập tên đăng nhập
        username = wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        username.send_keys("tomsmith")

        # Bước 5: Nhập mật khẩu
        password = driver.find_element(By.ID, "password")
        password.send_keys("SuperSecretPassword!")

        # Bước 6: Nhấn nút Login
        login_button = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        login_button.click()

        # Bước 7: Kiểm tra kết quả đăng nhập
        success_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )

        assert "You logged into a secure area!" in success_message.text

    finally:
        # Bước 8: Đóng trình duyệt sau khi kiểm thử
        driver.quit()
