from appium.webdriver.common.touch_action import TouchAction


def scroll_left(driver, y = 300,):
    driver.swipe(900, y, 300, y, 400)


def scroll_up(driver):
    action = TouchAction(driver)
    action.press(x=500, y=500).move_to(x=500, y=130).release().perform()


def scroll_down(driver):
    action = TouchAction(driver)
    action.press(x=500, y=500).move_to(x=500, y=-30).release().perform()
