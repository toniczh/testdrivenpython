from selenium import webdriver
import unittest
import time
class NewVistorTest(unittest.TestCase):
    def setUp(self):
        chrome_path = "c:\\chromedriver\\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_path)
    def tearDown(self):
        self.driver.quit()
    def test_start_a_list_retrieve_it_later(self):
        self.driver.get("http://localhost:8000")
        time.sleep(3)
        self.assertIn("Django", self.driver.title)
        
if __name__ == "__main__":
    unittest.main(warnings='ignore')