from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

wait_time = 10


def wait_and_click(driver, value, type='xpath'):
    wait = WebDriverWait(driver, wait_time)
    if type == 'xpath':
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, value))).click()
    elif type == 'class':
        wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, value))).click()
    elif type == 'id':
        wait.until(expected_conditions.element_to_be_clickable((By.ID, value))).click()


def wait_and_send_keys(driver, value, type, text_input):
    wait = WebDriverWait(driver, wait_time)
    if type == 'xpath':
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, value))).send_keys(text_input)
    elif type == 'class':
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, value))).send_keys(text_input)
    elif type == 'id':
        wait.until(expected_conditions.visibility_of_element_located((By.ID, value))).send_keys(text_input)


def text_is_present_and_clickable(driver, class_name, var_text, click):
    wait = WebDriverWait(driver, wait_time)
    text_xpath = "//{0}[@text='{1}']".format(class_name, var_text)
    try:
        driver.find_element_by_xpath(text_xpath)
        if click is True:
            print text_xpath
            assert wait.until(expected_conditions.element_to_be_clickable((By.XPATH, text_xpath))).is_enabled() is True
        return True
    except:
        return False


def keyboard_hide(driver):
    try:
        driver.hide_keyboard()
    except:
        pass
