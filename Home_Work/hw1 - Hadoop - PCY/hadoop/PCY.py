import sys
import os

# h(i,j) = (a*i + b*j) % N
a = int(sys.argv[2])
b = int(sys.argv[3])
N = int(sys.argv[4])

#s is threshold
s = int(sys.argv[5])

counttable = {}
frequentitem = []
lines = []
candidates = {}
frequentbuckets = {}
bitmap = []
frequentitems = []
pruncandidates = []
pass2count = {}
falsepositive = 0


# path output directory
file_path = "./" + sys.argv[6] + "/"
directory = os.path.dirname(file_path)

hash_convert_name = {}
cont_paper = 0

try:
    os.stat(directory)
except:
    os.mkdir(directory)


for i in range(0, N):
    frequentbuckets[i] = 0

with open(sys.argv[1], "r") as file:
    lines = file.readlines()

for line in lines:
    gen, list_of_papers_str = line.split("\t")

    list_of_papers = list_of_papers_str.strip("][").split(",")
    # print("{}) {} - {}".format(cont, type(list_of_papers), list_of_papers))
    # count table
    for paper_orig in list_of_papers:
        paper = paper_orig.strip(" ' ").replace("']", "")
        if paper not in hash_convert_name:
            hash_convert_name[paper] = cont_paper
            paper_to_int = cont_paper
            cont_paper += 1
        else:
            paper_to_int = hash_convert_name[paper]
        if paper_to_int not in counttable:
            counttable[paper_to_int] = 1
        else:
            counttable[paper_to_int] += 1

    # frequent buckets
    for i in range(0, len(list_of_papers) - 1):
        for j in range(i + 1, len(list_of_papers)):
            frequentbuckets[(a * int(hash_convert_name[list_of_papers[i].strip(" ' ").replace("']", "")]) + b * int(hash_convert_name[list_of_papers[j].strip(" ' ").replace("']", "")])) % N] += 1


# frequent item
for num in counttable:
    if counttable[num] >= s:
        frequentitem.append(num)


frequentitem.sort(key=int)

# #frequent buckets bitmap
for bucket in frequentbuckets:
    if frequentbuckets[bucket] >= s:
        bitmap.append(bucket)

falsepositive = float(len(bitmap)) / len(frequentbuckets)
print("False Postitive Rate: %.3f" % falsepositive)

# initial candidates
for i in range(0, len(frequentitem) - 1):
    for j in range(i + 1, len(frequentitem)):
        if (a * int(frequentitem[i]) + b * int(frequentitem[j])) % N not in bitmap:
            pruncandidates.append((int(frequentitem[i]), int(frequentitem[j])))
        else:
            if (int(frequentitem[i]),int(frequentitem[j])) not in candidates:
                candidates[(int(frequentitem[i]), int(frequentitem[j]))] = 0

for line in lines:
    gen, list_of_papers_str = line.split("\t")
    list_of_papers = list_of_papers_str.strip("][").split(",")

    # count candidates
    for i in range(0, len(list_of_papers) - 1):
        for j in range(i + 1, len(list_of_papers)):
            if (int(hash_convert_name[list_of_papers[i].strip(" ' ").replace("']", "")]), int(hash_convert_name[list_of_papers[j].strip(" ' ").replace("']", "")])) in candidates:
                candidates[(int(hash_convert_name[list_of_papers[i].strip(" ' ").replace("']", "")]), int(hash_convert_name[list_of_papers[j].strip(" ' ").replace("']", "")]))] += 1

for candidate in candidates:
    if candidates[candidate] >= s:
        frequentitems.append(candidate)

frequentitems.sort()
frequentitem = frequentitem + frequentitems


with open(file_path + "frequentset.txt", "w") as wf:
    reverse_dict = dict(map(reversed, hash_convert_name.items()))
    for value in frequentitem:
        if type(value) == tuple:
            out_ = (reverse_dict[value[0]] , reverse_dict[value[1]])
            wf.write(str(out_) + "\n")

with open(file_path + "frequentset.txt", "r") as file:
    lines = file.readlines()

with open(sys.argv[1], "r") as file:
    lines_output = file.readlines()

    for line in lines:
        first, second = tuple(line.replace("('", "").replace("'", "").replace(")", "").split(", "))
        list_gen = []
        for line_out in lines_output:
            gen, list_of_pap = line_out.split("\t")
            list_of_papers = list_of_pap.replace(" ", "")
            if list_of_papers.find(first.replace(" ", "")) != -1 and list_of_papers.find(second[:-3].replace(" ", "")) != -1:
                    list_gen.append(gen)
        print("{} ---> {}".format(line, list_gen))

