#!/usr/bin/env python3

import os

os.system("python3 web/generatePlaylist.py")
os.system("python3 web/generateHtml.py")

print("Html generated!")
