from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from support.logger import logger

class OffPlanPage(Page):
    OFF_PLAN_TITLE = By.CSS_SELECTOR,'div.page-title'
    FILTER_BUTTON = By.CSS_SELECTOR, '.filter-button.w-inline-block'
    LAST_UNITS_BUTTON = By.CSS_SELECTOR, '[wized$="LastUnits"][w-el-class$="8"]'
    PAGE_ITEMS = By.CSS_SELECTOR, '[class="project-card w-inline-block"]'
    CURRENT_SELECTION = By.CSS_SELECTOR, '._5-comission'
    TEXT = By.XPATH, '//*[@wized="projectStatus"]'
    def filter_by_last_units(self):
        logger.info('Filtering by Last Units')
        self.click_filter_button()
        self.driver.wait.until(EC.element_to_be_clickable(self.LAST_UNITS_BUTTON)).click()
    def filter_by_last_units_mobile(self):
        logger.info('Filtering by Last Units')
        self.click_filter_button_mobile()
        self.driver.wait.until(EC.element_to_be_clickable(self.LAST_UNITS_BUTTON)).click()

    def verify_each_item_last_unit(self):
        self.verify_text('Last units',*self.TEXT)

        # all_products = self.driver.find_elements(*self.PAGE_ITEMS)
        # print(all_products).text()
        # expected_tags = ['Last Units', 'Last Units', 'Last Units'
        #                  'Last Units', 'Last Units', 'Last Units'
        #                  'Last Units', 'Last Units', 'Last Units'
        #                  'Last Units', 'Last Units', 'Last Units'
        #                  'Last Units', 'Last Units', 'Last Units'
        #                  'Last Units', 'Last Units', 'Last Units'
        #                  'Last Units', 'Last Units', 'Last Units'
        #                  'Last Units', 'Last Units', 'Last Units']
        # actual_tags = []
        #
        # tags = self.driver.find_elements(*self.PAGE_ITEMS)
        # self.driver.wait.until(EC.presence_of_all_elements_located(self.PAGE_ITEMS))
        # print(tags)
        # print(len(tags))
        # #
        # for tag in tags[:24]:
        #     current_tag = self.driver.find_element(*self.CURRENT_SELECTION).text
        #
        #     print(current_tag)
        #     actual_tags.append(current_tag)
        #
        # print(actual_tags)
        #
        # assert actual_tags == expected_tags
        # expected_text = 'Last units'
        # len_of_elements = len(self.driver.find_elements(*self.PAGE_ITEMS))
        # print(len_of_elements)
        #
        # actual_text = self.driver.find_element(*self.TEXT)#.text
        # print(actual_text)

        # for i in range(len_of_elements):
        #
        #     assert expected_text == actual_text



    def verify_off_plan(self):
        p = self.driver.find_element(*self.OFF_PLAN_TITLE).text[:30]
        self.verify_text(p, *self.OFF_PLAN_TITLE[:30])



