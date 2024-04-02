import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import Expected
import Paths


class ListComponentAllConfig(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options)
        self.driver.get(Paths.ROOT_PATH + Paths.GENERAL_FEATURE_PAGE_PATH)

    def test_list_component_all_config(self):
        driver = self.driver
        try:
            result_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'cmp-list__items'))
            ) 
            time.sleep(2)
            self.check_content_count(driver, 3, 4)
            self.check_list_content(driver, Expected.INITIAL_LIST_CONTENTS)
            self.check_result_number_text(driver, 'Showing', '3', 'of', '7', 'items')
            self.check_load_more_button(driver)
                     
        finally:
            pass
        
    # Method to check Content Count
    def check_content_count(self, driver, showCount, hiddenCount):
        list_teaser_all_items = driver.find_elements(By.CSS_SELECTOR, 'li.cmp-list__item')
        self.assertEqual(len(list_teaser_all_items), showCount + hiddenCount)
        result_show_count = 0
        result_hidden_count = 0
        for item in list_teaser_all_items:
            if 'hbk-hidden' in item.get_attribute('class'):
                result_hidden_count += 1
            else:
                result_show_count += 1
        self.assertEqual(showCount, result_show_count)
        self.assertEqual(hiddenCount, result_hidden_count)
    
    # Method to check Content
    def check_list_content(self, driver, expected_contents):
        list_teaser_all_items = driver.find_elements(By.CSS_SELECTOR, 'li.cmp-list__item')
        for i in range(len(expected_contents)):
            current_element = list_teaser_all_items[i]
            current_expected = expected_contents[i]
            for key, value in current_expected.items():
                current_element.find_element(By.CSS_SELECTOR, key).text == value            
    
    # Method to check Result number Text
    def check_result_number_text(self, driver, initial_text, initial_count, conjunction_text, total_count, end_text):
        result_number = driver.find_elements(By.CSS_SELECTOR, 'div.cmp-list__results span')
        self.assertEqual(result_number[0].get_attribute('textContent').strip(), initial_text)
        self.assertEqual(result_number[1].get_attribute('textContent').strip(), initial_count)
        self.assertEqual(result_number[2].get_attribute('textContent').strip(), conjunction_text)
        self.assertEqual(result_number[3].get_attribute('textContent').strip(), total_count)  
        self.assertEqual(result_number[4].get_attribute('textContent').strip(), end_text)  
        
    # Method to check Load More Action
    def check_load_more_button(self, driver):
        load_more_button = driver.find_element(By.CSS_SELECTOR, 'button.cmp-button')
        driver.execute_script("arguments[0].click()", load_more_button)
        time.sleep(3)
        self.check_content_count(driver, 6, 1)
        load_more_button.click()
        time.sleep(3)
        self.check_content_count(driver, 7, 0)
    
     
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()