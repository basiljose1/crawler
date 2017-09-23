# crawler

A crawler is a program that starts with a url on the web (ex: http://python.org), fetches the web-page corresponding to that url, and parses all the links on that page into a repository of links. Next, it fetches the contents of any of the url from the repository just created, parses the links from this new content into the repository and continues this process for all links in the repository until stopped or after a given number of links are fetched.


#### How to execute ####

1. Clone the git repository https://github.com/basiljose1/crawler
2. cd crawler
3. python3
4. In python shell , 

> from spider import spider

> spider('url','maxPages')

url -> initial URL
maxPages -> no of page to crawel (pass only if want to limit)

if no 'maxPages' is passing to spider(), it will continues crawling for all the links in the repository

