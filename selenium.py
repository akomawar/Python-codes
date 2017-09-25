from selenium import webdriver


#setup
browser = webdriver.Chrome()

##homepage
# browser.get('https://www.bmw-connecteddrive.fr/app/fr/index.html#/portal')
browser.get('https://www.bmw-connecteddrive.fr/app/fr/index.html#/portal/dashboard')
browser.implicitly_wait(20);

## login page
email= browser.find_element_by_id('inputEmail')
pwd= browser.find_element_by_id('inputPassword')
button= browser.find_element_by_xpath('//*[@id="maincontainer"]/form[1]/div[1]/button')
email.send_keys('CarolineBerkeley')
pwd.send_keys('eCalCharge+BMW')
button.click()


#main dashboard page
browser.implicitly_wait(20)
cockpit= browser.find_element_by_id('vehicle-chooser-remote-cockpit')
cockpit.click()

#Remote cockpit page
browser.implicitly_wait(20)
soc= browser.find_element_by_xpath('/html/body/div[3]/div[2]/cockpit-loader/cockpit/div/div/cockpit-status-loader/cockpit-status/div/vehicle-stage-container/vehicle-stage/div/bmwi-stage/div/div[2]/bmwi-charging-status-container/bmwi-charging-status/div/div[2]/div')

browser.implicitly_wait(10)

print(soc.text)

# browser.quit()




