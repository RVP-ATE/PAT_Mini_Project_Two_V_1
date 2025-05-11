"""
This file contains all the data used
"""  # Module-level docstring explaining the purpose of the file


class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"  # Base URL of the application under test
    expected_title = "OrangeHRM"  # Expected page title for verification
    expected_url_after_login = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"  # URL expected after successful login
    expected_url_after_logout = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"  # URL expected after logging out

