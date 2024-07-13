import webbrowser
chat = True
helloIntent = ["hello","hey","hi","wassup","hie"]
while chat==True:
    msg = input("Enter msg : ").lower()
    if msg in helloIntent:
        print("Hi...")
    elif msg =="bye":
        print("tata....")
        chat = False
    elif msg.startswith("open"):
        webbrowser.open("https://www."+msg.split()[-1]+".com")
        
    else:
        print("Sorry I dont Understand")
