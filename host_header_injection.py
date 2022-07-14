# Lib imports.
import requests

# Important variables which might require changes.
HOST_HEADER_VALUE = "www.example.com"
# Put the CSV in the same folder as this script to avoid entering the entire path. This file is from https://github.com/cisagov/dotgov-data.
CSV_FILENAME = "current-full.csv"
# Burp proxy if debugging is needed.
proxies={"http":"http://127.0.0.1:8080"}

# Main code.
file_handler = open(CSV_FILENAME, "r")
for csv_lines in file_handler.readlines():
	hostname = csv_lines.split(",")[0].lower()
	try:
		HTTP_URL = f"http://{hostname}/"
		r = requests.get(HTTP_URL, headers={"Host":HOST_HEADER_VALUE}, timeout=2, allow_redirects=False)
		if (HOST_HEADER_VALUE[4:] in r.headers and "cloudflare" not in r.headers) or (HOST_HEADER_VALUE[4:] in r.text and "cloudflare" not in r.text):
			print(f"[+] Host header injection found at host: {hostname} for HTTP url: {HTTP_URL}.")
		HTTPS_URL = f"https://{hostname}/"
		r = requests.get(HTTPS_URL, headers={"Host":HOST_HEADER_VALUE}, timeout=2, allow_redirects=False)
		if (HOST_HEADER_VALUE[4:] in r.headers and "cloudflare" not in r.headers) or (HOST_HEADER_VALUE[4:] in r.text and "cloudflare" not in r.text):
			print(f"[+] Host header injection found at host: {hostname} for HTTPS url: {HTTPS_URL}.")
	except:
		pass

# Exiting.
file_handler.close()