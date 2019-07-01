import os
class QueryInfo:
    def __init__(self,title,ViewCt,AnsCt,FavCt):
        self.title = title
        self.ViewCt = ViewCt
        self.AnsCt = AnsCt
        self.FavCt = FavCt
        
    def titlePrint(self):
        print(self.title)
    def PrintObj(self):
        print(self)