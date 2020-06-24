#!/usr/bin/env python3
import sys
from bookhack_ikoblyk.test import Work
url=sys.argv[1]
w = Work(url=url)
w.run()
