import webbrowser

CVEname = input("What is the CVE?")

# For testing use CVE-2021-44228

webbrowser.open((https://www.tenable.com/cve/ + CVEname), new=2)

webbrowser.open((https://nvd.nist.gov/vuln/detail/ + CVEname), new=2)

webbrowser.open((https://cve.mitre.org/cgi-bin/cvename.cgi?name= + CVEname), new=2)
