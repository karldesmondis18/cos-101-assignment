# PHYSICS CALCULATOR ASSIGNMENT

# 1. IMPULSE
def impulse():
    print("\n--- IMPULSE ---")

    force = float(input("Enter force (N): "))
    time = float(input("Enter time (s): "))

    J = force * time

    print("Impulse =", J, "Ns")


# 2. TORQUE
def torque():
    print("\n--- TORQUE ---")

    force = float(input("Enter force (N): "))
    distance = float(input("Enter perpendicular distance (m): "))

    T = force * distance

    print("Torque =", T, "Nm")


# 3. CENTRIPETAL FORCE
def centripetal_force():
    print("\n--- CENTRIPETAL FORCE ---")

    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    radius = float(input("Enter radius (m): "))

    if radius == 0:
        print("Radius cannot be zero.")
    else:
        F = (mass * velocity ** 2) / radius
        print("Centripetal Force =", F, "N")


# 4. SPRING POTENTIAL ENERGY
def spring_energy():
    print("\n--- SPRING POTENTIAL ENERGY ---")

    spring_constant = float(input("Enter spring constant (N/m): "))
    extension = float(input("Enter extension (m): "))

    E = 0.5 * spring_constant * extension ** 2

    print("Spring Potential Energy =", E, "J")


# 5. ELECTRIC POWER
def electric_power():
    print("\n--- ELECTRIC POWER ---")

    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    P = voltage * current

    print("Electric Power =", P, "Watts")


# MAIN PROGRAM

while True:

    print("\n================================")
    print("       PHYSICS CALCULATOR")
    print("================================")

    print("1. Impulse")
    print("2. Torque")
    print("3. Centripetal Force")
    print("4. Spring Potential Energy")
    print("5. Electric Power")

    choice = input("\nChoose an operation (1-5): ")

    if choice == "1":
        impulse()

    elif choice == "2":
        torque()

    elif choice == "3":
        centripetal_force()

    elif choice == "4":
        spring_energy()

    elif choice == "5":
        electric_power()

    else:
        print("Invalid choice. Please select 1-5.")

    # ASK USER TO CONTINUE

    answer = input("\nDo you want to continue? (yes/no): ").lower()

    if answer != "yes":
        print("\nThank you for using the Physics Calculator!")
        break