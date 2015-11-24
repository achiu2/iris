import google, urllib2, re, bs4

def searchWho(query): 
    pattern = "[A-Z][a-z]{3,15} [A-Z][a-z]+"
    results = google.search(query, num=10, start=0, stop=10)
    rlist = []
    for url in results: 
        print url
        try: 
            request = urllib2.urlopen(url)
            result = request.read()
            soup = bs4.BeautifulSoup(result, "html.parser")
            raw = soup.get_text()
            pretty = re.sub("[ \t\n]+", " ",raw)
            entries = re.findall(pattern, pretty)
            rlist.append(entries)
        except: 
            print "Error. Request could not be processed."
    return mostCommon(rlist)

def mostCommon(list):
    return max(list)
