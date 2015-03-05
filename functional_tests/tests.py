__author__ = 'ddehertog'

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

    def test_can_start_a_list_and_retrieve_it_later(self):
        # someone checks out the homepage
        self.browser.get(self.live_server_url)

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
        self.check_for_row_in_list_table('1 : Buy peacock feathers')

        # the user sees this as the page is automatically updated and is immediately invited to do another one
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # each time you add one and press enter this is visible
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1 : Buy peacock feathers')
        self.check_for_row_in_list_table('2 : Use peacock feathers to make a fly')


        # The user expects the items to be stored. A unique url makes sure they are retrievable
        self.fail("Finish the test!")

        # she visits that url - her list is still there

        # then she quietly walks away and leaves