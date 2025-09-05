Feature: Test feature

  Scenario: Open a mobile chrome browser
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "MobileToyotaCookiesPage" is loaded after some time
    When I accept the cookie
    Then cookie banner is not displayed after some time