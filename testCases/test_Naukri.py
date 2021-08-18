from os import system
import random

from pageObjects.NaukriPage import NaukriLoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_UpdateHeadline():
    url = ReadConfig.getNaukriURL()
    username = ReadConfig.getNaukriUserName()
    password = ReadConfig.getNaukriPassword()

    log = LogGen.loggen()

    def test_Login_Naukri(self, setup):
        self.log.info("*******************Naukri Login test case started")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = NaukriLoginPage(self.driver)
        self.lp.Login_Naukri(username=self.username, password=self.password)
        act_title = self.driver.title
        if act_title == "Home | Mynaukri":
            self.log.info("*******************Naukri Login Successful**********")
            self.edit_text = "CDAC with 8+ years experience in Automation Testing using Selenium-Python,"
            self.edit_text = self.edit_text + "Automation Testing Framework, Pytest, PyCharm, Manual Testing, ALM, Jira,"
            self.edit_text = self.edit_text + "Test Plan, API Testing, selenium web driver, Agile, HP-UFT, GitHub,"
            self.edit_text = self.edit_text + "Jenkins, SAP-Sales,"
            self.keywords = ["QA", "Python", "Pytest", "SDET", "Postman", "Postman", "WebDriver", "BDD", "Banking",
                             "MySQL"]
            self.no = random.randint(0, 9)
            self.edit_text = self.edit_text + self.keywords[self.no]
            self.log.info("*******************Naukri Edit profile started**********")
            self.lp.Edit_Profile(self.edit_text)
            self.log.info("*******************Naukri profile edited successfully**********")
            self.lp.Logout_Naukri()
            self.log.info("*******************Naukri Logout Successful**********")
        else:
            self.log.info("*******************Naukri Login Failed**********")
            system(exit())
    """
    def test_Edit_Profile(self):
        self.lp1 = NaukriLoginPage(self.driver)
        self.lp1.Edit_Profile("test")
        #self.log.info("*******************Naukri profile edited successfully**********")

    def test_Logout_Naukri(self):
        self.lp = NaukriLoginPage(self.driver)
        self.lp.Logout_Naukri()
        self.log.info("*******************Naukri Logout Successful**********")
"""