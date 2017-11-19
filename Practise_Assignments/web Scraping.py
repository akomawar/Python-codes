import re, urllib
try:
    import urllib.request
except:
    pass

sites='google yahoo msn cnn'.split()
post=re.compile(r'<title>+.*</title>+',re.I|re.M)

for i in sites:
    print('Searcing {}'.format(i))
    try:
        a=urllib.urlopen('https://'+i+'.com')
    except:
        a=urllib.request.urlopen('https://'+i+'.com')

    text=a.read()
    title=re.findall(post,str(text))

    print(title[0])
