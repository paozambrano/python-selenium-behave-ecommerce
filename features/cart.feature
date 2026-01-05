Feature: Cart Management
    As a user
    I want to add products to my cart 
    So that I can purchase them later

    Scenario: Add two products to cart and verify details
        Given I am on the home page
        When I navigate to the products page 
        And I add the first product to the cart 
        And I click "Continue Shopping"
        And I add the second product to the cart
        And I click "View Cart"
        Then I verify both products are in the cart
        And I verify prices, quantities, and total prices