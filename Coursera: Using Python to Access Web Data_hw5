




def scan_op_url(position, count, link):
    # To run this, download the BeautifulSoup zip file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    lst = []
    count = 0
    while count < y:

        url = link
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
        tags = soup('a')
        for tag in tags:
            words = tag.get('href', None)
            lst.append(words)
        count += 1
        newlink = lst[x-1]
        print(newlink)
        url =newlink

        return url

x = int(input('Enter position:'))
y = int(input('Enter count:'))
z = input('Enter url:')
print(z)

a = scan_op_url(x,y,z)
b= scan_op_url(x,y,a)
c = scan_op_url(x,y,b)
d= scan_op_url(x,y,c)
e = scan_op_url(x,y,d)
f = scan_op_url(x,y,e)
g = scan_op_url(x,y,f)







"""
    count = 0
    while count != y:
        finallst.append(url)
        newurl = lst[x-1]
        finallst.append(newurl)

        count +=1
        if count == y:
            break
"""

"""
_link = urllib.request.urlopen(newurl, context=ctx).read()
newsoup = BeautifulSoup(_link, 'html.parser')
newtags = newsoup('a')

newlst = []
newlst.append(url)
for newtag in newtags:
    line = newtag.get('href', None)
    newlst.append(line)
"""





"""
newurl = lst[x]
_link = urllib.request.urlopen(newurl, context=ctx).read()
newsoup = BeautifulSoup(_link, 'html.parser')
newtags = newsoup('a')

counting = 1
newlst = []
for newtag in newtags:
    line = newtag.get('href', None)
    newlst.append(line)
    counting +=1
    if counting == y:
        break
"""
