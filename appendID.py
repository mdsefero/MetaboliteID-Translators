#Strips spaces and returns clean string variables
def strp (var):
	var = var.strip(" ")
	var = var.strip("\n")
	return var

print " "
name = raw_input("Enter changing metbolite file file (enter for 'ChangingMet.csv'): ")
if len(name) == 0 : name = "ChangingMet.csv"
handle1 = open(name)
handle1.close()

dict = dict()

#Parse the first Fold Change file and add to a dictionary
n1=0
handle1 = open(name)
handle1.readline()
for line in handle1:
	met = ""
	if line[:1] == "\"":
		pieces = line.split("\"")
		met = pieces[1]
		changes = pieces[2]
		met = strp(met)
		met = "\"" + met + "\""
		changes =  changes[1:]
		changes = strp(changes)
		dict[met] = (changes)
		n1 = n1 + 1
		#print changes
	else:
		continue
handle1.close()

#for keys, values in dict.items():
#	print keys
#	print values

print " "
name = raw_input("Enter masterlist of metabolites file (enter for 'NRmet.csv'): ")
if len(name) == 0 : name = "NRmet.csv"
handle2 = open(name)
handle2.close()

#Parse the second file for significance valuse, and replace dictionary 
#with new string of 3 values for matching keys.
n = 0
handle2 = open(name)
handle2.readline()
for line in handle2:
	
	replace = ""
	met = ""
	if line[:1] == "\"":
		#print "yes"
		pieces = line.split("\"")
		met = pieces[1]
		pieces = line.split(",")	
		#print met
		PUBCHEM = pieces[-1]
		HMDB = pieces[-2]
		KEGG = pieces[-3]
		ID = pieces[-4]
	
	
		met = strp(met)
		met = "\"" + met + "\""
		PUBCHEM = strp(PUBCHEM)
		HMDB = strp(HMDB)
		KEGG = strp(KEGG)
		ID = strp(ID)
		PUBCHEM = PUBCHEM + ","
		HMDB = HMDB + ","
		KEGG = KEGG + ","
			
		if met in dict.keys():
			#print "Matching metabolite found"
			#print met
			#print dict[met]
			replace = dict[met]
			#print ID
			#print dict[met]
			replace = "%s, %s, %s %s %s" % (replace, ID, KEGG, HMDB, PUBCHEM)
			print replace
			dict[met] = replace
			n = n + 1
		
handle2.close()
n1 = n1-n

#print ""
#for k, v in dict.items():
#	print k
#	print v
#print ""

print "Found %i matching metabolite IDs. Could not match the remaining %i, search for these manually. Sometimes metabolites with the same name have 2 different IDs, check that there are no extra IDs assigned to a name, determine which is correct manually" % (n, n1)



	
print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'Default'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "ChangingMetApp.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
#f.write("Significant changes for: ")
#f.write(name)
#f.write ("\n\n")
f.write("Metabolite, FC, P-value, FDR, Metabolon ID, KEGG, HMBD, PUBCHEM\n")
for keys, values in dict.items():
	f.write(keys)
	f.write(", ")
	f.write(values)
	f.write("\n")
f.write ("\n")
f.close()
print "Saved as:", savename	
	
