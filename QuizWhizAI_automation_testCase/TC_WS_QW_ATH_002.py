# verify that users can login with invalid data as admin.

import time

from selenium import webdriver

def test_TC_WS_QW_ATH_002 () :
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ai-quizwhiz.zluck.com/login")

    # getting user name
    userNameBox = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    userNameBox.clear()
    userNameBox.send_keys("admin@gmail.com")

    # getting password
    passwordBox = driver.find_element("xpath", "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    passwordBox.clear()
    passwordBox.send_keys("fsfsfsfsdfsf")

    # click on remember me
    rememberMeBox = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[4]/div/div/div/label/input")
    rememberMeBox.click()

    # click on Sign On Button
    signInBtn = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    signInBtn.click()

    #driver.implicitly_wait(10)
    time.sleep(10)

    # invalid message showing
    invalidMsg = driver.find_element("xpath", "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/p")
    assert (invalidMsg.text == "These credentials do not match our records.")

    time.sleep(10)
