
from selenium import webdriver


def test_smoke():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com")

        actual_title = driver.title
        expected_title = "The Internet"

        print("Tiêu đề thực tế:", actual_title)
        print("Tiêu đề mong đợi:", expected_title)

        assert actual_title == expected_title, (
            f"FAILED: Tiêu đề sai! "
            f"Mong đợi '{expected_title}', "
            f"nhưng nhận được '{actual_title}'"
        )

        print("PASSED: Tiêu đề website chính xác!")

    finally:
        driver.quit()
