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

# 1er scenario , je teste la présence des elements dans ma page
@scenario('features/contact_form.feature',"Verify the presence of the input field")

def test_input_field_presence(): #tjr ajouter test dans la fonction pour indiquer a pytest qu'il y a un test 
    pass #les etapes reelles du test seront exécutées par les implementations d'etapes ci-dessous

@given('I am on the contact page')
def open_contact_page(browser):
    browser.get("C:/Users/Administrateur/Desktop/Python/selenium/siteTest/contact.html")

@then('I should see the "nom_user" input field "text"')
def see_input_field(browser):
    try:
        assert browser.find_element(By.ID,"nom_user").is_displayed()
        print(f"Succès:Le champ [nom_user] est bien visible et a le type texte")
    except AssertionError :
         print(f"Erreur: Le champ [nom_user] n'a pas été trouvé ")

@then(parsers.parse('I should see the "{field_name}" input field "{field_type}"'))
def see_input_field(browser,field_name,field_type):
    # try:
        assert browser.find_element(By.NAME,field_name).is_displayed()
        assert browser.find_element(By.NAME,field_name).get_attribute('type') == field_type
    #     browser.save_screenshot(f"{field_name}.png")
    #     print(f"Succès:Le champs [{field_name}] est bien visible et a le type texte{field_type}")
    # except AssertionError:
    #      print(f"Erreur: Le champs [{field_name}] n'a pas été trouvé ")

@scenario('features/contact_form.feature',"Verify input field is disabled")

def test_input_field_disabled():
    pass

@then('I should see the "nom_user" is disabled')
def see_input_field_disabled(browser):
    assert not browser.find_element(By.NAME ,"nom_user").is_enabled()

@then('I should see the "prenom_user" is enabled')
def see_input_field_enabled(browser):
    assert browser.find_element(By.NAME ,"prenom_user").is_enabled()

@scenario('features/contact_form.feature','Verify label text')

def test_label_text():
    pass

@then('I should see the "nom_user" label is equal to "Votre nom"')
def verify_label_text(browser):
    assert browser.find_element(By.XPATH, '//*[@id="monFormulaire"]/label[1]').text == 'Votre nom :'


@scenario('features/contact_form.feature','Write in a field')

def test_write_text():
    pass

@then('I can write "Hello World !!" in the field "message"')
def write_text(browser):
    browser.find_element(By.ID,"message").send_keys('Hello World !!')
    #time.sleep(10)



@scenario('features/contact_form.feature',"I can change page")

def test_change_page():
    pass
@given('I am on the index page')
def open_page(browser):
    browser.get("C:/Users/Administrateur/Desktop/Python/selenium/siteTest/index.html")
    #time.sleep(5)

@when('I click on the contact link')
def click_elem(browser):
    browser.find_element(By.XPATH,'/html/body/footer/div/ul/li/a[2]').click()
    # footerlinks = browser.find_elements(By.CSS_SELECTOR, "body > footer > div > ul > li > a")
    # assert len(footerlinks) == 2 
    # footerlinks[1].click()
    #time.sleep(5)

@then('I am redirected on the contact page')
def redirected_page(browser):
    browser.get("C:/Users/Administrateur/Desktop/Python/selenium/siteTest/contact.html")
    assert browser.find_element(By.CSS_SELECTOR,'body > main > h3')
    assert browser.find_element(By.CSS_SELECTOR,'body > main > h2')
    #time.sleep(5)


@scenario('features/contact_form.feature',"Compare values on two pages")

def test_compare_values():
    pass

@given('I am on the index page with a value to compare')
def open_page_with_value(browser):
    global valuesToCompare
    browser.get("C:/Users/Administrateur/Desktop/Python/selenium/siteTest/index.html")
    valuesToCompare = browser.find_element(By.TAG_NAME,'h2').text
    time.sleep(5)

@then('the values to compare are equals')
def values_to_compare(browser):
    secondValue = browser.find_element(By.TAG_NAME,'h2').text
    assert secondValue == valuesToCompare 

@scenario('./features/contact_form.feature', "I can select a fruit")
def test_select_fruit():
    pass
@then('I can select mango in the fruits dropdown')
def select_from_dropdown(browser):
    fruitsSelection = Select(browser.find_element(By.ID, 'fruits'))
    fruitsSelection.select_by_value('mango')
    time.sleep(10)
