# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time


class HHParser(unittest.TestCase):

    MAIN_URL = ''


    def setUp(self):

        profile = webdriver.FirefoxProfile()

        profile.set_preference('browser.download.folderList', 2) # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        #profile.set_preference('browser.download.dir', '/home/ysklyarov/Загрузки')
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')

        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)

        profile.set_preference("plugin.scan.Acrobat", "99.0")
        profile.set_preference("plugin.scan.plid.all", False)

        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://almaty.hh.kz/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver

        driver.get("https://almaty.hh.kz/")
        #driver.find_element_by_xpath("(//input[@name='username'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='username'])[2]").send_keys("ysklyarov@kopilka.kz")
        driver.find_element_by_xpath("(//input[@name='password'])[2]").click()
        #driver.find_element_by_xpath("(//input[@name='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys("1990666chtulhu")
        driver.find_element_by_name("action").click()

        # for elem in driver.find_elements_by_xpath("(//a[@itemprop='jobTitle'])"):
        #     file.write(elem.get_property('href'))
        #     file.flush()

        # for link in file.readlines():
        #     driver.get(link)
        #     driver.find_element_by_xpath("//button[2]").click()
        #     driver.find_element_by_link_text(".pdfAdobe Reader").click()
        #     time.sleep(10)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
