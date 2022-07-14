# Host-header-injection-checker
A simple python script to detect host header injections for both HTTP/HTTPS hostnames from a csv database.

Few explanations are available on the comments in the python file. Basically run the python file with the provided CSV in the same directory and it will start telling the vulnerable hosts along with them using HTTP/HTTPS and their URLs. It might look stuck at first but it only outputs when it finds a vulnerable hostname, so be patient. Further, I have taken the CSV from https://github.com/cisagov/dotgov-data and cut it down for demonstration only. Feel free to edit the script as it might require changes if the CSV format is to be changed...

Oh and I have included a check for detecting cloudflare in the response, which will always output the payload host header value, thus making the host itself not vulnerable. Feel free to include any other WAFs too!
