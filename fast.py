import sys
import os
from url_util import change_url

if len(sys.argv) != 2:
    sys.stderr("Usage: fast github_url\n")
    exit(1)

url = sys.argv[1]
new_url = change_url(url)
print("git clone " + new_url)
os.execv("/usr/bin/git", ("git", "clone", new_url))
