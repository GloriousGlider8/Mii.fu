from FFLResource import *
import requests as r
import json as j

middleRequest = r.get("https://gloriousglider8.github.io/assets/FFLResMiddle.dat")
highRequest   = r.get("https://gloriousglider8.github.io/assets/FFLResHigh.dat")

middleRequest.raise_for_status()
highRequest.raise_for_status()

middleDat = middleRequest.content
highDat   = highRequest.content


