__author__ = 'ddehertog'

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # the user goes to the welcome screen and tries to submit an empty item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # the screen refreshes and says it's a big no-no
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # Now she tries again with some text and it works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # She persists in her devilish ways and tries to submit another blank
        self.get_item_input_box().send_keys('\n')


        # The system remains calm and quietly gives the same error message
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # she can, if she wants to, correct her text
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # someone goes and creates a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy stuff\n')
        self.check_for_row_in_list_table('1: Buy stuff')

        # that person tries to enter the same thing twice!
        self.get_item_input_box().send_keys('Buy stuff\n')

        # no good, she gets put off
        self.check_for_row_in_list_table('1: Buy stuff')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_in_input(self):
        # we start a list and cause a validationerror
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # we see the wrong and amend
        self.get_item_input_box().send_keys('a')

        # while we do, divinely the error message disappears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())