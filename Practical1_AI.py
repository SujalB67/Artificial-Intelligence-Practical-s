human_present = input("Is a human present in the room? (yes/no): ").lower()

outside_light = input("Is outside light available? (yes/no): ").lower()

if human_present == "yes" and outside_light == "no":
    print("Light ON")
else:
    print("Light OFF")
