#If we have a broadband internet connection, a single-threaded program cannot fully utilize the available bandwidth.So using multiple threads we can get 
#the downloads faster , thus creating a more optimised program for our needs.

import bs4,webbrowser,requests,os
import threading

#url='https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    #while not url.endswith('#'):
    for urlNumber in range(startComic, endComic):
        print('downloading page %s...' % urlNumber)
        res=requests.get('https://xkcd.com//%s' %urlNumber)
        res.raise_for_status()

        soup =bs4.BeautifulSoup(res.text, 'html.parser')
        comicElem=soup.select('#comic img')
        if comicElem == []:
            print('could not find comic image')
        else:
            comicUrl='https:' + comicElem[0].get('src')

            print('Downloading image %s...' %comicUrl )
            res =requests.get(comicUrl)
            res.raise_for_status()

            imageFile =open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        prevLink =soup.select('a[rel="prev"]')[0]
        url='https://xkcd.com' + prevLink.get('href')

    print('YOu succesfully finished downloading!!')

download_threads = [ ]
for i in range(0,140,10):
    start=i
    end=i+9
    if start==0:
        start=1

    downloadthread=threading.Thread(target=downloadXkcd, args=(start, end))
    download_threads.append(downloadthread)
    downloadthread.start()

for download_threads in downloadthread:
    download_threads.join()
print('Done.')
