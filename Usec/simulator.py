from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

chrome_options = ChromeOptions()
chrome_options.add_extension('0.7.7_0.crx')
# chrome_options.add_extension('ghostery_insights.crx')

# driver = webdriver.Chrome('/home/ishan/Usec/chromedriver_linux64/chromedriver', options=chrome_options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://stackoverflow.com/')
# driver.get("chrome-extension://eafjgfjfiocmniplemahnlhgibaanhch/dist/insights/login.html")
# driver.get("chrome-extension://eafjgfjfiocmniplemahnlhgibaanhch/index.html")
# driver.get('chrome://extensions/')
input("Press Enter")

driver.quit()