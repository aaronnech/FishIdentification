import os
import sys
import random
import subprocess

if len(sys.argv) < 4:
    print("./multi_query.py N queries.txt out")
    exit()

n = int(sys.argv[1])
queries = [query.strip() for query in open(sys.argv[2])]
dest = sys.argv[3]

try:
	os.makedirs(dest)
except:
	pass

for query in queries:
	# Scrape the query
	output = os.path.join(dest, query.replace(' ', '_') + '.txt')
	cmd = ['node', 'scrape.js', str(n)]
	cmd.extend(query.split(' '));
	links = subprocess.check_output(cmd)
	with open(output, "w") as f:
		f.write(links)