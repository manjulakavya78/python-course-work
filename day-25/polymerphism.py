class hotstar:
    def __init__(self,name,phnno):
        self.name=name
        self.phnno=phnno
        print(f"welcome to the jio hotstar,{self.name}")
    def dashboard(self):
        print("-----Dashboard Displayed-----")
    def search(self):
        print("you can search for content")
    def history(self):
        print("you can checkout your history")
    def quality(self):
        print("video quality-720")
    def audio(self):
        print("stereo-audio setting")
    def ads(self):
        print("ads will run")
    def access(self):
        print("you have limited content access")
    def login(self):
        print("you can login to the single device")
class premiumhotstar(hotstar):
    def __init__(self,name,phnno):
        self.name=name
        self.phnno=phnno
        print(f"welcome to the jio premium hotstar,{self.name}")
    def quality(self):
        print("video quality-1080")
    def audio(self):
        print("Dolly-audio setting")
    def ads(self):
        print("ads will not run")
    def access(self):
        print("you have unlimited content ")
    def login(self):
        print("you can login to the 2-3 device")
manoj=hotstar("manoj",9876543210)
manoj.dashboard()
manoj.search()
manoj.history()
manoj.quality()
manoj.audio()
manoj.ads()
manoj.access()
manoj.login()



aamid=premiumhotstar("aamid",9876543201)
aamid.dashboard()
aamid.search()
aamid.history()
aamid.quality()
aamid.audio()
aamid.ads()
aamid.access()
aamid.login()
        
