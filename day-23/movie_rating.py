class movie:
    def __init__(self,title,music,rating):
        self.title=title
        self.music=music
        self.rating=rating
    def is_good_kids(self):
        return self.rating<13
m1=movie("super","good",8)
print("goodforkids:m1.is_good_kids()")
