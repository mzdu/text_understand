import csv
import re

f = open('newsSpace', 'rb')
output = open('data.csv', 'wb')
writer = csv.writer(output)

allData = f.read()
allData = re.split(r'\\N', allData)


writer.writerow(['title','description','category'])
for data in allData:
    tmp = ''.join(re.split(r'[\n,\\]+', data))
    tmp = re.split(r'[\t]+', tmp)
    try:
        writer.writerow([tmp[2],tmp[5],tmp[4]])
    except:
        pass

f.close()
output.close()
