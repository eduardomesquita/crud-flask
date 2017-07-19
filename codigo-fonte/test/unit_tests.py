import unittest
import sys
sys.path.append('../app')

from connection.connections import MysqlConnection

class MysqlConnection(unittest.TestCase):
    
    def search(self):
        #self.assertEqual(fun(3), 4)
        pass
        

if __name__ == '__main__':
    unittest.main()