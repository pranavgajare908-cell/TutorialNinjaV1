from selenium.webdriver.common.by import By


class AccountRegisterPage():
    txt_FirstName = "firstname"
    txt_lastName = "lastname"
    txt_Email = "email"
    txt_telephone = "telephone"
    txt_Password = "password"
    txt_confirm_password = "confirm"  # ⚠ check correct locator
    chk_policy_name = "agree"
    btn_continue_xpath = "//input[@value='Continue']"
    txt_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.txt_FirstName).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.NAME, self.txt_lastName).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_Email).send_keys(email)

    def setTelephone(self, telephone):
        self.driver.find_element(By.NAME, self.txt_telephone).send_keys(telephone)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.txt_Password).send_keys(password)

    def setConfirmPassword(self, confirm_password):
        self.driver.find_element(By.NAME, self.txt_confirm_password).send_keys(confirm_password)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.chk_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()

    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_msg_conf_xpath).text
        except:
            return None
