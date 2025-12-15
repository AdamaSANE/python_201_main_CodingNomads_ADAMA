# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.

import os
from collections import Counter

# Example: Count the number of files by extension in the current directory
file_types = []
for filename in os.listdir('.'):
	if os.path.isfile(filename):
		ext = os.path.splitext(filename)[1].lower()
		if ext:
			file_types.append(ext)

counts = Counter(file_types)
print("File type counts:")
for ext, count in counts.items():
	print(f"{ext}: {count}")
