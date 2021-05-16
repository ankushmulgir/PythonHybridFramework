# from selenium.webdriver.chrome import webdriver
import time

from selenium.webdriver.common.by import By

from selenium import webdriver


class Login:
    # txt_username = (By.ID, "Email")
    # txt_password = By.ID, "Password"
    # login_btn = By.XPATH, "input[@class='button-1 login-button']"
    txt_username = "Email"
    txt_password = "Password"
    login_btn = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def login_app(self, username, password):
        self.driver.find_element_by_id(self.txt_username).clear()
        self.driver.find_element_by_id(self.txt_username).send_keys(username)
        self.driver.find_element_by_id(self.txt_password).clear()
        self.driver.find_element_by_id(self.txt_password).send_keys(password)
        self.driver.find_element_by_xpath(self.login_btn).click()
        time.sleep(15)


    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
