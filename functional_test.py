__author__ = 'ddehertog'

from selenium import webdriver
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
        self.fail('Finish the test')

        # you can add items in the textbox


        # pressing enter they are stored


        # the user sees this as the page is automatically updated and is immediately invited to do another one


        # each time you add one and press enter this is visible


        # The user expects the items to be stored. A unique url makes sure they are retrievable


        # she visits that url - her list is still there


        # then she quietly walks away and leaves

if __name__ == '__main__':
    unittest.main(warnings='ignore')
