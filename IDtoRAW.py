#Strips spaces and returns clean string variables
def strp (var):
	var = var.strip(" ")
	var = var.strip("\n")
	var = var.strip("*")
	#var = "".join(var.split())
	return var
	
def strp2 (var):
	var = var.strip(" ")
	var = var.strip("\n")
	return var	

print " "
name = raw_input("Enter raw file to switch out metabolites names (ex 'adipose_rawt.csv'): ")
if len(name) == 0 : name = "adipose_rawt.csv"
handle1 = open(name)
handle1.close()

#Parse the first Fold Change file and add to a dictionary
title = list()
n=0
handle1 = open(name)
for line in handle1:
	t = "," + line
	t = strp(t)
	title.append(t) 
	n = n + 1
	print t
	if n == 2:
		break
dict = dict()
handle1.close()

n1 = 0
handle1 = open(name)
handle1.readline()
for line in handle1:
	if line[:1] == "\"":
		pieces = line.split("\"")
		met = pieces[1]
	elif line[:1] == " " or line[:1] == ",":
		met = ""
		continue
	else:
		pieces = line.split(",")
		met = pieces[0]
	met = strp(met)
	dict[met] = (line)
	n1 = n1 + 1
handle1.close()

for i in dict:
	print i
	
print " "
name = raw_input("Enter masterlist of metabolites file (enter for 'NRmet.csv'): ")
if len(name) == 0 : name = "NRmet.csv"
handle2 = open(name)
handle2.close()

#Parse the second file for significance valuse, and replace dictionary 
#with new string of 3 values for matching keys.
n2 = 0
n4 = 0
handle2 = open(name)
handle2.readline()
for line in handle2:
	pieces = line.split(",")
	try:
		ID = pieces[-2]
		pieces = line.split("\"")
		met = pieces[1]
		ID = strp(ID)
	except:
		ID = "fail"
		print "fail"
	if met in dict.keys():
		replace = dict[met]
		if replace [:1] == "*":
			if replace[1:10] == ID:
				print "Found again (same ID)"
				continue
			else:
				replace = replace[1:]
				replace = "****2IDs%s %s" % (ID, replace)
				print "Found again (different ID)"
				n4 = n4 + 1
		else:	
			replace = "*%s,%s" % (ID, replace)
			print "Found it"
		dict[met] = replace
		n2 = n2 + 1
	else:
		continue
handle2.close()

n3 = 0
for key, value in dict.items():
	if value [:1] == "*":
		replace = value[1:]
	else:
		replace = "***NM,\"" + value[1:]
		n3 = n3 + 1
	dict[key] = replace

for keys, values in dict.items():
	v = values
	k = keys
	v = strp2(v)
	k = strp2(k)
	dict[keys] = v
	dict[keys] = dict.pop(k)

n3 = n3 - n4
print "\n\nMatched %i of %i metabolites from: %s" % (n2, n1, handle1)
print "There were %i unmatched and %i with multiple IDs, flagged for manual review.\n" % (n3, n4)
	
print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'Default'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "adipose_rawtOut.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
#f.write("Significant changes for: ")
#f.write(name)
#f.write ("\n\n")
#f.write("Metabolite, FC, P-value, FDR, Metabolon ID, KEGG, HMBD, PUBCHEM\n")
for i in title:
	f.write(i)
for keys, values in dict.items():
	f.write(values)
	f.write("\n")
f.close()
print "Saved as:", savename	