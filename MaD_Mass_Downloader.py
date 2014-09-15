'''   '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''


+               +                     + + + + +
+ +           + +      + + + +        +         +
+   +       +   +    +         +      +          +
+     +   +     +   +           +     +           +
+       +       +   +           +     +            +
+               +   +           +     +             +
+               +   +           +     +            + 
+               +   +           +     +           +
+               +    +         + +    +          + 
+               +     + + + + +   +   + + + + + +          


### Mass Downloader - For Linux ###

Coded By : mK


'''######################################################

from bs4 import BeautifulSoup
from pySmartDL import SmartDL , utils
import urllib.request
#from urllib.request import Request, urlopen
import re
import os



''' For Download Audios -
Function To Find Audio Links and
Download those links
'''

def audios(link):
    print("Enter the Minimum size of file to be downloaded\n")
    size = input('> ')
    size = int(size)

    url = urllib.request.urlopen(link)
    content = url.read()
    soup = BeautifulSoup(content)
    links = [a['href'] for a in soup.find_all('a',href=re.compile('http.*\.(mp3|wav|ogg|wma|flac)'))]
    print (str(len(links)) + " Images Found ")
   # print (links)
    print("\n".join(links))


  
   
#For Downloading
    dest = "C:\\Downloads\\" # or '~/Downloads/' on linux
    for i in range(len(links)):
        #a_link = urllib.request.Request(links[i])
        #a_link2 = int(round((links[i].length / 1024),2)) / 1024
        #req = urllib.request.Request(a_link, method='HEAD')
        #resp = urllib.request.urlopen(req)
        #resp = urllib.request.urlopen(a_link)
        #size = int(resp.headers['Content-Length'])
        #size = int(a_link.length)
        #a_link2 = urllib.request.urlopen(a_link)
        #site = urllib.request.urlopen(a_link)
        #size2 = int((a_link.length / 1024) / 1024)

        a_link = links[i]
        fix_link = utils.url_fix(a_link)
        b =(utils.get_filesize(fix_link, timeout=15))


        print (utils.sizeof_human(b))
        #if size >= b:
        obj = SmartDL(fix_link, dest)
        obj.start()

        path = obj.get_dest()
        #else:
         #   print("\n")



#######################################################################

''' For Download Videos -
Function To Find Video Links and
Download those links
'''


def videos(link):
    url = urllib.request.urlopen(link)
    content = url.read()
    soup = BeautifulSoup(content)
    links = [a['href'] for a in soup.find_all('a',href=re.compile('http.*\.mp4'))]
    print (str(len(links)) + " Videos Found ")
   # print (links)
    print("\n".join(links))


######################################################################



''' For Downloading Images -
Function To Find Image Links and
Download those links
'''


def images(link):

    print("Enter the Minimum size of file to be downloaded\n")
    u_size = input('> ')
    u_size = int(u_size)
    
    url = urllib.request.urlopen(link)
    #link = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    content = url.read()
    soup = BeautifulSoup(content)
    links = [a['href'] for a in soup.find_all('a',href=re.compile('http.*\.(jpg|JPG|png|gif|bmp|tiff)'))]
    print (str(len(links)) + " Images Found ")
   # print (links)
    print("\n".join(links))

    dest = "C:\\Downloads\\" # or '~/Downloads/' on linux
    
    for i in range(len(links)):
        a_link = links[i]
        fix_link = utils.url_fix(a_link)
        #b =(utils.get_filesize(fix_link, timeout=200000))
        b =(utils.get_filesize(fix_link))
        print (utils.sizeof_human(b))

        c_size =(utils.get_filesize(fix_link, timeout=15))
        c_size = (b / 1024)

        #print (round(c_size,2))
        
        
        
        if u_size <= c_size:
            obj = SmartDL(fix_link, dest)
            obj.start()

            path = obj.get_dest()

    main();
  
def main():

    print("""

    +               +                     + + + + +
    + +           + +      + + + +        +         +
    +   +       +   +    +         +      +          +
    +     +   +     +   +           +     +           +
    +       +       +   +           +     +            +
    +               +   +           +     +             +
    +               +   +           +     +            + 
    +               +   +           +     +           +
    +               +    +         + +    +          + 
    +               +     + + + + +   +   + + + + + +          


    ### Mass Downloader - For Linux {Not Just Another CommandLine} ###

    Coded By : mK

    """)


    print(" #################################################################### ")
    print(" #                                                                  # ")
    print(" #                  Select Your Choice                              # ")
    print(" #                                                                  # ")
    print("   1 . Audios (Mp3,Wav,Ogg,Wma,flac,Oga etc)                         ")
    print("   2 . Images (Jpg,Png,Gif etc)                                      ")
    print("   3 . Videos (Mp4,Wmv,Flv etc)                                      ")
    print("   4 . Documents (PDF,Doc,Xls,etc)                                   ")
    print("   5 . User Defined                                                  ")
    print(" \n #################################################################### ")
    choice = input()

    
    print("Enter the link \n")
    link = input()


    if choice == '1':
        audios(link);
    elif choice == '2':
        images(link);
    elif choice == '3':
        videos(link);
    elif choice == '4':
        user_def(link)
#else:
  #  return false;



main();
