import requests
from bs4 import BeautifulSoup

subject = 'Computer Science'
topic = 'algorithms'
subtopic = 'graphs'

edx_link = 'https://www.edx.org/course?search_query=' + topic.replace(' ','+')
crs_link = 'https://www.coursera.org/courses?languages=en&query=' + topic.replace(' ','+')
npt_link = 'https://www.youtube.com/user/nptelhrd/search?query=' + topic.replace(' ','+')
tnb_link = 'https://www.youtube.com/user/thenewboston/search?query=' + topic.replace(' ','+')

ud_link = 'https://www.udacity.com/courses/all'
mit_link = 'http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/'
goog_link = 'https://www.google.co.in/about/careers/students/guide-to-technical-development.html'


if(subtopic==''):
	npt_link = npt_link + '+playlist'
	tnb_link = tnb_link + '+playlist'
else:
	npt_link = npt_link + '+' + subtopic.replace(' ','+')
	tnb_link = tnb_link + '+' + subtopic.replace(' ','+')
	
	
def nptel_course(topic, subtopic):
	source_code = requests.get(npt_link)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,'html.parser')
	count1=0

	for course in soup.findAll('a',{'class':'yt-uix-sessionlink'}):
		link = 'https://www.youtube.com' + course.get('href')
		if(subtopic==''):
			if '/playlist?' in link and link2 != link:
				count1+=1
				print link
			if (count1==3):
				break	
		else:
			if not '/playlist?' in link and not '&list=' in link and '/watch?v=' in link and link2 != link:
				count1+=1
				print link
			if (count1==5):
				break	
		link2 = link


def mit_course(topic):
	source_code = requests.get(mit_link)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,'html.parser')
	count=0

	for course in soup.findAll('a',{'class':'preview'}):
		link = 'http://ocw.mit.edu/' + course.get('href')
		title = course.string
		if topic.title() in title:
			count+=1
			title = title.replace('\n ','')
			print title.replace('  ','')+'\n'+link
		if count==5:
			break
			

def google_course(topic):
	source_code = requests.get(goog_link)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,'html.parser')
	count=0
	
	for course in soup.findAll('a'):
		link = course.get('href')
		title = course.string
		if title and topic.title() in title:
			count+=1
			title = title.replace('\n','')
			print title.replace('  ','')+'\n'+link
		if count==5:
			break
	
google_course(topic)
	

