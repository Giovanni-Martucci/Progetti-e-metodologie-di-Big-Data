from operator import itemgetter
import sys

min_distance = None
min_key_y = None
min_key_x = None

current_distance = None
current_key_y = None
current_key_x = None
print("key_y\t[key_x, distance_min]")
for line in sys.stdin:
	line = line.strip()
	key_y, key_x__distance = line.split("\t")
	key_x__distance = key_x__distance.strip("][")

	if current_key_y == key_y:
		if min_distance is None or float(min_distance) > float(current_distance):
			min_distance = current_distance
			min_key_x = current_key_x
			min_key_y = current_key_y
	elif min_distance is None:
		min_key_x, min_distance = key_x__distance.split(",")
		min_key_x = min_key_x.strip("'")
		min_distance = min_distance.strip()
		min_key_y = key_y
	else:
		if float(min_distance) > float(current_distance):
			min_distance = current_distance
			min_key_x = current_key_x
			min_key_y = current_key_y
		print("{}\t{}".format(min_key_y, [min_key_x, min_distance]))
		min_distance = min_key_x = min_key_y = None

	current_key_y = key_y
	current_key_x = key_x__distance.split(",")[0].strip("  '")
	current_distance = key_x__distance.split(",")[1].strip(" ' ")


if min_distance is None or float(min_distance) > float(current_distance):
	min_distance = current_distance
	min_key_x = current_key_x
	min_key_y = current_key_y
print("{}\t{}".format(min_key_y, [min_key_x, min_distance]))





