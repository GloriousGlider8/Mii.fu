from FFLResource import *
import requests as r

# find some path to ffl res data files

middleRequest = r.get("https://gloriousglider8.github.io/assets/FFLResMiddle.dat")
highRequest   = r.get("https://gloriousglider8.github.io/assets/FFLResHigh.dat")



# TODO implement tests