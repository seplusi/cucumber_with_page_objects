Feature: Test feature

  Scenario: Test accepting the cookie
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "ToyotaCookiesPage" is loaded after some time
    And the text of element "accept_btn" is equal to "Accept"
    And the text of element "decline_btn" is equal to "Decline"
    And the text of element "title" is equal to "Welcome to Toyota!"
    And the text of element "content_txt" contains text "Our websites use cookies and similar tracking technologies"
    When I accept the cookie
    Then cookie banner is not displayed after some time
    And the cookie ".www.toyota.com" is found in the browser cookies

  Scenario: Test cookie when is declined
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "ToyotaCookiesPage" is loaded after some time
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
    And the page "ToyotaCookiesPage" is loaded after some time
    And the text of element "accept_btn" is equal to "Accept"
    And the text of element "decline_btn" is equal to "Decline"
    And the text of element "title" is equal to "Welcome to Toyota!"
    And the text of element "content_txt" contains text "Our websites use cookies and similar tracking technologies"
    And I accept the cookie
    And cookie banner is not displayed after some time
    And the cookie ".www.toyota.com" is found in the browser cookies

  Scenario: Test toyota home web page with full swipe
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "ToyotaCookiesPage" is loaded after some time
    When I accept the cookie
    Then the page "MobileToyotaHomePage" is loaded after some time
    And I safe click on the "play_btn" button
    And the text of element "heading_txt" matches the regex "^[0-9]{4}[a-zA-Z0-9\s]+$"
    And the text of element "subhead_txt" matches the regex "^[A-Z][a-zA-Z\s\.]+.$"
    And the text of element "learn_more" is equal to "Learn More"
    And the text of element "info_btn" is equal to "Info"
    And the text of element "al_vehi_txt" is equal to "Explore All Vehicles"
    And I perform a full swipe up

  Scenario: Test toyota home web page with scroll to element
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "ToyotaCookiesPage" is loaded after some time
    When I accept the cookie
    Then the page "MobileToyotaHomePage" is loaded after some time
    And I safe click on the "play_btn" button
    And I perform a swipe "up" with percentage "50.0" of total screen

  Scenario: Test toyota home web page after clicking hamburger icon
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "ToyotaCookiesPage" is loaded after some time
    And I accept the cookie
    And the page "MobileToyotaHomePage" is loaded after some time
    When I click on the "hamburger_btn" button
    Then the page "MobileToyotaHomePagewithHamburgerOptions" is loaded after some time
    And the text of element "vehic_btn" is equal to "Vehicles"
    And the text of element "shop_btn" is equal to "Shopping"
    And the text of element "owners_btn" is equal to "Owners"
    And the text of element "build_price_btn" is equal to "Build & Price"
    And the text of element "search_inv_btn" is equal to "Search Inventory"
    And the text of element "find_dealer_btn" is equal to "Find a Dealer"
    And the text of element "spc_offers_btn" is equal to "Special Offers"
    And the text of element "update_btn" is equal to "Update"
    And the element "zip_input_txt_box" has attribute "value" with value "95610"

  Scenario: Test toyota home web page after clicking hamburger icon and return home
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "ToyotaCookiesPage" is loaded after some time
    And I accept the cookie
    And the page "MobileToyotaHomePage" is loaded after some time
    And I click on the "hamburger_btn" button
    And the page "MobileToyotaHomePagewithHamburgerOptions" is loaded after some time
    When I click on the "close_btn" button
    Then the page "MobileToyotaHomePage" is loaded after some time

  @debug
  Scenario: Test toyota home web and search for gr corolla
    Given I open an android chrome web browser and go to "https://www.toyota.com/" url
    And I accept to open chrome browser without account 
    And I change the context to "chrome"
    And the page "ToyotaCookiesPage" is loaded after some time
    And I accept the cookie
    And the page "MobileToyotaHomePage" is loaded after some time
    And I click on the "hamburger_btn" button
    And the page "MobileToyotaHomePagewithHamburgerOptions" is loaded after some time
    And I click on the "zip_input_txt_box" button
    And I type text "95610" using the input element "zip_input_txt_box"
    And I hide the keypad
    And I click on the "update_btn" button
    And the element "zip_updated_msg" is displayed after some time
    When I click on the "search_inv_btn" button
    Then the page "MobileToyotaSearchInventoryPage" is loaded after some time
    And there are "12" elements on the "cars_minivan_model_tiles_lst" elements list after some time
