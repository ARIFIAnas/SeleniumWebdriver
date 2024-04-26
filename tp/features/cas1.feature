Feature: cas de test 

As a visitor
I want to connect correctly in the website

Scenario: Connect with the account standard
    Given I am on sauce demo home page
    When I fill the "standard_user" and the "secret_sauce"
    Then I login my account & logout

Scenario: Connect with the account locked out
    Given I am on sauce demo home page
    When I fill the "locked_out_user" and the "secret_sauce"
    Then I verify the message error

Scenario: Navigate in the website
    Given I am on sauce demo home page
    When I fill the "standard_user" and the "secret_sauce"
    Then sort price from high to low
    And I add two first articles
    And I go check the cart
    And I add client informations
    And I finalize the order

