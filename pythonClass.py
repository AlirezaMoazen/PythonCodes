class Car:
    def __init__(self, moddel1, year1, color1):
        self.moddel = moddel1
        self.year = year1
        self.color = color1
    def show(self):
        print("Hello Class")
    def whatIs(self):
        print ("modell is {} and year is {} years".format(self.moddel, self.year))
    def __repr__(self):
        return f"color is {self.color}"
c1=Car("the new 2", "2024", "grau")
c1.show()
c1.whatIs()
print(c1)