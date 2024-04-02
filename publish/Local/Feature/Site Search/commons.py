import Expected
from selenium.webdriver.common.by import By
def checkWrapperHiddenFieldValue(driver):
    for key,value in Expected.WRAPPER_HIDDEN_FIELD_SELECTOR_VALUE_MAP.items():
        assert driver.find_element(By.NAME, key).get_attribute('value') == value , "Value for " + key + " is not as expected"
