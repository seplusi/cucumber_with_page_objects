Feature: Test feature
 
  Scenario: Scenario name test1
    Given I sleep "1" seconds
    And I store current timestamp in storage key "timest"
    Then the value in storage with key "timest" is higher then valule in storage with key "initial_ts"

  Scenario: Open a chrome browser
    Given I open a chrome web browser and go to "https://www.toyota.com/" url
    And the page "ToyotaCookiesPage" is loaded after some time
    When I accept the cookie
    Then cookie banner is not displayed after some time

  Scenario: Test cookie content and acceptance
    Given I open a chrome web browser and go to "https://www.toyota.com/" url
    And the page "ToyotaCookiesPage" is loaded after some time
    And the text of element "accept_btn" is equal to "Accept"
    And the text of element "decline_btn" is equal to "Decline"
    And the text of element "title" is equal to "Welcome to Toyota!"
    And the text of element "content_txt" contains text "Our websites use cookies and similar tracking technologies"
    When I accept the cookie
    Then cookie banner is not displayed after some time
    And the cookie ".www.toyota.com" is found in the browser cookies

  Scenario: Test cookie when is declined
    Given I open a chrome web browser and go to "https://www.toyota.com/" url
    And the page "ToyotaCookiesPage" is loaded after some time
    And the text of element "accept_btn" is equal to "Accept"
    And the text of element "decline_btn" is equal to "Decline"
    And the text of element "title" is equal to "Welcome to Toyota!"
    And the text of element "content_txt" contains text "Our websites use cookies and similar tracking technologies"
    When I click on the "decline_btn" button
    Then cookie banner is not displayed after some time
    And I close webdriver
    And I open a chrome web browser and go to "https://www.toyota.com/" url
    And the page "ToyotaCookiesPage" is loaded after some time
    And the text of element "accept_btn" is equal to "Accept"
    And the text of element "decline_btn" is equal to "Decline"
    And the text of element "title" is equal to "Welcome to Toyota!"
    And the text of element "content_txt" contains text "Our websites use cookies and similar tracking technologies"
    And I accept the cookie
    And cookie banner is not displayed after some time
    And the cookie ".www.toyota.com" is found in the browser cookies

  Scenario: Test toyota home web page
    Given I open a chrome web browser and go to "https://www.toyota.com/" url
    And the page "ToyotaCookiesPage" is loaded after some time
    When I accept the cookie
    Then the page "ToyotaHomePage" is loaded after some time
    And the text of element "vehicles_btn" is equal to "Vehicles"
    And the text of element "shopping_btn" is equal to "Shopping"
    And the text of element "owners_btn" is equal to "Owners"
    And the text of element "expl_all_vehi_txt" is equal to "Explore All Vehicles"
    And there are "5" elements on the "expl_all_vehi_lst" elements list after some time
    And the elements list "expl_all_vehi_lst" contains the following texts in this order
      | content           |
      | Cars & Minivan    |
      | Trucks            |
      | Crossovers & SUVs |
      | Electrified       |
      | Upcoming Vehicles |

  Scenario: Test toyota vehicles web page
    Given I open a chrome web browser and go to "https://www.toyota.com/" url
    And the page "ToyotaCookiesPage" is loaded after some time
    And I accept the cookie
    And the page "ToyotaHomePage" is loaded after some time
    When I click on the "vehicles_btn" button
    Then the page "ToyotaVehiclesPage" is loaded after "120" seconds
    And the text of element "vehicles_btn" is equal to "Vehicles"
    And the text of element "shopping_btn" is equal to "Shopping"
    And the text of element "owners_btn" is equal to "Owners"
    And the text of element "cross_and_minivans_btn" is equal to "Crossovers & SUVs"
    And the text of element "cars_and_minivans_btn" is equal to "Cars & Minivan"
    And the text of element "trucks_btn" is equal to "Trucks"
    And the text of element "electrified_btn" is equal to "Electrified"
    And the text of element "upcom_vehi_btn" is equal to "Upcoming Vehicles"
    And the text of element "gazoo_rcn_btn" is equal to "Gazoo Racing"
    And the text of element "trd_pro_btn" is equal to "TRD Pro"
    And the text of element "view_all_vehi_btn" is equal to "View All Vehicles"
    And the text of element "cert_used_vehi_btn" is equal to "Toyota Certified Used Vehicles"
    And there are "15" elements on the "cross_suvs_lst" elements list after some time
    And each car slide has the correct info after moving the mouse to it
    | name                    | hybrid            |
    | Corolla Cross           |                   |
    | Corolla Cross Hybrid    | Hybrid EV         |
    | RAV4                    |                   |
    | RAV4 Hybrid             | Hybrid EV         |
    | RAV4 Plug-in Hybrid     | Plug-in Hybrid EV |
    | bZ                      | Battery EV        |
    | Highlander              |                   |
    | Highlander Hybrid       | Hybrid EV         |
    | Grand Highlander        |                   |
    | Grand Highlander Hybrid | Hybrid EV         |
    | 4Runner                 |                   |
    | 4Runner i-FORCE MAX     | Hybrid EV         |
    | Toyota Crown Signia     | Hybrid EV         |
    | Land Cruiser            | Hybrid EV         |
    | Sequoia                 | Hybrid EV         |

  Scenario: Test toyota shopping web page
    Given I open a chrome web browser and go to "https://www.toyota.com/" url
    And the page "ToyotaCookiesPage" is loaded after some time
    And I accept the cookie
    And the page "ToyotaHomePage" is loaded after some time
    When I click on the "shopping_btn" button
    Then the page "ToyotaShoppingPage" is loaded after "120" seconds
    And the text of element "vehicles_btn" is equal to "Vehicles"
    And the text of element "shopping_btn" is equal to "Shopping"
    And the text of element "owners_btn" is equal to "Owners"
    And the text of element "find_yr_vehicle_txt" is equal to "Find Your Vehicle"
    And the text of element "toy_cert_used_veh" is equal to "Toyota Certified Used Vehicles"
    And the text of element "accessories" is equal to "Accessories"
    And the text of element "comp_vehi" is equal to "Compare Vehicles"
    And the text of element "buy_parts_access" is equal to "Buy Parts & Accessories"
    And the text of element "shop_online_w_spath" is equal to "Shop Online With SmartPath"
    And the text of element "view_broch" is equal to "View Brochures"
    And there are "4" elements on the "shopping_slides" elements list after some time
    And each shopping car slide has the correct info after moving the mouse to it
    | name             |
    | Build & Price    |
    | Find a Dealer    |
    | Search Inventory |
    | Special Offers   |
