# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import time
import common
import random


FILENAME = '1st.txt'
START_WITH = 1
TRESHOLD = 450

class HHParser(unittest.TestCase):

    def setUp(self):

        profile = webdriver.FirefoxProfile()

        profile.set_preference('browser.download.folderList', 2) # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        #profile.set_preference('browser.download.dir', '/home/ysklyarov/Загрузки')
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf;application/msword;application/rtf')

        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)

        profile.set_preference("plugin.scan.Acrobat", "99.0")
        profile.set_preference("plugin.scan.plid.all", False)

        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://almaty.kz/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_save(self):
        driver = self.driver

        common.auth(driver)

        file = open(FILENAME, "r")

        i = 0
        for link in file.readlines():
            i += 1
            link = link.strip("\n")
            if link.find("Page ") < 0 and i >= START_WITH and i < TRESHOLD + START_WITH:
                driver.get(link)
                print "Saving " + link
                time.sleep(random.randint(1, 2))
                driver.find_element_by_xpath("//button[2]").click()
                time.sleep(random.randint(1, 2))
                driver.find_element_by_link_text(".pdfAdobe Reader").click()
                time.sleep(random.randint(1, 2))
                driver.find_element_by_link_text(".docMicrosoft Word").click()
                time.sleep(random.randint(1, 2))
                driver.find_element_by_link_text(".rtfMicrosoft Word").click()
                time.sleep(random.randint(5, 10))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
