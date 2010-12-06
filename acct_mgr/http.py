# -*- coding: utf8 -*-
#
# Copyright (C) 2005 Matthew Good <trac@matt-good.net>
#
# "THE BEER-WARE LICENSE" (Revision 42):
# <trac@matt-good.net> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.   Matthew Good
#
# Author: Matthew Good <trac@matt-good.net>

from urllib2 import build_opener, HTTPBasicAuthHandler, \
                    HTTPDigestAuthHandler, HTTPPasswordMgrWithDefaultRealm

from trac.core import *
from trac.config import Option

from api import IPasswordStore, _


class HttpAuthStore(Component):
    implements(IPasswordStore)

    auth_url = Option('account-manager', 'authentication_url', '',
        doc = _("URL of the HTTP authentication service"))

    def check_password(self, user, password):
        mgr = HTTPPasswordMgrWithDefaultRealm()
        mgr.add_password(None, self.auth_url, user, password)
        try:
            build_opener(HTTPBasicAuthHandler(mgr),
                         HTTPDigestAuthHandler(mgr)).open(self.auth_url)
        except IOError:
            return None
        except ValueError:
            return None
        else:
            return True

    def get_users(self):
        return []

    def has_user(self, user):
        return False
