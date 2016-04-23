import os
import sys
import random

n = int(sys.argv[1])

urls = []
for f in sys.argv[2:]:
	urls.extend([url.strip() for url in open(f)])

random.shuffle(urls)
for i in range(n):
	print(urls[i])