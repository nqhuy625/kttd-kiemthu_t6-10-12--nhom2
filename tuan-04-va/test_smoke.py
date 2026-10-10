
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_smoke():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # Truy cập trang chủ của website kiểm thử
        driver.get("https://the-internet.herokuapp.com/")

        # Xác nhận tiêu đề trang chủ chính xác
        assert driver.title == "The Internet"
    finally:
        # Đóng trình duyệt kể cả khi kiểm thử thất bại
        driver.quit()


def test_checkbox_toggle():
    # Khởi tạo trình duyệt để kiểm tra chức năng checkbox
    driver = webdriver.Chrome()

    try:
        # Mở trang kiểm thử checkbox
        driver.get("https://the-internet.herokuapp.com/checkboxes")

        # Lấy danh sách các ô checkbox trên trang
        checkboxes = driver.find_elements(
            By.CSS_SELECTOR, "input[type='checkbox']"
        )

        # Đảm bảo trang có đủ hai ô checkbox
        assert len(checkboxes) == 2

        # Kiểm tra trạng thái ban đầu của ô checkbox thứ nhất
        assert not checkboxes[0].is_selected()

        # Chọn ô checkbox thứ nhất
        checkboxes[0].click()

        # Xác nhận ô checkbox đã được chọn
        assert checkboxes[0].is_selected()
    finally:
        # Đóng trình duyệt sau khi hoàn tất kiểm thử
        driver.quit()
