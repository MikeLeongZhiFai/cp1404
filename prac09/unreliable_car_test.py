from prac09.unreliable_car import UnreliableCar


def main():
    # create cars with different status
    good_car = UnreliableCar("Mostly Good", 100, 90)
    lousy_car = UnreliableCar("Dodgy", 100, 9)

    #try to drive the cars many times
    # show the distance they drove
    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{lousy_car.name:12} drove {lousy_car.drive(i):2}km")

    # print the final states of the cars
    print(good_car)
    print(lousy_car)


main()