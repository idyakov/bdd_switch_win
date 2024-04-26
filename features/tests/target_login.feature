Feature: Test Scenarios for Target switch pages availability from the Sign in page

  Scenario: User is able to open Privacy Policy
    Given Open Target main page
    And Target Signin button pressed
    And Target Signin button popup
    And Store original window
    And Click Terms and Cond link
    And Switch to new window
    Then Verify Terms and Cond page opened
    Given Close current page
    Then Return to original Target window

