class Car(object):
    def __init__(self, color, model, company, speedLimit):
        self.color = color
        self.model = model
        self.company = company
        self.speedLimit = speedLimit

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def accelerate(self):
        print("accelerate")

audi = Car("blue", "b10", "audi", "220kmph")
bmw = Car("red", "ax11", "bmw", "255kmph")
print (audi.start())
print (audi.model)
