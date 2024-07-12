Feature: Add target product test

  Scenario: Adding product to cart Verification
    Given Open Target main page
    When Search for watermelon
    Then Adding watermelon in to cart
    Then Verify product is in the cart