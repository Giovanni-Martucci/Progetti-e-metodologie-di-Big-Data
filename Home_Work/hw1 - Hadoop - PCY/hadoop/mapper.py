# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
button_ti_ab = False
button_ti_complete = True
button_ab_complete = True

couple_gen = ""

dict_ti_ab = {}  # dictionary of papers
gen_uniq = {}

second_file = False
cont_line = 0


for line in sys.stdin:
	# to remove leading and trailing whitespace
	line = line.strip()
	cont_line += 1

	if line.find("ENST00000456328") != -1:
		second_file = True

	if second_file:     # metadata
		gen = line.split("\t")[1]

		if gen not in gen_uniq:
			gen_uniq[gen] = 1
			for key, value in dict_ti_ab.items():
				if value.find(" "+gen+" ") != -1:
					print("{}\t{}".format(gen, key))

	else: 		# pubmed
		if line.find("TI  - ") != -1:
			if button_ti_ab:
				# fix when paper has only TI without AB
				couple_gen = ""

			couple_gen += line[6:]  # + "\t\t"
			button_ti_ab = True
			button_ti_complete = False

		elif line.find("AB  - ") != -1:
			# couple generated
			couple_gen += line[6:]

			button_ti_ab = False
			button_ab_complete = False

		elif not button_ti_complete:
			if line.find(" - ") == -1:
				couple_gen += " "+line
			else:
				couple_gen += "\t\t"
				button_ti_complete = True
				
		elif not button_ab_complete:
			if line.find(" - ") == -1:
				couple_gen += line
			else:
				button_ab_complete = True

				# save couple in dict
				ti, ab = couple_gen.split("\t\t", 1)
				dict_ti_ab[ti] = ab
				button_ti_ab = True
