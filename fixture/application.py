from appium import webdriver
import os


class Application:

    def __init__(self):

        capabilities = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': 'Nexus 5X API 22',
            'app': os.getcwd() + "/application/travel-mate.apk"
            
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(10)


