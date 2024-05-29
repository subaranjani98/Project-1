
# This file consists of Test Information like username, password, XPATH etc

# Python Class for Username and Password
class TestData:
    username = "Admin"
    password = "admin123"
    password_1 = 'Invalid password'
    firstname = 'Suba'
    middle_name = 'Ranjani'
    last_name = 'S'
    employee_name = 'Suba Ranjani S'
    other_id = '1234'
    driver_lic_no = '199825Apr'
    licence_expiry_date = '2025-25-06'
    DOB = '1998-25-04'


# Python Class for Selenium Selectors
class TestSelectors:
    input_box_username = "username"

    input_box_password = "password"

    login_xpath = "//button[@type='submit']"

    pim_xpath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"

    add_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"

    input_box_first_name = "firstName"

    input_box_middle_name = "middleName"

    input_box_last_name = "lastName"

    save_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"

    search_employee_xpath = ('/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div['
                             '1]/div/div[2]/div/div/input')

    search_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"

    employee_edit_xpath = ("/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div["
                           "2]/div/div/div[9]/div/button[2]/i")

    other_id_xpath = ("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''2]/div[1]/div["
                      "2]/div/div[2]/input")

    driver_licence_no_xpath = ("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''2]/div["
                               "2]/div[1]/div/div[2]/input")

    licence_expiry_xpath = ("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''2]/div[2]/div["
                            "2]/div/div[2]/div/div/input")

    licence_input_xpath = ("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''2]/div[2]/div["
                           "2]/div/div[2]/div/div/input")

    nationality_icon_xpath = ("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''3]/div[1]/div["
                              "1]/div/div[2]/div/div/div[2]/i")

    nationality_select_xpath = ('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div['
                                '3]/div[1]/div[1]/div/div[2]/div/div[2]/div[83]/span')

    martial_status_1 = ("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''3]/div[1]/div["
                        "2]/div/div[2]/div/div/div[2]/i")

    martial_status_2 = ('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div['
                        '3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span')

    DOB_xpath_select = (
        "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''3]/div[2]/div[1]/div/div["
        "2]/div/div/input")

    DOB_input_xpath = ("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''3]/div[2]/div["
                       "1]/div/div[2]/div/div/input")

    gender_xpath = ("/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''3]/div[2]/div["
                    "2]/div/div[2]/div[1]/div[2]/div/label/span")

    save_button_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[''4]/button"

    delete_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[''2]/div/div/div[9]/div/button[1]/i"

    alert_xpath = "/html/body/div/div[3]/div/div/div/div[3]/button[2]/i"


