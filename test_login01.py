import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import data
import pytest
from webdriver_manager.firefox import GeckoDriverManager


class TestOrangeHRM:
    url = "https://opensource-demo.orangehrmlive.com"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    # TC_Login_01
    def test_data_01(self, booting_function):
        self.driver.get(self.url)

        # Enter username
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_username))
        )
        username_input.send_keys(data.TestData.username)

        # Enter password
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_password))
        )
        password_input.send_keys(data.TestData.password)

        # Clicking login button
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.login_xpath))
        )
        login_button.click()

        # Excepted result
        print("The user is logged in successfully.")

    # TC_Login_02
    def test_data_02(self, booting_function):
        self.driver.get(self.url)

        # Enter username
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_username))
        )
        username_input.send_keys(data.TestData.username)

        # Enter invalid password
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_password))
        )
        password_input.send_keys(data.TestData.password_1)

        # Clicking login button
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.login_xpath))
        )
        login_button.click()

        # Excepted result:
        print("A valid error message for invalid credential is displayed.")

    # TC_PIM_01 :
    def test_data_03(self, booting_function):

        self.driver.get(self.url)

        # Enter username
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_username))
        )
        username_input.send_keys(data.TestData.username)

        # Enter password
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_password))
        )
        password_input.send_keys(data.TestData.password)

        # Clicking login button
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.login_xpath))
        )
        login_button.click()

        # Go to the PIM module from the left pan in the webpage
        PIM_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.pim_xpath))
        )
        PIM_input.click()

        # CLICKING ON ADD BUTTON:
        Add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.add_xpath))
        )
        Add_button.click()

        # # Filling ---> Add new employee details in the webpage:
        # FILLING FIRST NAME:
        First_name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_first_name))
        )
        First_name_input.send_keys(data.TestData.firstname)

        # FILLING MIDDLE NAME:
        Middle_name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_middle_name))
        )
        Middle_name_input.send_keys(data.TestData.middle_name)

        # FILLING LAST NAME:
        Last_name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_last_name))
        )
        Last_name_input.send_keys(data.TestData.last_name)

        # Clicking Save ---> Saving Employee details by clicking save button
        Save_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.save_xpath))
        )
        Save_button.click()
        time.sleep(5)
        # Excepted Result:
        print('successful employee addition.')

        # *** As per (3Q) FILL IN ALL PERSONAL DETAILS OF THE EMPLOYEE AND CLICK SAVE -> the condition does not (
        # satisfied) updated detailed information  to the mentor

        # **

    # TC_PIM_02

    def test_data_04(self, booting_function):
        self.driver.get(self.url)

        # Enter username
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_username))
        )
        username_input.send_keys(data.TestData.username)

        # Enter password
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_password))
        )
        password_input.send_keys(data.TestData.password)

        # Clicking login button
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.login_xpath))
        )
        login_button.click()

        # Go to the PIM module from the left pan in the webpage
        PIM_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.pim_xpath))
        )
        PIM_input.click()

        # Searching employee name:
        searching_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.search_employee_xpath))
        )
        searching_input.send_keys(data.TestData.employee_name)

        # # clicking search button:
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.search_xpath))
        )
        search_button.click()

        # Clicking employee edit button in record found:
        employee_edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.employee_edit_xpath))
        )
        employee_edit_button.click()

        # Editing personal details of the employee:

        # other(ID):
        other_id_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.other_id_xpath))
        )
        other_id_input.send_keys(data.TestData.other_id)

        # Driver's License Number:
        driver_licence_number_id_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.driver_licence_no_xpath))
        )
        driver_licence_number_id_input.send_keys(data.TestData.driver_lic_no)

        # License Expiry Date:
        licence_expiry = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.licence_expiry_xpath))
        )
        licence_expiry.click()

        # filling Licence expiry data
        licence_expiry_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.licence_input_xpath))
        )
        licence_expiry_input.send_keys(data.TestData.licence_expiry_date)

        # Nationality:
        nationality_dropdown_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.nationality_icon_xpath))
        )
        nationality_dropdown_icon.click()

        # Selecting nationality:
        nationality_select = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.nationality_select_xpath))
        )
        nationality_select.click()

        # Marital Status:
        martial_l1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.martial_status_1))
        )
        martial_l1.click()

        martial_l2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.martial_status_2))
        )
        martial_l2.click()

        # Date of Birth:
        DOB_select = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.DOB_xpath_select))
        )
        DOB_select.click()
        # Filling DOB
        DOB_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.DOB_input_xpath))
        )
        DOB_input.send_keys(data.TestData.DOB)

        # Gender:
        Gender = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.gender_xpath))
        )
        Gender.click()

        # Save button:
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data.TestSelectors.save_button_xpath))
        )
        save_button.click()

        print('successful employee details addition.')

        # TC_PIM_03:
        def test_data_05(self, booting_function):
            self.driver.get(self.url)

            # Enter username
            username_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_username))
            )
            username_input.send_keys(data.TestData.username)

            # Enter password
            password_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, data.TestSelectors.input_box_password))
            )
            password_input.send_keys(data.TestData.password)

            # Clicking login button
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, data.TestSelectors.login_xpath))
            )
            login_button.click()

            # Go to the PIM module from the left pan in the webpage
            PIM_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, data.TestSelectors.pim_xpath))
            )
            PIM_input.click()

            # Searching employee name:
            searching_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, data.TestSelectors.search_employee_xpath))
            )
            searching_input.send_keys(data.TestData.employee_name)

            # # clicking search button:
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, data.TestSelectors.search_xpath))
            )
            search_button.click()

            # CLICKING DELETE BUTTON IN RECORDS FOUND OF EMPLOYEE:
            delete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, data.TestSelectors.delete_xpath))
            )
            delete_button.click()

            # CLICKING ALERT -> YES DELETE BUTTON:
            clicking_alert = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, data.TestSelectors.alert_xpath))
            )
            clicking_alert.click()

            # Expected result:
            print('Employee deleted successfully')





