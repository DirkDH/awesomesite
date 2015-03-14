__author__ = 'ddehertog'

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # the user goes to the welcome screen and tries to submit an empty item
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # the screen refreshes and says it's a big no-no
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # Now she tries again with some text and it works
        self.browser.find_element_by_css_selector('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # She persists in her devilish ways and tries to submit another blank
        self.browser.find_element_by_css_selector('id_new_item').send_keys('\n')


        # The system remains calm and quietly gives the same error message
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # she can, if she wants to, correct her text
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')