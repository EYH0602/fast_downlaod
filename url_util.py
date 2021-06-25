from func_util import foldl

def change_url(url: str) -> str:
    spurl = url.split('/')
    for idx, s in enumerate(spurl):
        if s == "github.com":
            spurl[idx] += ".cnpmjs.org"

    def merge_url(acc, s) -> str:
        if acc == "":
            return s
        suffix = "/" if s == "\n" else s
        return acc + "/" + suffix

    return foldl(merge_url, "", spurl)
