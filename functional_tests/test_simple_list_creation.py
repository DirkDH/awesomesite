__author__ = 'ddehertog'

from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # someone checks out the homepage
        self.browser.get(self.server_url)

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
        # the site takes her to the url of her list
        # and shows the first item
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1 : Buy peacock feathers')

        # the user sees this as the page is automatically updated and is immediately invited to do another one
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # each time you add one and press enter this is visible
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('2 : Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1 : Buy peacock feathers')

        # now good old buddy Francis comes along

        # We use a new browser session to make sure no information from Edith is still there
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # As hoped, there is noe information from Edith
        # as Francis treads his first steps into the site
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis enters a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets what he deserves, his own url
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        # Again, no trace of Ediths existence is there
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Buy milk', page_text)
        self.assertNotIn('Buy peacock feathers', page_text)

        # satisfied they both go back to sleep