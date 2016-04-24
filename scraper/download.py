import os
import urllib
import multiprocessing
import sys

if len(sys.argv) < 3:
    print("download.py IN.txt OUTDIR")
    exit()


def download(tup):
	if not os.path.isfile(tup[1]):
		try:
			urllib.urlretrieve(tup[0], tup[1])
		except:
			pass


try:
	os.makedirs(sys.argv[2])
except:
	pass

listUrls = [(url.strip(), os.path.join(sys.argv[2], url.strip().split('/')[-1])) for i, url in enumerate(open(sys.argv[1]))]

pool = multiprocessing.Pool(processes=4)
pool.map(download, listUrls)
