# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 Matthew Good <trac@matt-good.net>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#
# Author: Pedro Algarvio <ufs@ufsoft.org>

from acct_mgr.tests.functional import *

class AcctMgrFunctionalTester(FunctionalTester):
    
    def __init__(self, url, repo_url):
        super(AcctMgrFunctionalTester, self).__init__(url)
        # Don't stay logged in as admin.
        self.logout()

    def login(self, username, passwd=None):
        """Override FunctionalTester.login, we're not using Basic
        Authentication."""
        if not passwd:
            passwd = username
        login_form_name = 'acctmgr_loginform'
        self.go_to_front()
        tc.find('Login')
        tc.follow('Login')
        tc.formvalue(login_form_name, 'user', username)
        tc.formvalue(login_form_name, 'password', passwd)
        tc.submit()
        tc.find("logged in as %s" % username)
        tc.find("Logout")
        tc.url(self.url)
        tc.notfind(internal_error)
        
    def register(self, username, email='', passwd=None):
        """Allow user registration."""
        if not passwd:
            passwd = username
        reg_form_name = 'acctmgr_registerform'
        tc.find("Register")
        tc.follow("Register")        
        tc.formvalue(reg_form_name, 'user', username)
        tc.formvalue(reg_form_name, 'password', passwd)
        tc.formvalue(reg_form_name, 'password_confirm', passwd)
        tc.formvalue(reg_form_name, 'email', email)
        tc.submit()
        tc.notfind("The passwords must match.")
        tc.notfind(internal_error)

