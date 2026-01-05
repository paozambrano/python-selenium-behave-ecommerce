Feature: Product Details Verification 
    As a user
    I want to see the complete details of a Product
    So that I can make an informed purchase

    Scenario: Verify all product and product detail page
        Given I am on the home page
        And I verify that home page is visible
        When I navigate to the products page
        Then I verify user is navigated to "ALL PRODUCTS" page successfully
        And the products list is visible
        When I click on "View Product" of the first product
        Then I am landed to the product detail page
        And I verify that details are visible: name, category, price, availability, condition, brand
