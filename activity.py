class Car(object):
    def __init__(self, model, color, company, speed):
        self.color = color
        self.model = model
        self.company = company
        self.speed = speed
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerating...")
        self.speed = self.speed+3
        print(self.speed)
Mercades = Car("model 1", "black", "Daimler AG", 80)
Mercades.start()
Mercades.accelerate()
Mercades.stop()
