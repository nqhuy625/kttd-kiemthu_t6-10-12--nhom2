
# Ham xu ly dang nhap
def login(username, password):
    # Kiem tra du lieu rong
    if username == "" or password == "":
        return "Vui long nhap day du thong tin"

    # Kiem tra tai khoan va mat khau
    if username == "admin" and password == "123456":
        return "Dang nhap thanh cong"

    return "Sai tai khoan hoac mat khau"


# TC01: Dang nhap voi tai khoan va mat khau dung
def test_login_success():
    result = login("admin", "123456")
    assert result == "Dang nhap thanh cong"


# TC02: Dang nhap voi mat khau sai
def test_login_wrong_password():
    result = login("admin", "123")
    assert result == "Sai tai khoan hoac mat khau"


# TC03: Dang nhap khi bo trong thong tin
def test_login_empty():
    result = login("", "")
    assert result == "Vui long nhap day du thong tin"
