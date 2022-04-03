# WebCrawler
Web Crawler parses through websites and collects the urls inside a single url and continuously loops inside the collected urls to collect more urls

The Webcrawler application fetchs the HTML document from the URL, Parse out the URLs in the HTML Document, Logs the URL visted and the parsed URL on the consol and Loops back into the new URLs. 

## How to install all the dependencies
1. python3 -m pip install requests
2. python3 -m pip install bs4 

## How to Build/Run the script
1. python3 webcrawler_test.py "Any website url (https,http included)"


## How to Run the test
1. python3 webcrawler_test.py "https://rescale.com/"

webcrawler_main contains a class named WebCrawler with an initalizing argument of the URL

    WebCrawler("the https url")

