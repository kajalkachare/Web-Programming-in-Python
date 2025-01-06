#Python program to count amount of distance travel in kilometer
distance = float(input("Enter the distance traveled in km: "))

if distance > 0:
    if 1 <= distance <= 50:
        fare = 8* distance
    elif 51 <= distance <= 100:
        fare = 10 * distance
    elif distance > 100:
        fare = 12 * distance
    else:
        fare = 0

    print(f"The total fare km {fare:.2f}")
else:
    print("Invalid distance travel. Distance must be greater than 0.")
