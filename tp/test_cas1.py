import pytest
import pytest_bdd
import time
from pytest_bdd import parsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pytest_bdd import scenario, given , then , when 

@pytest.fixture
def browser():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

Article1 = ""
Article2 = ""
@scenario('features/cas1.feature',"Connect with the account standard")

def test_add_user():
    pass

@given('I am on sauce demo home page')
def open_saucedemo(browser) : 
    browser.get("https://www.saucedemo.com/")
    time.sleep(3)

# @when('I fill the username and the password')
@when(parsers.parse('I fill the "{username}" and the "{password}"'))
def user_info(browser,username,password):
    browser.find_element(By.ID,'user-name').send_keys(username)
    browser.find_element(By.ID,'password').send_keys(password)
    browser.find_element(By.ID,'login-button').click()

@then('I login my account & logout')
def login_user(browser):
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    time.sleep(4)
    browser.find_element(By.ID,'react-burger-menu-btn').click()
    time.sleep(2)
    browser.find_element(By.ID,'logout_sidebar_link').click()
    time.sleep(2)
    assert browser.current_url == "https://www.saucedemo.com/"



@scenario('features/cas1.feature',"Connect with the account locked out")

def test_locked_out_user():
    pass

# @when('I fill the username and the password for locked out user')
# def locked_out_user(browser):
#     assert browser.current_url == "https://www.saucedemo.com/"
#     browser.find_element(By.ID,'user-name').send_keys('locked_out_user')
#     browser.find_element(By.ID,'password').send_keys('secret_sauce')
#     browser.find_element(By.ID,'login-button').click()
#     time.sleep(10)

@then('I verify the message error')
def verify_error(browser):
    if browser.find_elements(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3'):
        print("Element found")
    else:
        print("Element not found")
    # assert browser.find_element(By.CSS_SELECTOR,'#login_button_container > div > form > div.error-message-container.error > h3')
    #time.sleep(5)

@scenario('features/cas1.feature',"Navigate in the website")
def test_price():
    pass

@then('sort price from high to low')
def cheapest_article(browser):
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    articlesSelection = Select(browser.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select'))
    articlesSelection.select_by_value('hilo')
    time.sleep(10)

@then('I add two first articles')
def first_article(browser):
    browser.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    time.sleep(5)
    browser.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(5)
    global Article1 , Article2
    Article1 = browser.find_element(By.CSS_SELECTOR,'#item_4_title_link > div').text
    Article2 = browser.find_element(By.CSS_SELECTOR,'#item_5_title_link > div').text 

@then('I go check the cart')
def go_to_cart(browser):
    browser.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
    time.sleep(5)
    assert browser.current_url == "https://www.saucedemo.com/cart.html"

    Article1toverify = browser.find_element(By.CSS_SELECTOR,'#item_5_title_link > div').text
    Article2Toverify = browser.find_element(By.CSS_SELECTOR,'#item_4_title_link > div').text

    assert Article1 == Article2Toverify
    assert Article2 == Article1toverify
    
@then('I add client informations')
def add_info(browser):
    browser.find_element(By.XPATH,'//*[@id="checkout"]').click()
    assert browser.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    time.sleep(2)
    browser.find_element(By.ID,'first-name').send_keys('Cristiano')
    browser.find_element(By.ID,'last-name').send_keys('RONALDO')
    browser.find_element(By.ID,'postal-code').send_keys('20000')
    browser.find_elementt(By.XPATH,'//*[@id="continue"]').click()

@then('I add client informations')
def end_order(browser):
    browser.find_element(By.ID,'finish').click()
    assert browser.current_url == "https://www.saucedemo.com/checkout-complete.html"
    time.sleep(2)



