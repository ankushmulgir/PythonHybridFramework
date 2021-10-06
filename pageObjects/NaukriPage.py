import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

# this is naukir page login and update profile
class NaukriLoginPage:
    link_lgoin = "login_Layer"
    txt_naukri_user = "//input[@placeholder='Enter your active Email ID / Username']"
    txt_naukri_pwd = "//input[@placeholder='Enter your password']"
    btn_naukri_Login = "//button[text()='Login']"

    link_my_naukri = "//a//div[text()='My Naukri']"
    link_logout = "//a[text()='Logout']"
    link_edit_profile = "//a[text()='Edit Profile']"
    icon_edit_headline = "//div[@class='resumeHeadline']//span[text()='Edit']"
    txt_resume_headline = "//textarea[@class='resumeHeadlineTxt materialize-textarea']"
    btn_save_resume_headline = "//form[@name='resumeHeadlineForm']//button[text()='Save']"


    def __init__(self, driver):
        self.driver = driver

    def Login_Naukri(self, username, password):
        self.driver.find_element_by_id(self.link_lgoin).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.txt_naukri_user).send_keys(username)
        self.driver.find_element_by_xpath(self.txt_naukri_pwd).send_keys(password)
        self.driver.find_element_by_xpath(self.btn_naukri_Login).click()
        time.sleep(10)

    def Logout_Naukri(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element_by_xpath(self.link_my_naukri)
        a.move_to_element(m).perform()
        self.driver.find_element_by_xpath(self.link_logout).click()
        time.sleep(5)
        self.driver.quit()

    def Edit_Profile(self, text_to_edit):
        a = ActionChains(self.driver)
        m = self.driver.find_element_by_xpath(self.link_my_naukri)
        a.move_to_element(m).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.link_edit_profile).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.icon_edit_headline).click()
        time.sleep(10)
        #strtext = self.driver.find_element_by_xpath(self.txt_resume_headline).text()
        #print(strtext)
        self.driver.find_element_by_xpath(self.txt_resume_headline).clear()
        self.driver.find_element_by_xpath(self.txt_resume_headline).send_keys(text_to_edit)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btn_save_resume_headline).click()
        time.sleep(30)

        #commit




