def isleapyear(year):
  if (year % 4 == 0):
    return True
  else:
    return False


year = int(input("enter a leap:"))
if isleapyear(year):
  print("{} is a leap year.".format(year))
else:
  print("{} is not a leap year.".format(year))
