from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import Paths




# Tests on author

driver.get(Paths.ROOT_PATH + Paths.GENERAL_FEATURE_PAGE_PATH)
driver.implicitly_wait(30)
site_search_element = driver.find_element_by_class_name('onsitesearch__searchbox')
print(driver.title)
driver.close()