#!/usr/bin/python3


#write a program to pracrtice webscraping


import requests , os, bs4


url = "http://xkcd.com"

os.makedirs("/media/mcbeeff/D/Secondary/xkcd", exist_ok=True) # store the comics in a directory, check if directory exists condition

while not url.endswith('#'):

    print('Downloading page %s...' %url)
    res = requests.get("http://xkcd.com")
    res.raise_for_status() # throws out an exception and end the program if something goes wrong
    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        print('Downloading image %s....' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        #Saves the file
        imageFile = open(os.path.join('/media/mcbeeff/D/Secondary/xkcd/', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):  # at most 100000 bytes of data
            imageFile.write(chunk)
        imageFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')




print('Done')
