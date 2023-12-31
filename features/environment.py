from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger


def browser_init(context,scenario_name):
    """
        :param context: Behave context
        """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                           desired_capabilities=chrome_options.to_capabilities())
    driver_path = ChromeDriverManager().install()
    mobile_emulation = {
    "deviceName": "iPhone 12 Pro"
}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    service = ChromeService(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)


    ### OTHER BROWSERS ###
    # driver_path = '/Users/jblai/Desktop/internship_project/python-selenium-automation-main/geckodriver.exe'
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)
    # # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    ## options = webdriver.ChromeOptions()
    ## options.add_argument('--headless')
    ## service = Service(driver_path)
    ## context.driver = webdriver.Chrome(
    ##     options=options,
    ##     service=service
    ## )


    # driver_path = ChromeDriverManager().install()
    # options = webdriver.ChromeOptions()
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1000,1000')
    # service = Service(driver_path)  # Please download the chromedriver and copy this driver file into your project folder.
    # context.driver = webdriver.Chrome(options=options, service=service)



    ### BROWSERSTACK ###
    ## Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'joshuablair_BJZ4IV'
    # bs_key = '6qd2zhkp41JUafehfEmA'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('/nStarted scenario: ', scenario.name)
    # Pass scenario.name to init() for browserstack config:
    logger.info(f'/nStarted scenario: , {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('/nStarted step: ', step)
    logger.info(f'Started step: , {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('/nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
