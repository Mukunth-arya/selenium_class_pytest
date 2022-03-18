from selenium import  webdriver
import pytest
driver = None
@pytest.fixture(scope='module')
def init_driver():
     global driver
     options = webdriver.ChromeOptions()
     options.add_argument("start-maximized")
     driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\testing_pytest\\chromedriver.exe",options=options)
     #driver = webdriver.Chrome(executable_path= "/mnt/c/Users/mukunth/PycharmProjects/pythonProject/testing_pytest/chromedriver", options = options)
     driver.implicitly_wait(10)
     driver.delete_all_cookies()
     driver.get("https://stackoverflow.com/")
     yield
     driver.quit()
@pytest.mark.usefixtures("init_driver")
def test_first():
     assert driver.current_url == "https://stackoverflow.com/"
