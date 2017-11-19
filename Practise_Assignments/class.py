class animal:
    def structure(self,name,age,hands,eyes):
        self.name=name
        self.age=age
        self.hands=hands
        self.eyes=eyes
        print("Animals name is {},age is {},number of hands are {} and eyes {}".format(name,age,hands,eyes))

    def __init__(self):
        print('You are welcom')
