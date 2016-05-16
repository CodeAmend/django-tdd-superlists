from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Lacy hears about a To-Do site and visits the home page
        self.browser.get('http://localhost:8000')

        # Lacy notices that "To-Do" is in the title
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Lacy is invited right away to enter items into the to-do list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Lacy types in "buy eggs for egg salad"
        inputbox.send_keys('Buy eggs for egg salad')

        # When she hits enter the page is updated with
        # "1: buy eggs for egg salad"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        # self.assertTrue(
        #     any(row.text == '1: buy eggs for egg salad' for row in rows),
        #     "New to-do item did not appear in table -- its text was:\n%s" % (
        #         table.text
        #     )
        # )
        # Much simpler test
        self.assertIn('1: Buy eggs for egg salad', [row.text for row in rows])

        # There is still a text box waiting for another to-do item
        # she enters "make egg salad"
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("make egg salad")

        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            '2: make egg salad',
            [row.text for row in rows]
        )

        # she wonders if the site will remember her list
        # she sees that a unique URL was generated for her -- some explanatory text as well

        self.fail("finish the test!")

        # she visits the URL and her list is just as she left it.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
