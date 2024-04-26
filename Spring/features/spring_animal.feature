Feature: Spring animal management  

As a visitor
I want to create a new users and add animals for them 

Scenario: Add first user
    Given I am on the homepage of petclinic
    When I go to page find owners
    And I add a new user
    Then the user details are displayed on the users list
    And the user details are disaplyed on the users details
 
