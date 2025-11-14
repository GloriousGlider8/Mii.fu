from FFLResource import *
import requests as r

# find some path to ffl res data files

resMiddleDat = r.get("").content
resHighDat = r.get("").content

# TODO implement tests