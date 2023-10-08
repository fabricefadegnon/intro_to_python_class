import unittest
from list_operations import animals


class TestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual(['elephant', 'lion', 'tiger', 'giraffe', 'monkey', 'dog', 'dinosaur'], animals,
                         msg='The resulting list does not match the expected one.')

    def test_dinosaur(self):
        try:
            self.assertTrue(animals[-1] == animals[6] == 'dinosaur', msg='The 7th (and the last) element'
                                                                         'has to be "dinosaur".')
        except IndexError:
            self.assertTrue(False, msg='The list appears to be too short.')