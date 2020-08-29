"""
Programming assignment 1. 
Write down for loop to print to the console: “I snacked today” and then the name of the candy (In result you should have printed in the console 3 lines)
"""


#write here for loop

print("I snacked today")

candies=["Snickers", "Twist", "Bounty"]
for candy in candies:
    print("%s" % candy)




"""
Programming Assignment 2. Selenium WebDriver
Go to datafolks.com. 
Verify the text of all navigation buttons in the top right corner (Home, Portfolio, Services, Contact Us)
"""

from selenium import webdriver
driver=webdriver.Firefox(executable_path=r'C:\Users\elena\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe')
driver.get("https://www.datafolks.com")

#code for home button
home=driver.find_element_by_xpath('//div[@data-elem-id=1551634462374]/a')
assert home.text=="Home"

#code for portfolio button
portfolio=driver.find_element_by_xpath('//div[@data-elem-id=1551634481382]/a')
assert portfolio.text=="Portfolio"

#code for services button
services=driver.find_element_by_xpath('//div[@data-elem-id=1551634484712]/a')
assert services.text=="Services"

#code for Contact Us button
contact_us=driver.find_element_by_xpath('//div[@data-elem-id=1551634487768]/a')
assert contact_us.text=="Contact Us"

driver.quit()