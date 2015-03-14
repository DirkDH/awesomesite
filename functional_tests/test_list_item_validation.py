__author__ = 'ddehertog'

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # the user goes to the welcome screen and tries to submit an empty item

        # the screen refreshes and says it's a big no-no

        # Now she tries again with some text and it works

        # She persists in her devilish ways and tries to submit another blank

        # The system remains calm and quietly gives the same error message

        # she can, if she wants to, correct her text
        self.fail('write me!')