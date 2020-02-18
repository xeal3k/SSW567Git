#!/usr/bin/env python
# coding: utf-8

# In[7]:


import unittest

from HW4 import git

class TestGit(unittest.TestCase):
    def test1(self):
        self.assertEqual(git("richkempinski"),{'hellogitworld': 30,'helloworld': 6,'Mocks': 10,'Project1': 2,'threads-of-life': 1})
        
    def test2(self):
        self.assertEqual(git("asdfasfas"),{})
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity = 2)


# In[ ]:




