#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ankit
#
# Created:     27/07/2017
# Copyright:   (c) ankit 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from selenium import webdriver

def main():
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")

if __name__ == '__main__':
    main()