import time
from random import randint
from config import app
from helpers.appium_helper import *
from helpers.selenium_helper import *

# -------------------------------------------- ELements ------------------------------------------------------ #

name_field = "tie.hackathon.travelguide:id/input_name_signup"
phone_field = "tie.hackathon.travelguide:id/input_num_signup"
phone_field_login = "tie.hackathon.travelguide:id/input_num_login"
password_field = "tie.hackathon.travelguide:id/input_pass_signup"
password_field_login = "tie.hackathon.travelguide:id/input_pass_login"
sign_up_button = "tie.hackathon.travelguide:id/ok_signup"
login_button = "tie.hackathon.travelguide:id/ok_login"
sign_up_link = "tie.hackathon.travelguide:id/signup"
login_link = "tie.hackathon.travelguide:id/login"
progress_bar = "android:id/progress"
switcher = "android.widget.ImageButton"
text_view = "android.widget.TextView"
nav_list_view = "android.widget.CheckedTextView"
sign_out = "//android.widget.CheckedTextView[@text='Sign Out']"
travel = "//android.widget.CheckedTextView[@text='Travel']"


# -------------------------------------------- Test Cases ------------------------------------------------------ #
# Check whether signup works on passing valid credentials


class TestCases:

    def test_sign_up(self, app):
        driver = app.driver
        wait_and_send_keys(driver, name_field, 'id', "Vaishakh")
        wait_and_send_keys(driver, phone_field, 'id', "9000" + str(randint(1000, 9999)))
        wait_and_send_keys(driver, password_field, 'id', "qwert12345")
        keyboard_hide(driver)
        wait_and_click(driver, sign_up_button, 'id')
        time.sleep(10)
        assert text_is_present_and_clickable(driver, text_view, "Most Popular Cities", False) is True

# Check whether login works

    def test_login(self, app):
        driver = app.driver
        wait_and_click(driver, login_link, 'id')
        wait_and_send_keys(driver, phone_field_login, 'id', "9009009009")
        wait_and_send_keys(driver, password_field_login, 'id', "qwert12345")
        wait_and_click(driver, login_button, 'id')
        assert text_is_present_and_clickable(driver, text_view, "Most Popular Cities", False) is True

# Check whether invalid creds are accepted

    def test_invalid_signup(self, app):
        driver = app.driver
        wait_and_send_keys(driver, name_field, 'id', "Vaishakh")
        wait_and_send_keys(driver, password_field, 'id', "qwert12345")
        keyboard_hide(driver)
        wait_and_click(driver, sign_up_button, 'id')
        time.sleep(10)
        assert text_is_present_and_clickable(driver, text_view, "Please wait...", False) is False
        assert text_is_present_and_clickable(driver, text_view, "Most Popular Cities", False) is False

# Check whether all the cities are present and clickable

    def test_cities_present(self, app):
        driver = app.driver
        self.test_sign_up(app)
        city_names = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Agra', 'Ahmedabad']
        try:
            for i in range(0, len(city_names)):
                assert text_is_present_and_clickable(driver, text_view, city_names[i], False) is True
        except:
            raise Exception('Assertion Failed')

# Check whether all the menu items are present and clickable

    def test_nav_list(self, app):
        driver = app.driver
        self.test_sign_up(app)
        city_names = ['Destinations', 'Travel', 'Utilities', 'Change Source/Destination', 'Emergency Contacts',
                      'Sign Out']
        wait_and_click(driver, switcher, 'class')
        try:
            for i in range(0, len(city_names)):
                assert text_is_present_and_clickable(driver, nav_list_view, city_names[i], True) is True
        except:
            raise Exception('Assertion Failed')

# Check whether each city contains all the city details and those items are clickable

    def test_city_detail(self, app):
        driver = app.driver
        self.test_login(app)
        city_names = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Agra', 'Ahmedabad']
        city_detail = ['Fun Facts', 'Hangout', 'Monuments', 'Shopping', 'Restaurants',
                       'City Trends']
        try:
            for i in range(0, len(city_names)):
                city_xpath = "//{0}[@text='{1}']".format(text_view, city_names[i])
                scroll_down(driver)
                wait_and_click(driver, city_xpath, 'xpath')
                print city_names[i]
                assert text_is_present_and_clickable(driver, text_view, city_names[i], True) is True
                try:
                    for j in range(0, len(city_detail)):
                        scroll_down(driver)
                        assert text_is_present_and_clickable(driver, text_view, city_detail[j],
                                                             True) is True
                except:
                    raise Exception('Assertion Failed')
                driver.back()
        except:
            raise Exception('Assertion Failed')

# Check whether login with credentials used for signup works

    def test_login_after_signup(self, app):
        driver = app.driver
        phone_num = "9000" + str(randint(1000, 9999))
        wait_and_send_keys(driver, name_field, 'id', "Vaishakh")
        wait_and_send_keys(driver, phone_field, 'id', phone_num)
        wait_and_send_keys(driver, password_field, 'id', "qwert12345")
        keyboard_hide(driver)
        wait_and_click(driver, sign_up_button, 'id')
        time.sleep(10)
        assert text_is_present_and_clickable(driver, text_view, "Most Popular Cities", False) is True
        wait_and_click(driver, switcher, 'class')
        wait_and_click(driver, sign_out, 'xpath')
        wait_and_click(driver, login_link, 'id')
        wait_and_send_keys(driver, phone_field_login, 'id', phone_num)
        wait_and_send_keys(driver, password_field_login, 'id', "qwert12345")
        wait_and_click(driver, login_button, 'id')
        assert text_is_present_and_clickable(driver, text_view, "Most Popular Cities", False) is True


# Check whether signing up a new account with existing credentials throw error

    def test_signup_with_existing_credentials(self, app):
        driver = app.driver
        phone_num = "9000" + str(randint(1000, 9999))
        wait_and_send_keys(driver, name_field, 'id', "Vaishakh")
        wait_and_send_keys(driver, phone_field, 'id', phone_num)
        wait_and_send_keys(driver, password_field, 'id', "qwert12345")
        keyboard_hide(driver)
        wait_and_click(driver, sign_up_button, 'id')
        time.sleep(10)
        assert text_is_present_and_clickable(driver, text_view, "Most Popular Cities", False) is True
        wait_and_click(driver, switcher, 'class')
        wait_and_click(driver, sign_out, 'xpath')
        wait_and_click(driver, sign_up_link, 'id')
        wait_and_send_keys(driver, name_field, 'id', "Vaishakh")
        wait_and_send_keys(driver, phone_field, 'id', phone_num)
        wait_and_send_keys(driver, password_field, 'id', "qwert12345")
        keyboard_hide(driver)
        wait_and_click(driver, sign_up_button, 'id')
        time.sleep(10)
        assert text_is_present_and_clickable(driver, text_view, "Please wait...", False) is False


# Check the items in Travel section

    def test_travel_items(self, app):
        driver = app.driver
        self.test_login(app)
        wait_and_click(driver, switcher, 'class')
        wait_and_click(driver, travel, 'xpath')
        travel_items = ['MY TRIPS', 'TRANSPORT', 'HOTEL BOOKING', 'ONLINE SHOPPING', 'REAL TIME LOCATOR']
        try:
            for i in range(0, len(travel_items)):
                city_xpath = "//{0}[@text='{1}']".format(text_view, travel_items[i])
                scroll_down(driver)
                assert text_is_present_and_clickable(driver, text_view, travel_items[i], True) is True
        except:
            raise Exception('Assertion Failed')
