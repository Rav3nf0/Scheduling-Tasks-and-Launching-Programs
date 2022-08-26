from fileinput import filename
import bs4,time,requests,os

os.makedirs('comics', exist_ok=True)
#==========================================================================
def xkcd_comics():
    url='https://xkcd.com'
    
    print('downloading page %s...' % url)
    res=requests.get(url)
    res.raise_for_status()

    soup =bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem=soup.select('#comic img')
    comicUrl='https:' + comicElem[0].get('src')
             
    if comicElem == []:
        print('Could not find comic element at %s.' %url)
    else:
        check_updates(comicUrl)
 #==========================================================================       
def check_updates(comicUrl):
    filename =os.path.basename(comicUrl)
    
    #checks if the comic has already been downloaded inside the comics folder.
    if filename in os.listdir('comics'):
        print('Nothing new today,latest comic is %s' %comicUrl)
    else:
        res =requests.get(comicUrl)
        res.raise_for_status()
        print('Downloading image %s...' %comicUrl )
        imageFile =open(os.path.join('comics', filename),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        print('YOu succesfully finished downloading!!') 

#here we want to schedule the program to run every 24 hours.
        for second in range(84600):#84600 seconds is 24 hours 
            time.sleep(1)
#============================================================================
for hour in range(7): #since in a week there are 7 days , each day being 24 hours.
    print('Searching for new comic')
    xkcd_comics() 