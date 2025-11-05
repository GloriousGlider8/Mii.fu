import json as j
import requests as r
import os

OUTPUT = "fut.deb"

release = j.loads(r.get("https://api.github.com/repos/fusionlanguage/fut/releases/latest").content)

for a in release["assets"]:
	if a["name"].endswith(".deb"):
		print(a["name"])
		asset = r.get(a["browser_download_url"]).content
		with open(OUTPUT, "wb") as f:
			f.write(asset)
		break

os.system(f"sudo apt install {os.path.abspath(OUTPUT)}")
os.remove(OUTPUT)