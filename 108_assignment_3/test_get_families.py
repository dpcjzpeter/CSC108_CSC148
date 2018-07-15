import unittest
import network_functions

class TestGetFamilies(unittest.TestCase):

    def test_get_families_empty(self):
        param = {}
        actual = network_functions.get_families(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_person_one_friend_diff_family(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_person_one_friend_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_two_people_one_friend_reversed_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett'], 'Gloria Pritchett': ['Jay Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_person_multiple_friends_diff_family(self):
        param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay'], 'Dunphy': ['Claire'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_one_person_multiple_friends_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Mitchell Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_multiple_people_multiple_friends_diff_family(self):
        param = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell'], 'Dunphy': ['Claire', 'Luke', 'Phil'], 'Delgado': ['Manny']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_multiple_people_multiple_friends_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Mitchell Pritchett'], 'Gloria Pritchett': ['Jay Pritchett', 'Mitchell Pritchett'], 'Mitchell Pritchett': ['Gloria Pritchett', 'Jay Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
if __name__ == '__main__':
    unittest.main(exit=False)