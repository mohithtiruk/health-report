name = (input("Enter your name: "))
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
blood_pressure = input("Enter your blood pressure (e.g., 120/80): ")
temperature = float(input("Enter your body temperature in Celsius: "))
print("\n--- Health Report ---")
print(f"Name: {name}")
print(f"Age: {age} years")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")
print(f"Blood Pressure: {blood_pressure}")
print(f"Body Temperature: {temperature} °C")
print(f"Hello, {name}! You are {age} years old.")
print(f"Your BMI is {bmi:.2f}.")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
print("Your blood pressure is recorded as:", blood_pressure)
print("Your body temperature is:", temperature, "°C")
if temperature > 37.5:
    print("You have a fever.")
else:
    print("Your body temperature is normal.")
if blood_pressure:
    systolic, diastolic = map(int, blood_pressure.split('/'))
    if systolic < 120 and diastolic < 80:
        bp_status = "normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        bp_status = "elevated"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        bp_status = "high blood pressure (stage 1)"
    elif 140 <= systolic or 90 <= diastolic:
        bp_status = "high blood pressure (stage 2)"
    else:
        bp_status = "hypertensive crisis"
    print(f"Your blood pressure is considered: {bp_status}.")
database = {
    "name": name,
    "age": age,
    "weight": weight,
    "height": height,
    "bmi": bmi,
    "blood_pressure": blood_pressure,
    "temperature": temperature
}
print("\nData stored in database:", database)
