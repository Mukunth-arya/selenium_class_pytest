from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("init_driver")
class Test1:
    pass
class Test2(Test1):
    @pytest.mark.parametrize("name,passw", [("mukunthnataraj@gmail.com", "jbjbfbvhfhvb")])
    def test3(self, name,passw):
        self.driver.get("https://hub.docker.com/")
        self.driver.find_element(By.CSS_SELECTOR, "div#log_in" ).click()
        data1 = self.driver.find_element(By.NAME, "username")
        data1.send_keys(name)
        self.driver.find_element(By.NAME, "action").click()
        data2 = self.driver.find_element(By.NAME, "password")
        data2.send_keys(passw)







