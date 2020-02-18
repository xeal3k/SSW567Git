#!/usr/bin/env python
# coding: utf-8

# In[69]:


import requests
import json


# In[74]:


def main():
    user_name = input("Input User Name: ")
    result = git(user_name)
    return result

def git(user_name):
    r = requests.get("https://api.github.com/users/" + user_name + "/repos")
    if r.status_code != 200:
        print("User name is invalid!")
        return "User name is invalid!"
    pretty_json = json.loads(r.text)
    js = json.dumps(pretty_json)
    repo = {}
    for i in range(len(js)):
        output = ""
        if js[i: i + 6] == '"name"':
            j = 9
            while js[i + j] != '"':
                output += js[i+j]
                j += 1
            repo[output] = 0
    
    for item in repo:
        r = requests.get("https://api.github.com/repos/" + user_name + "/" + item + "/commits")
        pretty_json = json.loads(r.text)
        js = json.dumps(pretty_json)
        for i in range(len(js)):
            if js[i: i + 8] == '"commit"':
                repo[item] += 1
    for item in repo:
        print("Repo: " + item + " Number of commits: " + str(repo[item]))
    return repo


# In[75]:


main()


# In[38]:





# In[ ]:




