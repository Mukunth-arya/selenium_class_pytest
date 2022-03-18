import pytest
from selenium import webdriver



@pytest.fixture(params = ["chrome"], scope= "class")
def init_driver(request):
   print("here comes the the sample testing")
   if request.param == "chrome":
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    web_driver = webdriver.Chrome(executable_path= "C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\testing_pytest\\chromedriver.exe",options=options )
    web_driver.implicitly_wait(10)
    web_driver.delete_all_cookies()
    request.cls.driver = web_driver
   else:
       print("please enter the proper driver details")
   yield
   web_driver.close()


@pytest.mark.usefixtures("init_driver")
class Basetest:
   pass
class Test_google_child(Basetest):
  def test_list_pytest(self):
     self.driver.get("https://www.google.com/")
     assert self.driver.title == "Google"

