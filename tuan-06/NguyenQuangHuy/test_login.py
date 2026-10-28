from pathlib import Path
import sys

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


# Bảo đảm PowerShell/Terminal trên Windows in đúng thông báo tiếng Việt.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


APPIUM_SERVER = "http://127.0.0.1:4723"
APK_PATH = Path(r"C:\MobileTesting\apps\swaglabs-2.7.1.apk")


capabilities = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "A4_API33",
    "appium:udid": "emulator-5554",
    "appium:app": str(APK_PATH),
    "appium:appWaitPackage": "com.swaglabsmobileapp",
    "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity",
    "appium:noReset": False,
    "appium:newCommandTimeout": 180,
    "appium:adbExecTimeout": 120000,
    "appium:uiautomator2ServerInstallTimeout": 120000,
    "appium:uiautomator2ServerLaunchTimeout": 120000,
}


def main():
    if not APK_PATH.exists():
        raise FileNotFoundError(f"Không tìm thấy APK: {APK_PATH}")

    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = None

    try:
        print("Đang tạo phiên Appium...")
        driver = webdriver.Remote(
            command_executor=APPIUM_SERVER,
            options=options,
        )

        wait = WebDriverWait(
            driver,
            30,
            ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
        )

        def enter_text(accessibility_id, value):
            def attempt(current_driver):
                element = current_driver.find_element(
                    AppiumBy.ACCESSIBILITY_ID, accessibility_id
                )
                if not element.is_displayed():
                    return False
                element.clear()
                element.send_keys(value)
                return True

            wait.until(attempt)

        def click_element(accessibility_id):
            def attempt(current_driver):
                element = current_driver.find_element(
                    AppiumBy.ACCESSIBILITY_ID, accessibility_id
                )
                if not element.is_displayed() or not element.is_enabled():
                    return False
                element.click()
                return True

            wait.until(attempt)

        print("Đang nhập tài khoản...")
        enter_text("test-Username", "standard_user")
        enter_text("test-Password", "secret_sauce")

        print("Đang nhấn LOGIN...")
        click_element("test-LOGIN")

        products_visible = wait.until(
            lambda current_driver: current_driver.find_element(
                AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS"
            ).is_displayed()
        )

        assert products_visible, (
            "Không tìm thấy màn hình PRODUCTS sau đăng nhập"
        )

        print("PASS: Đăng nhập thành công và PRODUCTS đã xuất hiện.")

    except Exception as error:
        print(f"FAIL: {error}")
        raise

    finally:
        if driver is not None:
            driver.quit()
            print("Đã đóng phiên Appium.")


if __name__ == "__main__":
    main()
