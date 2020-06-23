#!/usr/bin/env python3

from bookhack_ikoblyk.test import Work
import os, re
url=None
reg = re.compile(r"^https://elib.nlu.org.ua/view.html\?&id=\d+")
while reg.fullmatch(url) is None:
    url = input("paste a valid url: ")
    reg=url
else:
    Work(url).run()
