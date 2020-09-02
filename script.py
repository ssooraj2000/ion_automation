from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

website_link = "http://10.87.0.2"
username = "reg_no" #fill your registration number
password = "ion_password" #fill your ion password

username_field_id = "cpusername" #html id for the username text field
password_field_id = "cppassword" #html id for the password text fiele
submit_field_id = "btnLogin" #html id for the login button 

browser = webdriver.Chrome()	

browser.get((website_link))

if(browser.current_url != "http://10.87.0.2/status"): #checks if already logged in
    try:    
        username_text_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, username_field_id))
        )
        username_text_field.send_keys(username)
        password_text_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, password_field_id))
        )
        password_text_field.send_keys(password)
        LoginButton=browser.find_element_by_id(submit_field_id)
        LoginButton.click()
    
    finally:
        while(browser.current_url == "https://wifilogin.myion.in/?page=login"): #wait till the next page loads
            flag=1
        flag=0
        if(flag==0):
            browser.quit() #quit once the logged in page is shown
else:
    browser.quit() #quits browser if already logged into ion

    