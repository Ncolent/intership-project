from pages.base_page import Page
from pages.reelly_page import ReellyPage
from pages.off_plan_page import OffPlanPage

class Application:
    def __init__(self,driver):
        self.base_page = Page(driver)
        self.reelly_page = ReellyPage(driver)
        self.off_plan_page = OffPlanPage(driver)