Feature: Product Review
    As a customer
    I want to leave a review on a product 
    So that I can share my feedback

    Scenario: Add review on product
        Given I am on the home page
        When I click "Products"
        Then I verify "ALL PRODUCTS" is visible
        When I click "View Product" of the first product
        Then I verify "WRITE YOUR REVIEW" is visible
        And I fill the review form with name "Pao", email "pao@test.com" and comment "Great product!"
        And I click "Submit Review"
        Then I verify "Thank you for your review." is visible
