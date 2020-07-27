class RolesPermissionPage:

    def __init__(self, driver):
        self.driver = driver
        self.roles_menu_xpath = "//a[@data-title='Roles & Permissions']"

    def click(self):
        self.driver.find_element_by_xpath(self.roles_menu_xpath).click()

