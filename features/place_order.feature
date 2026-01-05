Feature: Place Order
    As a customer
    I want to register during checkout
    So that I can complete my purchase

    Scenario: Register while checkout and place order 
        Given I am on the home page
        And I add the first product to the cart
        And I click "View Cart"
        Then I verify that cart page is displayed
        When I click "Proceed To Checkout"
        And I click "Register/Login"
        And I fill signup name "Pao" and email "pao.test123@mail.com"
        And I complete the full registration form
        Then I verify "ACCOUNT CREATED!" is visible
        And I click "Continue" button
        And I verify "Logged in as Pao" is visible
        When I click "Proceed To Checkout"
        Then I verify address details and review order
        When I enter comment "Order for testing! and click "Place Order"
        And I enter payment details "Pao Z", "123456789", "311", "12", "2027"
        Then I verify success message "Your order has been placed successfully!"
        When I click "Delete Account"
        Then I verify "ACCOUNT DELETED!" is visible