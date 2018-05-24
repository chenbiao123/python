#!/usr/bin/env python
"""this model provides function for authentication users"""

def login(username, password):
    try:
        user_file = open('/etc/users.txt')
        user_buf = user_file.read()
        users = [line.split("|") for line in users_buf.split("\n")]
        if[username,password] in users:
            return True
        else:
            return False
        except Exception,exc:
            print "I cant't authentication you "
            return False
def logout():
    print '这一行不会用测试用例覆盖到'
    print '这一行也不会用测试用例覆盖到'
