# File Name: webcrawler_test
# Application: Web Crawler 
# Created by: Abemelech Mesfin Belachew
# Date: 4/2/2022
# Description for the file: Test the webcrawler_main (class WebCrawler)

# Import the file and sys to access terminal input
import webcrawler_main
import sys

# The function to test the webcrawler
def main():

    # Take user input
    try:
        user_input = sys.argv[1]
        webcrawler_main.WebCrawler(user_input)
    except:
        print("Unexpected Crash: Potential Cause - Invalid URL or Null URL")

main()