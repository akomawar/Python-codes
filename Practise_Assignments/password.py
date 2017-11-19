username1='akomawar'
password1='ankit'

for i in range(1,4):
    username=input("Please Enter your Username: ")
    password=input("Please Enter your Password: ")
    j=3
    
    if(username==username1 and password==password1):
        print("Succesfully looged in by: ",username)
        break
    
    else:
        print("Please check your username and password")
        print("Number of attempts left: ",j-i)
        continue
    print("Please try again later")
        
