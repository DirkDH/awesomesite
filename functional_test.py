__author__ = 'ddehertog'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # someone checks out the homepage
        self.browser.get('http://localhost:8000')

        # and is expecting to see a to do list app
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # you can add items in the textbox
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )


        # she wants to go and buy peakock feathers
        inputbox.send_keys("Buy peacock feathers")

        # pressing enter they are stored
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows)
        )

        # the user sees this as the page is automatically updated and is immediately invited to do another one
        # each time you add one and press enter this is visible
        self.fail("Finish the test!")

        # The user expects the items to be stored. A unique url makes sure they are retrievable

        # she visits that url - her list is still there

        # then she quietly walks away and leaves

if __name__ == '__main__':
    unittest.main(warnings='ignore')
