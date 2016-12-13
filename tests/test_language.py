import unittest

from base_case import on_platforms
from base_case import browsers
from base_case import BaseCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

@on_platforms(browsers)
class LanguageTest(BaseCase):

    def test_language(self):
        driver = self.driver
        
        # go to homepage
        driver.get("http://127.0.0.1:5981/apps/_design/bell/MyApp/index.html")
        # test all languages
        languages = ["Arabic", "English", "Spanish", "Urdu"]
        logins = ["دخول", "Login", "Iniciar sesión", "لاگ ان"]
        for i in range(len(languages)):
            dropdown = Select(driver.find_element_by_id("onLoginLanguage"))
            dropdown.select_by_value(str(languages[i]))
            
           # sleep(10)
            waitdr = WebDriverWait(driver, 20)
            #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "c50_login")))   
            waitdr.until(EC.invisibility_of_element_located((By.ID, "c50_login")))
            waitdr.until(EC.element_to_be_clickable((By.ID, "c50_login")))   

            actual = driver.find_element_by_xpath('//label[@for="c50_login"]').text
            expected = logins[i]
            self.assertEqual(actual, expected)
            


if __name__ == "__main__":
    unittest.main()