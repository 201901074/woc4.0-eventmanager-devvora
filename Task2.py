#Task2
from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
  url = input("Enter url of the website whose text you want to scrape!")
  html = urlopen(url).read()
  soup = BeautifulSoup(html, features="html.parser")

  # kill all script and style elements
  for script in soup(["script", "style"]):
      script.extract()    # rip it out

  # get text
  text = soup.get_text()

  # break into lines and remove leading and trailing space on each
  lines = (line.strip() for line in text.splitlines())
  # break multi-headlines into a line each
  chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
  # drop blank lines
  text = '\n'.join(chunk for chunk in chunks if chunk)

  file = open('text_file','w')
  for each in text:
    file.write(each)
  file.close();

  file = open('text_file','r')
  for each in file:
    print(each)

except:
  print("Invalid URL")

text = input("Please add some data to append!")

file = open('text_file','a')
for each in text:
  file.write(each)
file.close();

file = open('text_file','r')
for each in file:
  print(each)

  
