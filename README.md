# urlPhish
Mask Phishing Urls
```
╱╱╱╱╱╭╮╭━━━┳╮╱╱╱╱╱╭╮
╱╱╱╱╱┃┃┃╭━╮┃┃╱╱╱╱╱┃┃
╭╮╭┳━┫┃┃╰━╯┃╰━┳┳━━┫╰━╮
┃┃┃┃╭┫┃┃╭━━┫╭╮┣┫━━┫╭╮┃
┃╰╯┃┃┃╰┫┃╱╱┃┃┃┃┣━━┃┃┃┃
╰━━┻╯╰━┻╯╱╱╰╯╰┻┻━━┻╯╰╯
```
* this tool is inspired by MaskPhish simply written in Python
   - https://github.com/jaykali

# Prerequisite
```
$ pip3 install -r requirements.txt
```

# Usage
```
usage: urlPhish.py [-h] [-u URL] [-m MASK]
                   [-w WORDS]

Mask Phishing Urls

optional arguments:
  -h, --help            show this help message
                        and exit
  -u URL, --url URL     specify phishing url
  -m MASK, --mask MASK  specify domain name to
                        mask [https/http]
  -w WORDS, --words WORDS
                        specify words for
                        social engineering ['-'
                        between words]

```

* Example
```
$ python3 urlPhish.py -u <phishing_url> -m https://google.com -w account-login
```


