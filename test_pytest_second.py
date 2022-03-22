import pytest


@pytest.mark.usefixtures("init_driver")
class Basetest:
   pass
class Test_google_child(Basetest):
  def test_list_pytest(self):
     self.driver.get("https://www.google.com/")
     assert self.driver.title == "Google"

