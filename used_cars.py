from car import Car


def main():
    # Create a new Car object
    limo = Car("Limo", 100)

    # Add fuel
    limo.add_fuel(20)

    # Print amount of fuel
    print(f"Fuel in limo: {limo.fuel}")


    distance_driven = limo.drive(115)
    print(f"Distance driven: {distance_driven} km")

    # Print car details
    print(limo)


if __name__ == "__main__":
    main()
