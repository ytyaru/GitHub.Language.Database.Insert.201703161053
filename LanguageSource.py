import urllib.request
import os
import yaml
import requests
import pprint
class LanguageSource(object):
    def __init__(self):
        pass
    def Get(self, is_show=True):
        url_str = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"
        file_name = os.path.basename(url_str)
        if is_show:
            print(url_str)
            print(file_name)
        if not(os.path.isfile(file_name)):
            r = requests.get(url_str)
            with open(os.path.basename(file_name), mode='wt', encoding='utf-8') as f:
                f.write(r.text)
                if is_show:
                    print(r.text)
        with open(os.path.basename(file_name), mode='r', encoding='utf-8') as f:
            y = yaml.load(f)
            if is_show:
                pprint.pprint(y)
            return y

