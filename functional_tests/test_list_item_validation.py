__author__ = 'ddehertog'

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # the user goes to the welcome screen and tries to submit an empty item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # the screen refreshes and says it's a big no-no
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # Now she tries again with some text and it works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # She persists in her devilish ways and tries to submit another blank
        self.get_item_input_box().send_keys('\n')


        # The system remains calm and quietly gives the same error message
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # she can, if she wants to, correct her text
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # someone goes and creates a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy stuff')
        self.check_for_row_in_list_table('1: Buy stuff')

        # that person tries to enter the same thing twice!
        self.get_item_input_box().send_keys('Buy stuff')

        # no good, she gets put off
        self.check_for_row_in_list_table('1: Buy stuff')
        error = self.browser.find_element_by_css_selector('.has_error')
        self.assertEqual(error.text, "You've already got this in your list")