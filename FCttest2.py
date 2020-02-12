#Strips spaces and returns clean string variables
def strp (var):
	var = var.strip(" ")
	var = var.strip("\n")
	return var

print " "
name = raw_input("Enter 'Fold Change' file (enter for 'fold_change.csv'): ")
if len(name) == 0 : name = "fold_change.csv"
handle1 = open(name)
handle1.close()

dict = dict()

#Parse the first Fold Change file and add to a dictionary
n=0
handle1 = open(name)
handle1.readline()
for line in handle1:
	met = ""
	if line[:1] == "\"":
		pieces = line.split("\"")
		met = pieces[1]
		pieces = line.split(",")	
	else:
		npieces = line.count(",")
		pieces = line.split(",")
		for i in xrange(0, npieces -2):
			met = met + pieces[i]
			
	met = strp(met)
	met = "\"" + met + "\""
	FC = pieces[-2]
	FC = strp(FC)
	
	dict[met] = (FC)
	n = n + 1
handle1.close()

for keys, values in dict.items():
	print keys
	print values

print " "
name = raw_input("Enter 'P Values' file (enter for 't_test.csv'): ")
if len(name) == 0 : name = "t_test.csv"
handle2 = open(name)
handle2.close()

#Parse the second file for significance valuse, and replace dictionary 
#with new string of 3 values for matching keys.
n=0
handle2 = open(name)
handle2.readline()
for line in handle2:
		
	met = ""
	if line[:1] == "\"":
		pieces = line.split("\"")
		met = pieces[1]
		pieces = line.split(",")	
	else:
		npieces = line.count(",")
		pieces = line.split(",")
		for i in xrange(0, npieces -2):
			met = met + pieces[i]
		print met
	
	P = pieces[-3]
	FDR = pieces [-1]
	
	met = strp(met)
	met = "\"" + met + "\""
	P = strp(P)
	FDR = strp(FDR)
	
	
	if met in dict.keys():
		print "Matching metabolite found"
		replace = dict[met]
		replace = "%s, %s, %s" % (replace, P, FDR)
		dict[met] = replace
	
	n = n + 1
handle2.close()

#for i in dict:
#	print i
	

	

#Identify which keys were not updated with P and FDR and delete those entries
dellist = []
for key, values in dict.items():
	pieces = values.split(",")
	try:
		test = pieces[2]
	except:
		dellist.append(key)
		
for i in dellist:
	del dict[i]

print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'Default'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "ChangingMet.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
#f.write("Significant changes for: ")
#f.write(name)
#f.write ("\n\n")
f.write("Metabolite, FC, P-value, FDR\n")
for keys, values in dict.items():
	f.write(keys)
	f.write(", ")
	f.write(values)
	f.write("\n")
f.write ("\n")
f.close()
print "Saved as:", savename	
	
