from selenium import webdriver
import unittest


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
        self.fail("Finish the test!")

        # Lacy is invited right away to enter items into the to-do list

        # Lacy types in "buy eggs for egg salad"

        # When she hits enter the page is updated with
        # "1: buy eggs for egg salad"

        # There is still a text box waiting for another to-do item

if __name__ == '__main__':
    unittest.main(warnings='ignore')
