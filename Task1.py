#Task1

!pip install countryinfo

from countryinfo import CountryInfo

country  = input ("Enter any country whose capital you want to find out! ")

try:
  capital = CountryInfo(country).capital()
  print(capital)
except:
  print("Not a valid country")
