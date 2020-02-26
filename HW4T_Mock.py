#!/usr/bin/env python
# coding: utf-8

# In[30]:


import unittest
from unittest import mock

import HW4

class TestGit(unittest.TestCase):
    @mock.patch('HW4.git')
    def test1(self, mock_git):
        mock_git("richkempinski").return_value = {'hellogitworld': 30,'helloworld': 6,'Mocks': 10,'Project1': 2,'threads-of-life': 1}
        self.assertEqual(mock_git("richkempinski").return_value,{'hellogitworld': 30,'helloworld': 6,'Mocks': 10,'Project1': 2,'threads-of-life': 1})

    @mock.patch('HW4.git')    
    def test2(self, mock_git):
        mock_git("asdfasfas").return_value = {}
        self.assertEqual(mock_git("asdfasfas").return_value,{})

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity = 2)


# In[ ]:




