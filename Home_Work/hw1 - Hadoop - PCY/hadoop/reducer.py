from operator import itemgetter
import sys

current_count = 0
current_gen = None
current_ti = None
current_list_ti = []


dictionary_of_ti = {}

# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	current_count += 1

	gen, ti = line.split("\t")

	if current_gen == gen:
		current_list_ti.append(current_ti)
		current_ti = ti
	else:
		if current_gen:
			current_list_ti.append(current_ti)
			print("{}\t{}".format(current_gen, current_list_ti))
			current_list_ti = []
		current_gen = gen
		current_ti = ti

if current_gen == gen:
	current_list_ti.append(current_ti)
	print("{}\t{}".format(current_gen, current_list_ti))




	'''# slpiting the data on the basis of tab we have provided in mapper.py
	word, count = line.split('\t', 1)
	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
	else:
		if current_word:
			# write result to STDOUT
			print('{}\t{}'.format(current_word, current_count))
		current_count = count
		current_word = word

# do not forget to output the last word if needed!
if current_word == word:
	print('{}\t{}'.format(current_word, current_count))'''