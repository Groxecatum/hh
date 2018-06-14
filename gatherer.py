# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import common


class HHGatherer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://almaty.kz/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver

        file = open(common.FILENAME, "a")

        common.auth(driver)

        i = common.START_WITH - 1
        while True:
            driver.get(common.MAIN_URL + str(i))
            file.write("Page " + str(i) + "\n")
            i += 1
            for elem in driver.find_elements_by_xpath("(//a[@itemprop='jobTitle'])"):
                 file.write(elem.get_property('href') + "\n")
            file.flush()


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
