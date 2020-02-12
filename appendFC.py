#Strips spaces and returns clean string variables
def strp (var):
	var = var.strip(" ")
	var = var.strip("\n")
	var = "".join(var.split())
	return var

print " "
name = raw_input("Enter changing metbolite file file (enter for 'ChangingMetAppM.csv'): ")
if len(name) == 0 : name = "ChangingMetAppM.csv"
handle1 = open(name)
handle1.close()

dict = dict()

#Parse the Fold Change file and add to a dictionary
n1=0
handle1 = open(name)
for line in handle1:
		pieces = line.split(",")
		ID = pieces[-2]
		info = pieces[-7] + "," + pieces[-6] + "," + pieces[-5] + ","
		ID = strp(ID)
		if ID == "":
			ID = "no HMDB ID"
		info = strp(info)
		dict[ID] = (info)
		n1 = n1 + 1
handle1.close()




for keys, values in dict.items():
	print keys
	print values

print " "
name = raw_input("Enter masterlist of metabolites file (enter for 'tables.csv'): ")
if len(name) == 0 : name = "tables.csv"
handle2 = open(name)
handle2.close()

#Parse the second file for significance valuse, and replace dictionary 
#with new string of 3 values for matching keys.
n = 0
l = []
handle2 = open(name)
for line in handle2:
	pieces = line.split(",")
	met = pieces[-1]
	met = strp(met)
	print met
	if met in dict.keys():
		replace = dict[met]
		print "yes"
	else:
		print "no"
		replace =  ""
	line = strp(line)
	replace = line + "," +replace
	l.append(replace)
	n = n + 1
handle2.close()
n1 = n1-n

print ""
for lines in l:
	print lines

print "Found %i matching metabolite IDs. Could not match the remaining %i, search for these manually. Sometimes metabolites with the same name have 2 different IDs, check that there are no extra IDs assigned to a name, determine which is correct manually" % (n, n1)



	
print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'Default'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "tablesOUT.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
#f.write("Significant changes for: ")
#f.write(name)
#f.write ("\n\n")
f.write("Metabolite, HMBD, FC, P-value, FDR,\n")
for lines in l:
	f.write(lines)
	f.write("\n")
f.close()
print "Saved as:", savename	
	
