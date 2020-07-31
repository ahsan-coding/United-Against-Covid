class Names():
    def __init__(self):
        self.names = ("John", "Joe", "James", "Jerri", "Janice")

    def start(self):
        print("Starting to print names")

    def printNames(self):
        for i in self.names:
            print(i)

    def finish(self):
        print("Finished printing names")

    def init(self):
        self.start()
        self.printNames()
        self.finish()

names = Names()
names.init()
