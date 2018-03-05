import requests
from bs4 import BeautifulSoup


class theGuardian :

	def returnHeadlines(self,noOfHeadlines=12):
		self.headlineList=[]
		r=requests.get("https://www.theguardian.com/us")
		self.soup=BeautifulSoup(r.content,'html.parser')
		self.soup=self.soup.find('section',id="headlines")
		self.headlines=self.soup.find_all(class_="fc-item__title")
		for headline,j in zip(self.headlines,range(noOfHeadlines)):
			self.headlineList.append("")
			self.headlineList[j]=""
			a=headline.find_all(class_="js-headline-text")
			try:
				for i in a:
					print (i.string)
					self.headlineList[j]+=i.string

			except:
				j=j-1;
				self.headlineList.pop()
				continue
			print ("\n")

		print self.headlineList

a=theGuardian()
a.returnHeadlines()
