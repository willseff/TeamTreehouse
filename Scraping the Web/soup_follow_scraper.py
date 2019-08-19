from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

def internal_links(linkURL):
	html = urlopen('https://treehouse-projects.github.io/horse-land/[]'.format(linkURL))
	soup = BeautifulSoup(html,'html.parser')

	return soup.find('a', href=re.compile('(.html)$'))