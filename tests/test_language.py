import unittest

from base_case import on_platforms
from base_case import browsers
from base_case import BaseCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
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
        logins = ["تسجيل الدخول", "Sign In", "Crear cuenta", "سائن ان کریں"]
        for i in range(len(languages)):
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "onLoginLanguage")))
            dropdown = Select(driver.find_element_by_id("onLoginLanguage"))
            old_button = driver.find_element_by_id("formButton")
            dropdown.select_by_value(languages[i])

            sleep(10)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "formButton")))   
            
            actual = driver.find_element_by_id('formButton').text
            expected = logins[i]
            self.assertEqual(actual, expected)
            


if __name__ == "__main__":
    unittest.main()
