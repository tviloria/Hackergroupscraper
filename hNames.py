from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from time import sleep

# This script is made to take Hacker groups/names in 'zoneh.org' Adjust the URL and paths accordingly and how you find elements on
# the web page.
# Credits to zoneh.org for the published information

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
#options.add_argument('--headless')

# Set path to the driver exe and get URL
driver = webdriver.Chrome(executable_path=r'C:/Users/tviloria/Desktop/selenium/chromedriver.exe', chrome_options=options)

# Iterate through the web pages with respect to crawl-delay
for i in range(1, 3):
    driver.get('http://zone-h.org/archive/special=1/page={}?hz=1'.format(i))
    #driver.get('http://zone-h.org/archive/page={}'.format(i))
# Get the hacker groups, domain, and time of defacement
    titles_element = driver.find_elements_by_xpath('//*[@id="ldeface"]/tbody/tr[position()> 1 and position()<=(last() -2)]//td[position()> 1 and position()<=(last() -7)]//a')
    titles = [x.text for x in titles_element]

# Prints in one column
    print('\n'.join(str(x) for x in titles))
    sleep(2)
