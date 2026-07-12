class Human:
    def _init__(self,n,o):
        self.name = n
        self.occupation = o
    def do_work(self):
        if self.occupation == "tennis palyer":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots film")
    def speaks(self):
        print(self.name,"says how are you?")
# tom = Human("tom cruise","actor")
# tom.do.work()
# tom.speaks()