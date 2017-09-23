from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import math


class URLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]

    # This is a function to get all the <a> tag links in a webpage

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        try:
            response = urlopen(url)
        except Exception as e:
            print('URLException: ', e)
            return []

        # Make sure that we are looking at HTML and not other things
        # (such as JavaScript files, CSS, or .PDFs for example).

        info = response.info()
        if info.get_content_type() == 'text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")

            # Refer
            # https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser.feed

            self.feed(htmlString)
            return self.links
        else:
            return []


# Spider to crawl the given URl, It takes in an URL and the number of
# pages to search through.

def spider(url, maxPages=None):
    pagesToVisit = [url]
    numberVisited = 0

    if maxPages is None:
        maxPages = math.inf

    while numberVisited < maxPages and pagesToVisit != []:
        numberVisited = numberVisited + 1

        url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        try:
            print(numberVisited, "Crawling:", url)
            parser = URLParser()
            links = parser.getLinks(url)

            # Avoid link duplication

            pagesToVisit = pagesToVisit + list(set(links) - set(pagesToVisit))
            print("Crawling success")
        except Exception as e:
            print("Crawling Failed: ", e)
