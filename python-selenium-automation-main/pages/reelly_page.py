from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ReellyPage(Page):
    EMAIL_FIELD = By.CSS_SELECTOR, '#email-2'
    PASSWORD_FIELD = By.CSS_SELECTOR, '#field'
    SIGN_IN_HEADER = By.CSS_SELECTOR, '.form-header'
    OFF_PLAN_BUTTON = By.CSS_SELECTOR, '.menu-twobutton'
    CONTINUE_BUTTON = By.CSS_SELECTOR, '.login-button.w-button'


    def open_main(self):
        self.driver.get('https://soft.reelly.io/')
        sleep(2)
        self.driver.refresh()

    def log_in(self):
        sleep(5)
        self.input_text('joshhbizz@gmail.com',*self.EMAIL_FIELD)
        self.input_text('Careerist2023!',*self.PASSWORD_FIELD)
        e = self.driver.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()


    def click_off_plan(self):
        e = self.driver.wait.until(EC.visibility_of_element_located(self.OFF_PLAN_BUTTON))
        e.click()