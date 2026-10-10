
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_smoke():
    # Khởi tạo trình duyệt Chrome
    browser = webdriver.Chrome()

    try:
        # Mở trang web kiểm thử
        browser.get("https://the-internet.herokuapp.com/")
        time.sleep(2)

        # Lấy tiêu đề thực tế và tiêu đề mong đợi
        actual_title = browser.title
        expected_title = "The Internet"

        # Kiểm tra tiêu đề trang
        if actual_title != expected_title:
            print("Sai tiêu đề!")
            print("Tiêu đề mong đợi:", expected_title)
            print("Tiêu đề thực tế:", actual_title)

        assert actual_title == expected_title, "Kiểm thử thất bại: Sai tiêu đề!"

        # Kiểm tra tiêu đề chính trên trang
        heading = browser.find_element(By.TAG_NAME, "h1")
        assert heading.is_displayed(), "Tiêu đề chính không hiển thị!"

        print("Kiểm thử thành công!")

    finally:
        # Đóng trình duyệt sau khi kiểm thử
        browser.quit()
