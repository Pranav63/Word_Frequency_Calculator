import requests 
import operator 
from bs4 import BeautifulSoup 

# Gets the data from the website , example it gets the cream stuff , as the data of the hyperlink excluding all the crap
def start(url):
	word_list=[]
	source=requests.get(url).text
	soup=BeautifulSoup(source)
	for links in soup.findAll('a',{'class':'dropdown-item'}):
		content=links.string
		words=content.lower().split()  # Count each word by word 
		for single_word in words:
			word_list.append(single_word)
	clean_list(word_list)
	
# It cleans the word list by tremoving any special characters along with words like ok.. or ;) something like it 
def clean_list(word_list):
	clean_word_list=[]
	for words in word_list:
		symbols="!@#$%^&*()_+{}|\".,';][\=-:><?"	
		for i in range(0,len(symbols)):
			words=words.replace(symbols[i],"")    # replace special characters with "" blank space 
		if len(words)>0:
			clean_word_list.append(words)
			dictionary(clean_word_list)
# Dictinonary with the count of each word 

def dictionary(clean_word_list):
	word_count={}
	for word in clean_word_list:
		if word in word_count:
			word_count[word]+=1
		else:
			word_count[word]=1
	for key, value in sorted(word_count.items(),key=operator.itemgetter(0)):
		print(key ,value)
			

start("https://github.com/Pranav63")			