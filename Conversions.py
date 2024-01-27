# Conversions for calculations

class Conversions:
    def __init__(self, choice, numInput):
        self._numInput = numInput
        self._choice = choice
        
    #calculates/mutates the metric conversion based on user input
    def calculation(self):
        conversion = [0.0042267528, 28.349523125, 0.45359237, 3.785411784]
        conversion = conversion[self._choice-1]
        self._numInput= round(self._numInput * conversion,2)

    #acessor, gets numInput
    def getConversion(self):
        return self._numInput
        
    #tells user the correct measurement to input for the quantity
    def prompt(self):
        if self._choice in [1,2,3,4]:
            measurement = ["milliliters", "ounces", "pounds", "gallons"]
            measurement = measurement[self._choice-1]
            return measurement
        
    #calculates the metric conversion based on user input
    def prompt2(self):
        if self._choice in [1,2,3,4]:
            measurement = ["cups", "grams", "kilograms", "liters"]
            measurement = measurement[self._choice-1]
            return measurement

        
    #calculates the metric conversion based on user input
    def End(self):
        print("Exiting program")
        print("Thank you for using the Metrics Converter Application.")

    def Error(self):
        print("That is not an option, please enter a valid choice.")


