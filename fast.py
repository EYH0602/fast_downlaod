import sys
import os
from func_util import foldl

if len(sys.argv) != 2:
    print("Usage: fast github_url")
    exit(1)

url = sys.argv[1]
spurl = url.split('/')
    
def merge_url(acc, s) -> str:
    if acc == "":
        return s
    
    if s == "github.com":
        suffix = s + ".cnpmjs.org"
    elif s == "\n":
        suffix = "/"
    else:
        suffix = s
    
    return acc + "/" + suffix

new_url = foldl(merge_url, "", spurl)

print("git clone " + new_url)
os.execv("/usr/bin/git", ("git", "clone", new_url))
