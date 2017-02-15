import urllib.request
from bs4 import BeautifulSoup

results = [ ["Name","Roll","Cgpa"]]

for i in range(1,73):
	roll = str(i)
	if i < 10:
		roll = "0" + str(i)
	else:
		roll = str(i) 
	url = "http://www.juexam.org/newexam/show_result.asp?f1=ITE1640"+ roll + "&f2=E3ITE1622R"
	f = urllib.request.urlopen(url).read()
	beauty = BeautifulSoup(f,'html.parser')
	alltable = beauty.select('table')
	if (len(alltable)==1):
		continue;

	name_table = alltable[2]
	cgpa_table = alltable[5]

	columns = BeautifulSoup(str(name_table.contents),'html.parser').select('td')
	name = columns[6].text
	rollno = columns[11].text

	columns = BeautifulSoup(str(cgpa_table.contents),'html.parser').select('td')
	cgpa = columns[1].text.strip().split(" ")
	if len(cgpa) > 2:
		cgpa = cgpa[2]
	else:
		cgpa = "---"
	result = [name,rollno,cgpa]
	print(result)
	results.append(result)

f = open('result.txt','w')
for result in results:
	f.write("".join(str(x).ljust(30) for x in result))
	f.write("\n")
f.close()