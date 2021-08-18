import pytest
#from selenium import webdriver

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login():
    # url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username = "admin@yourstore.com"
    # password1 = "admin"

    url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password1 = ReadConfig.getPassword()

    log = LogGen.loggen()

    #@pytest.mark.sanity
    def test_verifylogin(self, setup):
        self.log.info("*******************Verify Login test case started")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Login(self.driver)
        self.lp.login_app(self.username, self.password1)
        act_title = self.driver.title
        self.driver.save_screenshot(".\\Screenshots\\homepagetitle.png")
        print(act_title)
        self.driver.close()
        self.log.info("*******************Verify Login test case ended")

    #@pytest.mark.regression
    def test_verifylogin2(self, setup):
        self.log.info("*******************Verify Login test case started_____2")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Login(self.driver)
        self.lp.login_app(self.username, self.password1)
        act_title = self.driver.title
        self.driver.save_screenshot(".\\Screenshots\\homepagetitle.png")
        print(act_title)
        self.driver.close()
        self.log.info("*******************Verify Login test case ended")
