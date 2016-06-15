from functional_tests.base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Lacy hears about a To-Do site and visits the home page
        self.browser.get(self.server_url)

        # Lacy notices that "To-Do" is in the title
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Lacy is invited right away to enter items into the to-do list
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Lacy types in "buy eggs for egg salad"
        inputbox.send_keys('buy eggs for egg salad')

        # When she hits enter she is directed to a unique URL
        # 1: buy eggs for egg salad is listed as the first item.
        inputbox.send_keys(Keys.ENTER)

        lacy_list_url = self.browser.current_url
        self.assertRegex(lacy_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: buy eggs for egg salad')

        # There is still a text box waiting for another to-do item
        # she enters "make egg salad"
        inputbox = self.get_item_input_box()
        inputbox.send_keys("make egg salad")

        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: buy eggs for egg salad')
        self.check_for_row_in_list_table('2: make egg salad')

        # Now a new user Francis comes to the site

        # A new browser session to emulate a new user with different cookies.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits home page and there is no sign of Lacy's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy eggs for egg salad', page_text)
        self.assertNotIn('make egg salad', page_text)

        # Francis starts adding list items
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis is taken to a unique URL
        # first item is "1: Buy milk"

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, lacy_list_url)

        # again, no trace of Lacy's list
        self.assertNotIn('buy eggs for egg salad', page_text)
        self.assertNotIn('make egg salad', page_text)

        # she visits the URL and her list is just as she left it.

