Feature: Target search test
  Scenario: User  can search for a coffee
    Given Open Target main page
    When Search for coffee
    Then Verify search results are shown for coffee
    Then Verify that URL has coffee

  Scenario: User can search for a tea
    Given Open Target main page