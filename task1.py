# task 1
import re

#reading data
f = open('onelinefile.txt', 'r')
data = f.read()
f.close()


# regular expression pattern containing patterns for integer, string and float in different groups enclosed by parenthesis
pattern = "([0-9]+)([a-zA-Z]+)([-+]?[0-9]*\.?[0-9]*)([a-zA-Z]+)"


# splitting the text into list of tuple of int string float string format
splitted_data = re.findall(pattern,data)


#writing data
f = open("task1Output.csv","w")
n = len(splitted_data)

for i in range(n):
  x = splitted_data[i]
  if (i == n-1):
    f.write(x[0]+","+x[1]+","+x[2]+","+x[3])
  else:
    f.write(x[0]+","+x[1]+","+x[2]+","+x[3]+"\n")

f.close()