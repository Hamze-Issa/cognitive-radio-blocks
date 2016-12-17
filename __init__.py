
...
This is the GNU Radio COWN module. Place your Python package
description here (python/__init__.py).
'''

# import swig generated symbols into the COWN namespace
try:
	# this might fail if the module is python-only
	from COWN_swig import *
except ImportError:
	pass

# import any pure python here
#
