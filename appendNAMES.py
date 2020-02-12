#Strips spaces and returns clean string variables
def strp (var):
	#var = var.strip(" ")
	var = var.strip("\n")
	var = "".join(var.split())
	return var

print " "
name = raw_input("Enter file to switch out metabolites names (Enter for 'ChangingMetApp.csv'): ")
if len(name) == 0 : name = "ChangingMetApp.csv"
handle1 = open(name)
handle1.close()

dict = dict()

#Parse the first Fold Change file and add to a dictionary
n1=0
handle1 = open(name)
handle1.readline()
for line in handle1:
	line = line[:-5]
	pieces = line.split(",")
	ID = pieces[-4]
	ID = strp(ID)
	#line = strp(line)
	ID = strp(ID)
	dict[ID] = (line)
	n1 = n1 + 1
handle1.close()

for keys, values in dict.items():
	print keys
	print values
	
print " "
name = raw_input("Enter masterlist of metabolites file (enter for 'NRmet.csv'): ")
if len(name) == 0 : name = "NRmet.csv"
handle2 = open(name)
handle2.close()

#Parse the second file for significance valuse, and replace dictionary 
#with new string of 3 values for matching keys.
n2 = 0
handle2 = open(name)
handle2.readline()
for line in handle2:
	pieces = line.split(",")
	try:
		ID = pieces[-4]
		pieces = line.split("\"")
		met = pieces[1]
		#met = strp(met)
		met = "\"" + met + "\""
		ID = strp(ID)
	except:
		ID = "fail"
	ID = strp(ID)
	print ID
	
	if ID in dict.keys():
		print "yes"
		replace = dict[ID]
		pieces = replace.split(",")
		replace = "%s, %s, %s, %s, %s, %s, %s" % (pieces[-7], pieces[-6],pieces[-5],pieces[-4], pieces[-3], pieces[-2], pieces[-1])
		replace = strp(replace)
		replace = "*%s, %s" % (met, replace)
		dict[ID] = replace
	else:
		print "no"
		
handle2.close()

for key, value in dict.items():
	if value [:1] == "*":
		print "got it"
		replace = value[1:]
		dict[key] = replace
	else:
		replace = "\"" + "***" + value[0:]
		dict[key] = replace
		n2 = n2 + 1

print ""
for k, v in dict.items():
	print v
print ""

print "Of the %i metabolites in ChangingMetApp.csv replaced all except %i that are marked with  *** for manual replacement." % (n1, n2)



	
print " "	
savename = raw_input("Save as (Blank to exit without saving, Enter d for 'Default'): ")
if len(savename) == 0: quit()
if savename == "d": savename = "ChangingMetAppM.csv"
else: savename = savename + ".csv"
f = open(savename,'w')
#f.write("Significant changes for: ")
#f.write(name)
#f.write ("\n\n")
f.write("Metabolite, FC, P-value, FDR, Metabolon ID, KEGG, HMBD, PUBCHEM\n")
for keys, values in dict.items():
	f.write(values)
	f.write("\n")
f.close()
print "Saved as:", savename	
	
