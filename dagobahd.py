# !/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /dagobahd.py
# Project: dagobah
# Created Date: 2019-09-15 22:42:33
# Author: huxh
# -----
# Last Modified: Sun Sep 22 2019
# Modified By: huxh
# -----
# Copyright (c) 2019 X
# 
# All shall be well and all shall be well
# and all manner of things shall be well.
# Nope...we're doomed!
# -----
# HISTORY:
# Date      	By		Comments
###
# !/mnt/d/code/PyProjects/dagobah/py35/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'dagobah==0.3.4','console_scripts','dagobahd'
__requires__ = 'dagobah==0.3.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('dagobah==0.3.4', 'console_scripts', 'dagobahd')()
    )