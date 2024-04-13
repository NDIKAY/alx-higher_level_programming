#!/usr/bin/python3

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    # Using a with statement to open the URL
    with urllib.request.urlopen(url) as response:
        # Read the response
        content = response.read()
        
        # Convert content to utf-8
        utf8_content = content.decode("utf-8")
        
        # Displaying the results as specified
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf8_content))

