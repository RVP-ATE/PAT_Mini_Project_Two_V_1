"""
This file contains all the web locators like xpath, id, tag name, link text etc.,
"""  # Docstring describing the purpose of this file


class Locators:

    # admin page

        # Locators for User Role selection dropdown
        user_role = "(//*[@class='oxd-select-text--after'])[1]" #ByXpath
        user_select = "//*[@class = 'oxd-select-text-input' and text() = '-- Select --']" #ByXpath
        user_admin = "//*[@class = 'oxd-select-text-input' and text() = 'Admin']" #ByXpath
        user_dropdown = "//*[@class='oxd-userdropdown-tab']" #ByXpath
        logout = "//a[text()='Logout']" #ByXpath

        # Locators for Status dropdown
        status = "(//*[@class='oxd-select-text--after'])[2]" #ByXpath
        status_select = "//*[@class = 'oxd-select-text-input' and text() = '-- Select --']" #ByXpath
        status_enabled = "//*[@class = 'oxd-select-text-input' and text() = 'Enabled']" #ByXpath

        # Locators for input fields
        employee_name = '//input[@placeholder="Type for hints..."]' #ByXpath
        username_field = "(//*[@class='oxd-input oxd-input--active'])[2]" #ByXpath
        password_field = "(//*[@type='password'])[1]" #ByXpath
        confirm_password_field = "(//*[@type='password'])[2]" #ByXpath
        save_button = "//button[normalize-space()='Save']" #ByXpath


    # dashboard page

        Admin =   "//span[text()='Admin']" #ByXpath
        PIM =  "//span[text()='PIM']" #ByXpath
        Leave =  "//span[text()='Leave']" #ByXpath
        Time = "//span[text()='Time']" #ByXpath
        Recruitment =  "//span[text()='Recruitment']" #ByXpath
        MyInfo = "//span[text()='My Info']" #ByXpath
        Performance =  "//span[text()='Performance']" #ByXpath
        Dashboard =  "//span[text()='Dashboard']" #ByXpath
        add_user_button = "//button[normalize-space()='Add']" #ByXpath


    # home page/login page

        username_input = "username" #ByName
        password_input = "password" #ByName
        login_btn = "//button[@type='submit']" #ByXpath







