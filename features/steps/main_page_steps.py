from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


@given('Open the main page')
def open_reelly(context):
    context.app.main_page.open_main()

@when ('Log in to the page')
def log_in(context):
    context.app.main_page.log_in()

@when('Click on off plan at the left side menu.')
def click_off_plan(context):
    context.app.main_page.click_off_plan()


@when('Click on off plan at the left side menu on a mobile device')
def click_off_plan(context):
    context.app.main_page.click_off_plan_mobile()

