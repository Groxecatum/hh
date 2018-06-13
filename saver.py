# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import common


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

        common.auth()

        file = open(common.FILENAME, "w")

        for link in file.readlines():
            driver.get(link)
            driver.find_element_by_xpath("//button[2]").click()
            driver.find_element_by_link_text(".pdfAdobe Reader").click()
            time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
