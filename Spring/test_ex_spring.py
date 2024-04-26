import pytest
import pytest_bdd
import time
from pytest_bdd import parsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pytest_bdd import scenario, given , then , when 

firstName = ""
lastName = ""
address = ""
city = ""
telephone = ""
@pytest.fixture
def browser():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@scenario('features/spring_animal.feature',"Add first user")
def test_add_user():
    pass

@given('I am on the homepage of petclinic')
def open_clinic_page(browser) : 
    browser.get("https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/")
    time.sleep(3)

@when('I go to page find owners')
def find_owners(browser):
    browser.find_element(By.XPATH,'/html/body/nav/div/button').click()
    browser.find_element(By.XPATH,'//*[@id="main-navbar"]/ul/li[2]/a').click()
    assert browser.current_url == "https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/owners/find"
    time.sleep(4)

@when('I add a new user')
def owners_page(browser):
    browser.find_element(By.CSS_SELECTOR,'body > div > div > a').click()
    assert browser.current_url == "https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/owners/new"
    browser.find_element(By.ID,"firstName").send_keys('Cristiano')
    browser.find_element(By.ID,"lastName").send_keys('RONALDO')
    browser.find_element(By.ID,"address").send_keys('Al Halilah, 7073 2303')
    browser.find_element(By.ID,"city").send_keys('Riyadh')
    browser.find_element(By.ID,"telephone").send_keys('0206010305')
    browser.find_element(By.XPATH,'//*[@id="add-owner-form"]/div[2]/div/button').click()
    assert browser.find_element(By.XPATH,'/html/body/div/div/table[1]').is_displayed()
    browser.find_element(By.CSS_SELECTOR,'body > nav > div > a').click()
    time.sleep
    global firstName,lastName,address,city,telephone 
    firstName = 'Cristiano'
    lastName = 'RONALDO'
    address = 'Al Halilah, 7073 2303'
    city = 'Riyadh'
    telephone = '0206010305'

    time.sleep(5)

@then('the user details are displayed on the users list')
def display_user(browser):
    browser.find_element(By.XPATH,'/html/body/nav/div/button').click()
    browser.find_element(By.XPATH,'//*[@id="main-navbar"]/ul/li[2]/a').click()
    time.sleep(5)
    assert browser.current_url == "https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/owners/find"
    browser.find_element(By.ID,"lastName").send_keys('RONALDO')
    browser.find_element(By.XPATH,'//*[@id="search-owner-form"]/div[2]/div/button').click()
    time.sleep(5)
    assert browser.current_url == "https://spring-framework-petclinic-qctjpkmzuq-od.a.run.app/owners?lastName=RONALDO"
    # browser.find_element(By.LINK_TEXT,"Cristiano RONALDO").click()
    Name = browser.find_element(By.XPATH,'//*[@id="ownersTable"]/tbody/tr[1]/td[1]/a').text
    Address = browser.find_element(By.XPATH,'//*[@id="ownersTable"]/tbody/tr[1]/td[2]').text
    City = browser.find_element(By.XPATH,'//*[@id="ownersTable"]/tbody/tr[1]/td[3]').text
    Telephone = browser.find_element(By.XPATH,'//*[@id="ownersTable"]/tbody/tr[1]/td[4]').text

    assert Name == firstName + ' ' + lastName
    assert Address == address
    assert City == city
    assert Telephone == telephone
    
    time.sleep(5)

@then('the user details are disaplyed on the users details')
def user_details(browser):

    browser.find_element(By.LINK_TEXT,"Cristiano RONALDO").click()
    Name = browser.find_element(By.CSS_SELECTOR,'body > div > div > table:nth-child(2) > tbody > tr:nth-child(1) > td').text
    Address = browser.find_element(By.XPATH,'body > div > div > table:nth-child(2) > tbody > tr:nth-child(2) > td').text
    City = browser.find_element(By.XPATH,'body > div > div > table:nth-child(2) > tbody > tr:nth-child(3) > td').text
    Telephone = browser.find_element(By.XPATH,'body > div > div > table:nth-child(2) > tbody > tr:nth-child(4) > td').text

    assert Name == firstName + ' ' + lastName
    assert Address == address
    assert City == city
    assert Telephone == telephone

    time.sleep(5)
    











