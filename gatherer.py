# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import common


class HHGatherer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://almaty.hh.kz/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver

        file = open(common.FILENAME, "w")

        common.auth(driver)

        for elem in driver.find_elements_by_xpath("(//a[@itemprop='jobTitle'])"):
             file.write(elem.get_property('href'))
             file.flush()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
