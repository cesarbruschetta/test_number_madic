''' test to script '''

import unittest

from script import count_number_madic


class TestScriptMethod(unittest.TestCase):

    def setUp(self):
        """ """
        
        self.simple_list = {
            "list": [[8, 27], [49, 49]],
            "result": 3
        }
        
        self.little_list = {
            "list": [[1, 10]],
            "result": 2
        }
        
    def test_simple_list(self):
        """ test of the simple list """
        
        result = count_number_madic(self.simple_list['list'])
        self.assertEqual(result, self.simple_list['result'])

    def test_little_list(self):
        """ test of the simple list """
        
        result = count_number_madic(self.little_list['list'])
        self.assertEqual(result, self.little_list['result'])









if __name__ == '__main__':
    unittest.main()



