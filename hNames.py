from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from time import sleep


# This script is made to take Hacker groups/names in 'zoneh.org' Adjust the URL and paths accordingly and
# how you find elements on the web page.
# Credits to zoneh.org for the published information

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"')

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True
capabilities['acceptInsecureCerts'] = True


# Set path to the driver exe and get URL
driver = webdriver.Chrome(executable_path=r'C:\Users\tviloria\OneDrive\Desktop\selenium\chromedriver.exe', chrome_options=options)

# Iterate through the web pages with respect to crawl-delay
for i in range(1, 2):
    driver.get('http://zone-h.org/archive/special=1/page={}?hz=1'.format(i))
    #driver.get('http://zone-h.org/archive/page={}'.format(i))

# Get the hacker groups, domain, and time of defacement
    titles_element = driver.find_elements_by_xpath('//*[@id="ldeface"]/tbody/tr[position()> 1 and position()<=(last() -2)]//td[position()> 1 and position()<=(last() -7)]//a')

    with open('test.txt', 'r+') as y:
        for x in titles_element:
            if x.text not in y:
                print(x.text, file=y)
            else:
                print('')

    sleep(10)


