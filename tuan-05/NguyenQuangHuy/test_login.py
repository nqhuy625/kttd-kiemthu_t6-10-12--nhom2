
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://the-internet.herokuapp.com/login"


# Khoi tao va dong Chrome sau moi bai kiem thu
@pytest.fixture
def driver():
    browser = webdriver.Chrome()

    try:
        yield browser
    finally:
        browser.quit()


# Ham dung chung de thuc hien dang nhap
def login(driver, username, password):
    # Buoc 1: Mo trang dang nhap
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    # Buoc 2: Tim va nhap username
    username_input = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "username")
        )
    )
    username_input.send_keys(username)

    # Buoc 3: Tim va nhap password
    password_input = driver.find_element(
        By.ID, "password"
    )
    password_input.send_keys(password)

    # Buoc 4: Bam nut Login
    login_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )
    login_button.click()

    # Buoc 5: Lay thong bao ket qua
    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "flash")
        )
    )

    return message.text


# TC01: Dang nhap thanh cong
def test_login_success(driver):
    message = login(
        driver,
        "tomsmith",
        "SuperSecretPassword!"
    )

    assert "You logged into a secure area!" in message
    assert driver.current_url.endswith("/secure")


# TC02: Dang nhap sai mat khau
def test_login_wrong_password(driver):
    message = login(
        driver,
        "tomsmith",
        "WrongPassword123"
    )

    assert "Your password is invalid!" in message
    assert not driver.current_url.endswith("/secure")


# TC03: Dang nhap sai ten tai khoan
def test_login_wrong_username(driver):
    message = login(
        driver,
        "wronguser123",
        "SuperSecretPassword!"
    )

    assert "Your username is invalid!" in message
    assert not driver.current_url.endswith("/secure")
