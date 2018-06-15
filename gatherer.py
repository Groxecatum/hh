# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import common

FILENAME = '1st.txt'
MAIN_URL = 'https://hh.kz/search/resume?exp_period=all_time&order_by=publication_time&specialization=1&no_magic=true&' \
           'area=160&text=разработчик&pos=full_text&label=only_with_salary&salary_from=0&logic=normal&clusters=true&' \
           'currency_code=KZT&salary_to=200600&page='
START_WITH = 157

class HHGatherer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://almaty.kz/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_gather(self):
        driver = self.driver

        file = open(FILENAME, "a")

        common.auth(driver)

        i = START_WITH - 1
        file.write(MAIN_URL + "\n")
        while True:
            driver.get(MAIN_URL + str(i))
            file.write("Page " + str(i) + "\n")
            i += 1
            elems = False
            for elem in driver.find_elements_by_xpath("(//a[@itemprop='jobTitle'])"):
                elems = True
                file.write(elem.get_property('href') + "\n")
            if not elems:
                break
            file.flush()
            print "Page " + str(i) + " done!"
        print "Job ended!"


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
