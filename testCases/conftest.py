import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser='chrome'):
    if browser == 'chrome':
        driverpath = "C:\\Users\\amq5708\\Desktop\\Py\\HybridFramework\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driverpath)
        driver.maximize_window()
        print("Launching chrome browser.........")
        return driver
    else:
        print("browser not available for run")
        assert False




def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


