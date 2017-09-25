from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        ##for i in range(1,n):
            ##if(attrs!=[]):
            ##    print(len(attrs))
            ##    for i in range(0,n):
        for j in range(0,len(attrs)):
            print("-> {} > {}".format(attrs[j][0],attrs[j][1]))
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
    
        
# instantiate the parser and fed it some HTML
n=int(input())
if(n>=0 and n<=100):
    parser = MyHTMLParser()
    for i in range(1,(n+1)):
        temp=input()
        parser.feed(temp)
<!-- Comments -->
