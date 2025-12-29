Feature: Login Functionality
    As a registered user
    I want to log in the AutomationExercise platform
    So that I can manage my account

    Background:
        Given I navigate to the login page

    Scenario: Successful login with valid credentials
        When I enter email "paozambranoo@outlook.com" and password "password123"
        Then I should see "Logged in as" on the navbar

    Scenario: Unsuccessful login with invalid credentials
        When I enter email "wrong@mail.com" and password "wrongpassword"
        Then I should see an error message