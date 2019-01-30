import csv


with open("csvfile.csv","wb") as csvfile:
	csvwriter = csv.writer(csvfile,delimiter =',', quoting =csv.QUOTE_MINIMAL)
	csvwriter.writerow(['John smith','Accounting'])
	csvwriter.writerow(['erica meyers','it'])
