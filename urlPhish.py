import requests
import argparse

def maskUrl(url, mask, words):
	phishUrl = mask + '-' + words + '@' + url
	return phishUrl


def getUrl(url):
	response = requests.get('https://is.gd/create.php?format=simple&url=' + url)
	shortUrl = response.text
	shortUrl = shortUrl.replace("https://", "")
	return shortUrl

def Main():
	parser = argparse.ArgumentParser(description="Mask Phishing Urls")
	parser.add_argument("-u", "--url", help="specify phishing url")
	parser.add_argument("-m", "--mask", help="specify domain name to mask [https/http]")
	parser.add_argument("-w", "--words", help="specify words for social engineering ['-' between words]")
	args = parser.parse_args()

	url = args.url
	mask = args.mask
	words = args.words

	short = getUrl(url)
	mask = maskUrl(short, mask, words)

	print("\033[1;33;40m[!] Phishing Url: " + mask)

if __name__=="__main__":
	Main()
