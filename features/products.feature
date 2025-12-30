Feature: Product Management
    As a user
    I want to interact with the products catalog
    So that I can find items I want to purcharse

    Scenario: Search for a specific product
        Given I am on the home page
        When I navigate to the product page
        And I search for "Blue Top"
        Then I should see "SEARCHED PRODUCTS" as the title
        And I should see results for the search