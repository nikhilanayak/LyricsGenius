from lyricsgenius.types.song import Song
from parallelize import parallelize
from tqdm import tqdm
from typing import List
import json
import traceback
import lyricsgenius
import time
import gc
import os
import glob
import sys

genius = lyricsgenius.Genius("DLi7m1FHqWPDP0Lktod1LXAUqC06IpNHpPIQ6i3ZtCpmJ7xwRLGMT3qimxAxMKrn")
genius.verbose = False

start = time.time()

i = 0
os.chdir("/home/nikhil")
for file in list(glob.glob("piece*")):
	os.chdir("/mnt/sd")
	print(file)
	with open("/home/nikhil/" + file, "r", encoding="utf-8") as file:
		lines = file.readlines()[47637:]
		print(len(lines))
		@parallelize(lines, num_threads=10)
		def run(line):
			global i
			try:
				data = json.loads(line)
				artist_name = data["response"]["artist"]["name"]
				artist = genius.search_artist(artist_name)
				for song in artist.songs:
					song.to_json(f"/mnt/sd/{artist_name}_{song.full_title}.json")
				gc.collect()
				print(i)
				i += 1
			except:
				traceback.print_exc()
				print("failed", i)
				pass
			
		[l for l in run()]
				


	print(time.time() - start)
