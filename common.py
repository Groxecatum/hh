# -*- coding: utf-8 -*-

def auth(driver):
    driver.get("https://almaty.hh.kz/")
    #driver.find_element_by_xpath("(//input[@name='username'])[2]").clear()
    driver.find_element_by_xpath("(//input[@name='username'])[2]").send_keys("ysklyarov@kopilka.kz")
    driver.find_element_by_xpath("(//input[@name='password'])[2]").click()
    #driver.find_element_by_xpath("(//input[@name='password'])[2]").clear()
    driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys("1990666chtulhu")
    driver.find_element_by_name("action").click()