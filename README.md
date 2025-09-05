# cucumber_with_page_objects

# Where mobile chromedriver is downloaded and stored. Whenever we open a chrome browser in de mobile devide, this chormedriver is downloaded to the mobile devide and installed to interact with the mobile chrome driver.
$HOME/.appium/node_modules/appium-uiautomator2-driver/node_modules/appium-chromedriver/chromedriver/linux

# How to download older versions of chromedriver for android. For example, version v139
1) Use this link to find the full version of v139
https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json

2) We're going to fetch the last version fo 139 using the pervious link (139.0.7258.154)
https://storage.googleapis.com/chrome-for-testing-public/139.0.7258.154/linux64/chromedriver-linux64.zip

3) Unzip the zip file and place the chromedriver bin under $HOME/.appium/node_modules/appium-uiautomator2-driver/node_modules/appium-chromedriver/chromedriver/linux

4) Go to the previous folder and test chromedriver version
cd $HOME/.appium/node_modules/appium-uiautomator2-driver/node_modules/appium-chromedriver/chromedriver/linux
./chromedriver --version
ChromeDriver 139.0.7258.154 (9e0d6b2b47ffb17007b713429c9a302f9e43847f-refs/branch-heads/7258@{#2926})

5) Downloading the desired chromedriver to be used against android allows us not to use the appium option "--allow-insecure chromedriver_autodownload". This option is not possible in appium-server 3.0
Move from:
appium --base-path /wd/hub --allow-insecure chromedriver_autodownload
To:
appium --base-path /wd/hub


# INFO: This works for appium-server 3.0. Check doc in "https://appium.io/docs/en/3.0/guides/security/". It will download the necessary android chrome driver under the above folder.
appium --base-path /wd/hub --relaxed-security