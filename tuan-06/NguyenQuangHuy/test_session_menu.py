import argparse
import json
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from test_login import APPIUM_SERVER, APK_PATH, capabilities


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence-dir', type=Path, default=Path(__file__).resolve().parents[2] / 'build' / 'week06-session-menu')
    args = parser.parse_args()
    args.evidence_dir.mkdir(parents=True, exist_ok=True)
    if not APK_PATH.is_file():
        raise FileNotFoundError(f'Không tìm thấy APK: {APK_PATH}')

    # Giữ dữ liệu đã có; nếu đang ở Login thì đăng nhập, không reset app.
    requested = dict(capabilities)
    requested['appium:noReset'] = True
    options = UiAutomator2Options().load_capabilities(requested)
    driver = None
    result = {'status': 'FAIL', 'server': APPIUM_SERVER}
    try:
        print('1. Tạo Android session qua webdriver.Remote...', flush=True)
        driver = webdriver.Remote(command_executor=APPIUM_SERVER, options=options)
        session_id = driver.session_id
        assert session_id, 'Server chưa cấp session_id'
        result['session_id'] = session_id
        result['capabilities'] = driver.capabilities
        print('SESSION ID:', session_id, flush=True)
        print('CAPABILITIES (server trả về):', flush=True)
        print(json.dumps(driver.capabilities, ensure_ascii=False, indent=2), flush=True)
        assert driver.capabilities.get('platformName', '').lower() == 'android'

        wait = WebDriverWait(driver, 30, ignored_exceptions=(NoSuchElementException, StaleElementReferenceException))

        def visible(accessibility_id):
            return any(e.is_displayed() for e in driver.find_elements(AppiumBy.ACCESSIBILITY_ID, accessibility_id))

        def click(accessibility_id):
            element = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, accessibility_id)))
            element.click()

        def save(name):
            (args.evidence_dir / f'{name}.xml').write_text(driver.page_source, encoding='utf-8')
            driver.save_screenshot(str(args.evidence_dir / f'{name}.png'))

        # Chuẩn bị từ màn hình Login hoặc PRODUCTS; không tự xử lý màn hình lạ.
        wait.until(lambda d: visible('test-Username') or visible('test-PRODUCTS'))
        if visible('test-Username'):
            print('2. Đăng nhập standard_user...', flush=True)
            for locator, value in [('test-Username', 'standard_user'), ('test-Password', 'secret_sauce')]:
                def enter(d, locator=locator, value=value):
                    element = d.find_element(AppiumBy.ACCESSIBILITY_ID, locator)
                    if not element.is_displayed():
                        return False
                    element.clear()
                    element.send_keys(value)
                    return True
                wait.until(enter)
            click('test-LOGIN')
        else:
            print('2. Đã đăng nhập từ trước; giữ dữ liệu hiện có.', flush=True)

        # Nếu lần thao tác thủ công trước còn mở Menu, đóng bằng Close ở setup.
        if visible('test-Close'):
            click('test-Close')
            wait.until(lambda d: not visible('test-Close'))
        assert wait.until(lambda d: visible('test-PRODUCTS'))
        print('PASS: PRODUCTS hiển thị.', flush=True)
        save('01-products')

        print('3. Mở Menu bằng Accessibility ID test-Menu...', flush=True)
        click('test-Menu')
        markers = ('test-Close', 'test-ALL ITEMS', 'test-LOGOUT')
        assert wait.until(lambda d: all(visible(marker) for marker in markers)), 'Menu chưa mở đủ'
        print('PASS: Menu hiển thị Close, ALL ITEMS, LOGOUT.', flush=True)
        save('02-menu-open')

        print('4. Gọi driver.back(): gửi Android Back...', flush=True)
        driver.back()
        assert wait.until(lambda d: all(not visible(marker) for marker in markers) and visible('test-PRODUCTS')), 'Back chưa đóng Menu và trở về PRODUCTS'
        assert driver.current_package == 'com.swaglabsmobileapp', 'Đã rời ứng dụng Swag Labs'
        assert driver.session_id == session_id, 'Session đã thay đổi ngoài ý muốn'
        save('03-after-back')
        result['status'] = 'PASS'
        print('PASS: Android Back đóng Menu; PRODUCTS hiển thị; session giữ nguyên.', flush=True)
    except Exception as error:
        result['error'] = repr(error)
        print(f'FAIL: {error}', flush=True)
        raise
    finally:
        try:
            if driver is not None:
                driver.quit()
                result['session_closed'] = True
                print('Đã đóng Appium session bằng driver.quit().', flush=True)
        except Exception as error:
            result['status'] = 'FAIL'
            result['quit_error'] = repr(error)
            raise
        finally:
            (args.evidence_dir / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print('PASS: DEMO A4 TUẦN 6 HOÀN TẤT.', flush=True)


if __name__ == '__main__':
    main()
