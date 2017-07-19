import unittest
import sys
sys.path.append('../app')

from utils.string_utils import StringUtils

class StringUtilsTest(unittest.TestCase):
    
    def test_upper(self):
         self.assertEqual(StringUtils().to_upper('TEST upper'), 'TEST UPPER')

    def test_lower(self):
         self.assertEqual(StringUtils().to_lower('TEST Lower'), 'test lower')

    def test_is_upper(self):
         self.assertFalse(StringUtils().is_upper('TEST Lower'))

    def test_join(self):
         self.assertEqual(StringUtils().join(['a', 'b', 'c']), 'a,b,c')

if __name__ == '__main__':
    unittest.main()