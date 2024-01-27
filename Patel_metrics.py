import Conversions

def menu():
    choice = int(input(
    "\nEnter 1 for Milliliters to Cups conversion."
    "\nEnter 2 for Ounces to Grams conversion."
    "\nEnter 3 for Pounds to Kilograms conversion."
    "\nEnter 4 for Gallons to Liters conversion."
    "\nEnter 5 to exit the program.\n"))

    return choice 




def main():
    name=str(input("Please enter your name: \n"))
    print("Welcome", name ,"to the Metrics Converter Application.")
    while True:
        choice=menu()
        if choice==5:
            metric=Conversions.Conversions(choice,0)
            metric.End()
            break
        elif choice in [1,2,3,4]:
            metric=Conversions.Conversions(choice,0)
            numInput=float(input(f"Please enter your quantity in {metric.prompt()}\n"))
            metric=Conversions.Conversions(choice,numInput)
            metric.calculation()
            print(f"The quantity in {metric.prompt2()} is {metric.getConversion()} rounded to 2 decimal places.")
            
        else:
            metric=Conversions.Conversions(choice,0)
            metric.Error()
            
                        
        

        
        



main()
    
    
