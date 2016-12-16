import unittest

from base_case import on_platforms
from base_case import browsers
from base_case import BaseCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from time import time
@on_platforms(browsers)
class LanguageTest(BaseCase):

    def test_language(self):
        driver = self.driver
        
        # go to homepage
        driver.get("http://127.0.0.1:5981/apps/_design/bell/MyApp/index.html")
        # test all languages
        languages = ["Arabic", "English", "Spanish", "Urdu"]
       # logins = ["دخول", "Login", "Iniciar sesión", "لاگ ان"]

        logins = ["تسجيل الدخول", "Sign In", "Crear cuenta", "سائن ان کریں"]
        for i in range(len(languages)):
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "onLoginLanguage")))
            while True:
                try:
                    dropdown = Select(driver.find_element_by_id('onLoginLanguage'))
                    dropdown.select_by_value(languages[i])
                    break
                except StaleElementReferenceException:
                    print("Stale select")


            # wait for page reload 2 times
            WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.TAG_NAME, "html")))   
            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.TAG_NAME, "html")))   
            WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.TAG_NAME, "html")))   
            WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.TAG_NAME, "html")))               
            
            sleep(60)
            #WebDriverWait(driver, 30, 3).until(EC.visibility_of_element_located((By.ID, 'formButton')))   

            actual = ""
            
            while True:
                try:
                    actual = driver.find_element_by_xpath('//a[@id="formButton"]').text
                    break
                except StaleElementReferenceException:
                    print("Stale formButton")
                except NoSuchElementException:
                    print("No such Element")
                    sleep(1)
            
            expected = logins[i]
            self.assertEqual(actual, expected)
            


if __name__ == "__main__":
    unittest.main()
