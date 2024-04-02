import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import Paths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import Expected


class SiteSearchGeneralFeature(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options)
        self.driver.get(Paths.ROOT_PATH + Paths.GENERAL_FEATURE_PAGE_PATH)

    # def test_site_search_general_feature(self):
    #     driver = self.driver
        # driver.get(Paths.ROOT_PATH + Paths.GENERAL_FEATURE_PAGE_PATH)
        # search_box = driver.find_element(By.CLASS_NAME, 'onsitesearch__searchboxbar__input')
        # search_box.send_keys("HBK")
        # search_box.send_keys(Keys.RETURN)
        # time.sleep(10)
        
    # def test_wrapper_hidden_field_value(self):
    #     driver = self.driver
    #     onsite_search_element = driver.find_element(By.CLASS_NAME, 'onsitesearch-container')
    #     print(onsite_search_element)
    #     for key,value in Expected.WRAPPER_HIDDEN_FIELD_SELECTOR_VALUE_MAP.items():
    #         self.assertEqual(driver.find_element(By.NAME, key).get_attribute('value'), value)
            
    def test_default_search_result(self):
        driver = self.driver
        try:
            result_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ais-InfiniteHits'))
            )
            # Test component texts
            self.check_component_text(driver)
        
            # Test component placeholders
            self.check_component_placeholder(driver)
                
            # Test component attributes
            self.check_component_attribute(driver)
                    
            self.check_hidden_field_value(driver)
            
            # Check Sort By values
            self.check_sort_by_value(driver)
            
            # Check Other Filters
            self.check_other_filter_values(driver)
            
            # Check default counter count
            self.assertEqual(driver.find_element(By.CSS_SELECTOR, 'div.onsitesearch__filterarea-sort__counter p span').get_attribute('textContent').strip(), '4380 Applied Items')
            
            # Check Result Items
            self.check_result_items(driver, Expected.BASIC_HIT_ITEMS)  
            
            # Indication Section
            self.check_indication_section(driver, 'Showing', '3', ' Of 4380 Results')
            
            # Switch Teaser View
            self.check_switch_view_action(driver)
            
            # Check Load More
            self.check_load_more_action(driver)
            
            # Switch to product tab
            self.check_tab_switch_action(driver, 'li#ProductsTab', Expected.PRODUCT_TAB_HIT_ITEMS)            
            
            # Switch to All Sections Tab
            self.check_tab_switch_action(driver, 'li#AllSectionsTab', Expected.BASIC_HIT_ITEMS)
            
            # Check Sorting Alphabetically
            self.check_sort_feature_action(driver, '', Expected.HIT_ALPHABETICAL_SORT)
         
            # Check Sorting Date
            self.check_sort_feature_action(driver, '3', Expected.HIT_DATE_SORT)
            
            # Return to default sort
            self.check_sort_feature_action(driver, '2', Expected.BASIC_HIT_ITEMS)
            
            # Check Search Action
            self.check_search_action(driver, Expected.SEARCH_AND_FILTER)
                  
            # Check on facets
            facet_items = driver.find_elements(By.CSS_SELECTOR, 'div.search-facet')
            for i in range(0, 3):
                facet_item = facet_items[i]
                facet_item_expected = Expected.FACET_SEARCH_CONFIG['search-facet'][i]
                self.assertEqual(facet_item.get_attribute('data-name').strip(), facet_item_expected['data-name'])
                driver.execute_script("arguments[0].click();", facet_item)
                facet_option_items = facet_item.find_elements(By.CSS_SELECTOR, 'div.simplebar-content label')
                self.assertEqual(len(facet_option_items), facet_item_expected['option_count'])
                facet_search_input_element = facet_item.find_element(By.CSS_SELECTOR, 'input')
                
                # Check for facet search
                for facet_search_key in range(0,3):
                    facet_search_input_element.send_keys(facet_item_expected['search_key_' + str(facet_search_key)])
                    time.sleep(2)
                facet_search_input_element.clear()  
                                  
                # Check for facet selected item
                for facet_item_check in range(0, len(facet_item_expected['select_item'])):
                    facet_option_check_item = facet_item.find_elements(By.CSS_SELECTOR, 'div.simplebar-content label')[facet_item_expected['select_item'][facet_item_check]]
                    driver.execute_script("arguments[0].click();", facet_option_check_item)
                    time.sleep(1)
                    
                    #check for selected result
                    result_after_refinement_selection = driver.find_elements(By.CSS_SELECTOR, 'li.ais-InfiniteHits-item')
                    self.assertTrue(len(result_after_refinement_selection) > 0)
                    
                    for result_key, result_value in facet_item_expected['select_item_results_'+str(facet_item_check)].items():
                        result_item = result_after_refinement_selection[result_key]
                        for selector, text in result_value.items():
                            self.assertTrue(result_item.find_element(By.CSS_SELECTOR, selector).get_attribute('textContent').startswith(text))
                            
                    selected_refinements_element = driver.find_element(By.CSS_SELECTOR, 'ul#current-refinements')
                    refinement_items = facet_item_expected['refinement_items_select_' + str(facet_item_check)]
                    time.sleep(1)
                    for refinement_item in refinement_items:
                        self.assertEqual(" ".join(selected_refinements_element.find_element(By.CSS_SELECTOR, 'li:nth-child(' + refinement_item['index'] + ') span').get_attribute('textContent').split()), refinement_item['label'])
                    time.sleep(1)
                    
                selected_refinements_element = driver.find_element(By.CSS_SELECTOR, 'ul#current-refinements')
                last_refinement_item = selected_refinements_element.find_element(By.CSS_SELECTOR, 'li:last-child')
                driver.execute_script("arguments[0].click();", last_refinement_item)
                time.sleep(5)
                      
        finally:
            pass

    def check_component_text(self, driver):
        for key, value in Expected.UI_CONFIGURATIONS_SELECTORS_TEXT.items():
            self.assertEqual(driver.find_element(By.CSS_SELECTOR, key).text, value)
            
    def check_component_placeholder(self, driver):
        for key, value in Expected.UI_CONFIGURATIONS_SELECTORS_PLACEHOLDER.items():
            self.assertEqual(driver.find_element(By.CSS_SELECTOR, key).get_attribute('placeholder'), value)
            
    def check_component_attribute(self, driver):
        for key, value in Expected.UI_CONFIGURATIONS_SELECTORS_ATTRIBUTE.items():
            for attribute, attribute_value in value.items():
                self.assertEqual(driver.find_element(By.CSS_SELECTOR, key).get_attribute(attribute), attribute_value)
                
    def check_hidden_field_value(self, driver):
        self.assertNotEqual(driver.find_element(By.CSS_SELECTOR, 'input#tags_list').get_attribute('value'), '')
        self.assertNotEqual(driver.find_element(By.CSS_SELECTOR, 'input#tags_map').get_attribute('value'), '')
        
    def check_sort_by_value(self, driver):
        #Check Filter items
        filter_items = driver.find_elements(By.CSS_SELECTOR, 'div.onsitesearch__filterarea-filters__option ul li')
        self.assertEqual(len(filter_items), 8)
        # Check filter values
        default_sort_by_element = filter_items[1].find_element(By.CSS_SELECTOR, 'div#sort-by')
        self.assertEqual(default_sort_by_element.get_attribute('data-relevancelabel'), 'Relevance')
        self.assertEqual(default_sort_by_element.get_attribute('data-alphabeticallabel'), 'Alphabetical')
        self.assertEqual(default_sort_by_element.get_attribute('data-timestamplabel'), 'Date')
        sort_by_menu_items = filter_items[1].find_elements(By.CSS_SELECTOR, 'div#sort-by label')
        for sort_item in sort_by_menu_items:
            value = sort_item.find_element(By.CSS_SELECTOR, 'input').get_attribute('value')
            label = sort_item.find_element(By.CSS_SELECTOR, 'span').get_attribute('textContent')
            self.assertTrue(label in ['Relevance', 'Alphabetical', 'Date'])
            self.assertTrue(value in ['hbkworld_dev/sort/hierarchy.lvl0:asc',
                                        'hbkworld_dev/sort/item_priority:desc',
                                        'hbkworld_dev/sort/timestamp:desc'])
            
    def check_other_filter_values(self, driver):
        filter_items = driver.find_elements(By.CSS_SELECTOR, 'div.onsitesearch__filterarea-filters__option ul li')
        for i in range(2, len(filter_items)):
            filter_item = filter_items[i]
            # Check wrapper attributes
            filter_item_attribute = filter_item.find_element(By.CSS_SELECTOR, 'div.search-facet')
            self.assertTrue(filter_item_attribute.get_attribute('data-name') in ["industry", "application", "services", "content-type", "language", "product"])
            self.assertTrue(filter_item_attribute.get_attribute('data-tagid') in ["hbkworld:industry", "hbkworld:application", "hbkworld:services", "hbkworld:content-type", "hbkworld:language", "hbkworld:product"])
            
            # Check for Non Empty Filter Items
            self.assertTrue(len(filter_item.find_elements(By.CSS_SELECTOR, 'label.dropdown-item__content')) > 0)
    
    def check_result_items(self, driver, EXPEXTEC_RESULT_ITEMS):
        result_items = driver.find_elements(By.CSS_SELECTOR, 'li.ais-InfiniteHits-item')
        for key, value in EXPEXTEC_RESULT_ITEMS.items():
            result_item = result_items[key]
            for selector, text in value.items():
                self.assertTrue(result_item.find_element(By.CSS_SELECTOR, selector).get_attribute('textContent').startswith(text))
    
    def check_indication_section(self, driver, initial, middle, final):
        indication_element = driver.find_elements(By.CSS_SELECTOR, 'div.loadmore__results span')
        self.assertEqual(indication_element[0].get_attribute('textContent').strip(), initial)
        self.assertEqual(indication_element[1].get_attribute('textContent').strip(), middle)
        self.assertEqual(indication_element[2].get_attribute('textContent'), final)
        
    def check_switch_view_action(self, driver):
        list_button_element = driver.find_element(By.CSS_SELECTOR, 'div.list-button')
        driver.execute_script("arguments[0].click();", list_button_element)
        self.assertTrue(list_button_element.get_attribute('class').find('active') > -1)
        time.sleep(1)
        grid_button_element = driver.find_element(By.CSS_SELECTOR, 'div.grid-button')
        driver.execute_script("arguments[0].click();", grid_button_element)
        self.assertTrue(grid_button_element.get_attribute('class').find('active') > -1)
        time.sleep(1)

    def check_load_more_action(self, driver):
        load_more_element = driver.find_element(By.CSS_SELECTOR, 'button.loadmore-button')
        driver.execute_script("arguments[0].click();", load_more_element)
        time.sleep(1)
        self.assertTrue(len(driver.find_elements(By.CSS_SELECTOR, 'li.ais-InfiniteHits-item')) == 6)
        self.assertEqual(driver.find_elements(By.CSS_SELECTOR, 'div.loadmore__results span')[1].get_attribute('textContent').strip(), '6')
    
    def check_tab_switch_action(self, driver, tabSelector, resultItem):
        tab_element = driver.find_element(By.CSS_SELECTOR, tabSelector)
        driver.execute_script("arguments[0].click();", tab_element)
        time.sleep(2)
        self.check_result_items(driver, resultItem)
    
    def check_sort_feature_action(self, driver, sortSelector, resultItem):
        sort_by_element = driver.find_element(By.CSS_SELECTOR, 'div.content-dropdown')
        driver.execute_script("arguments[0].click();", sort_by_element)
        time.sleep(1)
        sort_option_item = driver.find_element(By.CSS_SELECTOR, 'div.dropdown-item__container label') if sortSelector == '' else driver.find_element(By.CSS_SELECTOR, 'div.dropdown-item__container label:nth-child('+ sortSelector +')')
        driver.execute_script("arguments[0].click();", sort_option_item)
        driver.execute_script("arguments[0].click();", sort_by_element)
        time.sleep(1)
        
        # Check Product Alphabetical Sort Result Items
        self.check_result_items(driver, resultItem)
        
    def check_search_action(self, driver, search_keywords):
        for key, value in search_keywords.items():
                search_box = driver.find_element(By.CSS_SELECTOR, 'input.onsitesearch__searchboxbar__input')
                search_box.clear()
                search_box.send_keys(value['search_keyword'])
                search_box.send_keys(Keys.RETURN)
                time.sleep(2)
                # Check Result Items
                if value['search_keyword'] == 'Uganda':
                    self.assertEqual(len(driver.find_elements(By.CSS_SELECTOR, 'li.ais-InfiniteHits-item')), 0)
                    self.assertEqual(driver.find_element(By.CSS_SELECTOR, 'div.ais-InfiniteHits--empty p').get_attribute('textContent').strip(), 'No Search Result Found')
                    search_box.clear()
                    search_box.send_keys(Keys.RETURN)
                    continue
                self.check_result_items(driver, value['search_result'])
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()