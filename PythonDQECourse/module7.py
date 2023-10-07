# CSV parsing
#create the csv file
import csv
# with open ('moduletest.csv', 'w') as f:
#     f.write('Ismail,sajjad,pakistan,software engineer,kohat,25\n')
#     f.write('Mohammad,sajjad,pakistan,software engineer,kohat,28\n')
#     f.write('Bilal,sajjad,pakistan,software engineer,kohat,29\n')
#     f.write('Amin,sajjad,pakistan,software engineer,kohat,15\n')

#read the csv file

# with open ('moduletest.csv', 'r') as f:
#     result = f.read()
#     rows = result.split('\n')
#     for row in rows:
#         print(row.split(';'))
    # print(rows)

# Create file using CSV writer
csv.register_dialect('customize_dialect',quotechar="'", delimiter =";",quoting=csv.QUOTE_ALL)
print(csv.list_dialects()) #['excel', 'excel-tab', 'unix', 'customize_dialect']

with open ('writertest.csv', 'w', newline='') as f:
    headers =['Name','FName','Country','Role','City','Rank']
    test_write = csv.DictWriter(f,fieldnames=headers,quotechar="'", delimiter =";",quoting=csv.QUOTE_ALL)
    test_write.writeheader()
    test_write.writerow({'Name':'Ismail','FName':'sajjad','Country':'pakistan','Role':'software engineer','City':'kohat','Rank':'25,5'})
    test_write.writerow({'Name':'Sajid','FName':'tahir','Country':'pakistan','Role':'software engineer','City':'kohat','Rank':'65'})
    # test_write = csv.writer(f,'customize_dialect')
    print()
#using csv reader
# with open ('writertest.csv', 'r') as f:
#     result_reader = csv.reader(f, 'customize_dialect')
#     for row in result_reader:
#         print(row)
with open ('writertest.csv', 'r') as f:
    result_reader = csv.DictReader(f,quotechar="'", delimiter =";",quoting=csv.QUOTE_ALL)
    print(result_reader)
    for row in result_reader:
        print(row)
        print(f"name = {row['Name']},FName = {row['FName']},Country = {row['Country']},City = {row['City']},Rank = {row['Rank']}")

with open ('writertest.csv', 'r') as f:
    dialect_need = csv.Sniffer().sniff(f.read())
    print(dialect_need.delimiter)

