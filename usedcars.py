from car import Car

def main():
    bus = Car(180)
    bus.drive(30)
    limo=Car(100,"Limo")
    limo.add_fuel(20)
    print("{} fuel={}".format(limo.name,limo.fuel))
    limo.odometer=115
    print("{} odo ={}".format(limo.name,limo.odometer))
    print(limo)
    #print("fuel =", bus.fuel)
    #print("odo =", bus.odometer)
    #print(bus)

main()

