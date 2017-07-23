import time
def inOneNumber(numbers):
 numbers = str(numbers)
 result = 0
 for num in numbers:
  result = int(result) + int(num)
  result = str(result)
  count = len(str(result))
  #print result
 while count > 1:
   tmp = 0
   for res in result:
    tmp = tmp + int(res)
   result = tmp
   count = len(str(result))
 return int(result)

def Equal(number,equal):
 while inOneNumber(number) == equal:
  number = str(number)
  strnga = ""
  for n in number:
   strnga = strnga + str(n) + "+"
  tmp = inOneNumber(number)
  strnga = strnga[:len(strnga)-1]
  strnga = strnga + "=" + str(tmp)
  print strnga
  number = int(number)
  number = number+tmp
  time.sleep(0.5)
 return number

Answer = Equal(666,9)
print "Answer?: :)  "+ str(Answer)
