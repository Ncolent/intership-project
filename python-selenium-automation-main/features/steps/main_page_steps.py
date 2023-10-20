from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


@given('Open the main page')
def open_reely(context):
    context.app.reely_page.open_main()

@when ('Log in to the page')
def log_in(context):
    context.app.reely_page.log_in()

@when('Click on off plan at the left side menu.')
def click_off_plan(context):
    context.app.reely_page.click_off_plan()