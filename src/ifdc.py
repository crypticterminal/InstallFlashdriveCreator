#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ifdclib.py
#  
#  Copyright 2017 Igor Kolonchenko <enepunixoid@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

import platform, os, logging
import subprocess,pexpect

#log = logging.log(__name__)

def sudo_exec(cmdline,password):
   osname = platform.system()
   if osname == "Linux":
      promt = r'/[sudo]/ password %s:' % os.environ["USER"]
   elif osname == "Darwin":
      promt = 'Password: '
   else:
      assert False,osname 
   child = pexpect.spawn(cmdline)
   idx = child.expect([promt, pexpect.EOF], 3)
   if idx == 0:
 #     log.debug("sudo password was asked")
      child.sendline(password)
      child.expect(pexpect.EOF)

   return child.before
       

def main(args):
    print("+-----------------------------------------------------------+")
    print("|          sudo exec test                                   |")
    print("+-----------------------------------------------------------+")
    print(sudo_exec("lsusb",""))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
