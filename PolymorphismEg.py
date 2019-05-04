class Car:

    def igntionType(self):
        print('Either by keys or button')

class Honda(Car):
    
    def ignitionType(self):
        print('my latest versions do not require any keys')

class Maruti(Car):

    def ignitionType(self):
        print('Do not lose your keys')



h=Honda()
h.ignitionType()