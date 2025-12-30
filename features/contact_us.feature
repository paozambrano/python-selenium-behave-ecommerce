Feature: Contact Us Form
    As a user
    I want to contact the support team
    So that I can resolve my doubts

    Scenario: Submit contact us form successfully
        Given I am on the home page
        Then I verify that home page is visible
        When I click on "Contact Us" button
        Then I verify "GET IN TOUCH" is visible
        When I enter name "John", email "johndoe@test.com", subject "Support", and message "Hello Support"
        And I upload a file
        And I click "Submit" button
        And I accept the confirmation alert
        Then I verify success message "Success! Your details have been submitted successfully." is visible
        When I click the "Home" button
        Then I verify that I landed to home page successfully
