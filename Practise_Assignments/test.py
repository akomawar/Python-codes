from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        for j in range(0,len(attrs)):
            print("-> {} > {}".format(attrs[j][0],attrs[j][1]))

n=int(input())
if(n>0 and n<100):
    parser=MyHTMLParser()
    for i in range(1,(n+1)):
        temp=input()
        parser.feed(temp)
