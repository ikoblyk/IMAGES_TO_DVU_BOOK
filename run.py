#!/usr/bin/env python3
import sys
from bookhack_ikoblyk.test import Work
w = Work(sys.argv[1], '/home/automation/app/books')
w.run()
