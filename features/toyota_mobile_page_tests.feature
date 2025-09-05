Feature: Test feature

  Scenario: Test accepting the cookie
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "MobileToyotaCookiesPage" is loaded after some time
    And the text of element "accept_btn" is equal to "Accept"
    And the text of element "decline_btn" is equal to "Decline"
    And the text of element "title" is equal to "Welcome to Toyota!"
    And the text of element "content_txt" contains text "Our websites use cookies and similar tracking technologies"
    When I accept the cookie
    Then cookie banner is not displayed after some time
    And the cookie ".www.toyota.com" is found in the browser cookies

  @debug
  Scenario: Test cookie when is declined
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "MobileToyotaCookiesPage" is loaded after some time
    And the text of element "accept_btn" is equal to "Accept"
    And the text of element "decline_btn" is equal to "Decline"
    And the text of element "title" is equal to "Welcome to Toyota!"
    And the text of element "content_txt" contains text "Our websites use cookies and similar tracking technologies"
    When I click on the "decline_btn" button
    Then cookie banner is not displayed after some time
    And I close webdriver
    And I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account
    And I change the context to "chrome"
    And the page "MobileToyotaCookiesPage" is loaded after some time
    And the text of element "accept_btn" is equal to "Accept"
    And the text of element "decline_btn" is equal to "Decline"
    And the text of element "title" is equal to "Welcome to Toyota!"
    And the text of element "content_txt" contains text "Our websites use cookies and similar tracking technologies"
    And I accept the cookie
    And cookie banner is not displayed after some time
    And the cookie ".www.toyota.com" is found in the browser cookies