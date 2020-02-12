#Program to get metabolic assignments: 


def strp (var):
	var = var.strip(" ")
	var = var.strip("\n")
	var = var.strip("*")
	return var

print " "
name = raw_input("Enter master list file name or ENER for 'allmet.csv': ")
if len(name) == 0 : name = "allmet.csv"
handle1 = open(name)
handle1.close()

dict = dict()

n=0
nr=0
handle1 = open(name)
handle1.readline()


masterlist = list()
for line in handle1:
	newline = ""
	if line[:1] == "\"":
		newline = line
		newline = "\"" + newline + "\""
		continue
	else:
		npieces = line.count(",")
		pieces = line.split(",")
		for i in xrange(0, npieces -3):
			newline = newline + pieces[i]
			newline = strp(newline)

		newline = "\"" + newline + "\""
		ID = pieces[-4]
		KEGG = pieces[-3]
		HMBD = pieces[-2]
		PUBCHEM = pieces[-1]
		ID = strp(ID)
		KEGG = strp(KEGG)
		HMBD = strp(HMBD)
		PUBCHEM = strp(PUBCHEM)
		newline	= "%s, %s, %s, %s, %s" % (newline, ID, KEGG, HMBD, PUBCHEM)
	masterlist.append(newline)
handle1.close()



for line in masterlist:
	
	pieces = line.split("\"")
	met = pieces[1]
		
	pieces = line.split(",")
	ID = pieces[-4]
	KEGG = pieces[-3]
	HMBD = pieces[-2]
	PUBCHEM = pieces[-1]
	
	met = strp(met)
	met = "\"" + met + "\""
	ID = strp(ID)
	KEGG = strp(KEGG)
	HMBD = strp(HMBD)
	PUBCHEM = strp(PUBCHEM)
	
	if ID in dict.keys():
		n = n + 1
	else: 
		add = "%s, %s, %s, %s, %s" % (met, ID, KEGG, HMBD,PUBCHEM)
		dict[ID] = add
		nr = nr + 1
		
for keys, values in dict.items():
	#print keys
	print values

print "\nThere were ", n, " redundant metabolites, and ", nr, " non-redundant compiled."

print " "	
savename = raw_input("To save a list of non redundant metabolites, enter a file name (Blank to exit without saving, Enter d for 'NRmet'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "NRmet.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
#f.write("Significant changes for: ")
#f.write(name)
#f.write ("\n\n")
f.write("Metabolite, Metabolon ID, KEGG, HMDB, PUBCHEM\n")
for keys, values in dict.items():
	f.write(values)
	f.write("\n")
f.write ("\n")
f.close()
print "\n", nr,
print " metabolites with IDs saved as: ", savename	



