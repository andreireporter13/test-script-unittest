# New scraper idea for  QA Automation with Python;
#
# Author: Andrei C. Cojocaru
# Github: https://github.com/andreireporter13
# LinkedIn: https://www.linkedin.com/in/andrei-cojocaru-985932204/
# Twitter: https://twitter.com/andrei_reporter
# Website: https://ideisioferte.ro && https://webautomation.ro
# date_time - data la care este facut scriptul;
#
#
#
import unittest
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#
from selenium.webdriver.firefox.service import Service
#
from time import sleep
#
#
#
#------------------------ Test for 1_link -------------------------------------------
#


class StepikTest(unittest.TestCase):
    " This is my fisrt test for web aplication in python3! "

    
    # setUp driver for future tests;
    def setUp(self):
        
        # setup Firefox webdriver + options;
        options = webdriver.FirefoxOptions()
        options.headless = True # not open browser;
        firefox_service = Service(executable_path="/home/andy-1101/Documents/QA_Automation_tests/geckodriver")

        # set self.driver;
        self.driver = webdriver.Firefox(service=firefox_service, options=options)


    # first test for my fist link - http://suninjuly.github.io/registration1.html
    def test_first_link(self):
        
        self.driver.get('http://suninjuly.github.io/registration1.html')


        # from old form;
        input1 = self.driver.find_element(By.CLASS_NAME, "form-control.first").send_keys('And')
        input2 = self.driver.find_element(By.CLASS_NAME, "form-control.third").send_keys('Coo@gmail.com')
        input3 = self.driver.find_element(By.CLASS_NAME, "form-control.first").send_keys('+9855554455845')
        input3 = self.driver.find_element(By.CLASS_NAME, "form-control.second").send_keys('Google_Adress_13')

        # complete the online form;
        # first_name = self.driver.find_element(By.CLASS_NAME, 'form-control.first').send_keys('Cojocaru')
        # last_name = self.driver.find_element(By.CLASS_NAME, 'form-control.second').send_keys('Andrei')
        # email = self.driver.find_element(By.CLASS_NAME, 'form-control.third').send_keys('contact@ideisioferte.ro')
        # phone_number = self.driver.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.first_class input.form-control.first').send_keys('0722200099888')
        # adress = self.driver.find_element(By.CSS_SELECTOR, 'div.second_block div.form-group.second_class input.form-control.second').send_keys('Hacker_Land, nr. 3344')

        # press submit;
        button_submit = self.driver.find_element(By.CLASS_NAME, 'btn.btn-default').click()

        # set time for upload;
        sleep(1)

        # find welcome test;
        final_text = self.driver.find_element(By.TAG_NAME, 'h1').text

        # assertEqual for final_text, this is verification;
        self.assertEqual("Congratulations! You have successfully registered!", final_text)


    # second test test for my second link - http://suninjuly.github.io/registration2.html
    def test_second_link(self):
        
        self.driver.get('http://suninjuly.github.io/registration2.html')

        # from old form;
        input1 = self.driver.find_element(By.CLASS_NAME, "form-control.first").send_keys('And')
        input2 = self.driver.find_element(By.CLASS_NAME, "form-control.third").send_keys('Coo@gmail.com')
        input3 = self.driver.find_element(By.CLASS_NAME, "form-control.first").send_keys('+9855554455845')
        input3 = self.driver.find_element(By.CLASS_NAME, "form-control second").send_keys('Google_Adress_13')
        

        # # complete the form;
        # first_name = self.driver.find_element(By.CLASS_NAME, 'form-control.first').send_keys('Cojocaru')
        # email = self.driver.find_element(By.CLASS_NAME, 'form-control.third').send_keys('contact@ideisioferte.ro')
        # phone = self.driver.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.first_class input.form-control.first').send_keys('07222331232')
        # adress = self.driver.find_element(By.CSS_SELECTOR, 'div.second_block div.form-group.second_class input.form-control.second').send_keys('Hacker_land, nr.34455')

        button_submit = self.driver.find_element(By.CLASS_NAME, 'btn.btn-default').click()

        # time to sleep;
        sleep(1)

        final_text = self.driver.find_element(By.TAG_NAME, 'h1').text

        # assert for verification;
        self.assertEqual("Congratulations! You have successfully registered!", final_text)

        
    def tearDown(self):
        
        # exit from browser;
        self.driver.quit()


    if __name__ == "__main__":
        unittest.main()