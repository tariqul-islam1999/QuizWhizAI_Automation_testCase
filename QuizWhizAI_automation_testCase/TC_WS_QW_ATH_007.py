# verify that users can login as user with the " Remember Me " option .

import time

from selenium import webdriver

def test_TC_WS_QW_ATH_007 () :
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ai-quizwhiz.zluck.com/login")

    # getting user name
    userNameBox = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    userNameBox.clear()
    userNameBox.send_keys("user@gmail.com")

    # getting password
    passwordBox = driver.find_element("xpath", "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    passwordBox.clear()
    passwordBox.send_keys("123456")

    # click on remember me
    rememberMeBox = driver.find_element("xpath",    "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[4]/div/div/div/label/input")
    rememberMeBox.click()

    # click on User
    UserBox = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[5]/div/div/button[2]")
    UserBox.click()
    time.sleep(5)

    # click on Sign On Button
    signInBtn = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    signInBtn.click()

    driver.implicitly_wait(10)

    # User Dashboard
    user_dashboard_title = driver.find_element("xpath", "/html/body/div[1]/div[1]/main/div/section/header/div[1]/h1")
    assert (user_dashboard_title.text == "Dashboard")

    time.sleep(5)