Feature: Test that Target cart is empty

  Scenario: Verifies that “Your cart is empty” message is shown
    Given Open target.com
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: Test logged out user can Sign In
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened