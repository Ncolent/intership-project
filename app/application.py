from pages.base_page import Page
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage

# $behave -f allure_behave.formatter:AllureFormatter -o%allure_result_folder% ./features
class Application:
    def __init__(self,driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlanPage(driver)

    # $ behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/