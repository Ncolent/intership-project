from pages.base_page import Page
from pages.reely_page import ReelyPage
from pages.off_plan_page import OffPlanPage

class Application:
    def __init__(self,driver):
        self.base_page = Page(driver)
        self.reely_page = ReelyPage(driver)
        self.off_plan_page = OffPlanPage(driver)