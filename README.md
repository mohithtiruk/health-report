-----Health Metric Analyzer-----

--Overview of the Project--

The Health Metric Analyzer is a simple, command-line utility written in Python designed to collect essential personal and health data from a user. It then processes this data to calculate the Body Mass Index (BMI) and provide basic health status assessments based on standard clinical guidelines for BMI, body temperature, and blood pressure. The goal is to demonstrate basic input/output operations, mathematical calculations, and conditional logic in a practical application.

--Features--

The application provides the following core functionalities:

Interactive Data Collection: Prompts the user to enter their name, age, weight (kg), height (meters), blood pressure (Systolic/Diastolic), and body temperature (°C).

BMI Calculation: Automatically calculates the Body Mass Index using the formula: 
BMI = (Weight (kg))/(Height (m)**2)

BMI Status Classification: Classifies the BMI into one of four categories:
Underweight (BMI < 18.5)
Normal Weight (18.5 <= BMI < 24.9)
Overweight (25 <= BMI < 29.9)
Obese (BMI => 30)

Blood Pressure Assessment: Parses the blood pressure input (e.g., "120/80") and classifies the status (Normal, Elevated, Stage 1 Hypertension, Stage 2 Hypertension, or Hypertensive Crisis).

Fever Detection: Checks if the recorded body temperature is indicative of a fever (above $37.5$ °C).

Structured Report: Prints a comprehensive, formatted health report to the console.

Data Storage: Stores all input and calculated metrics in a Python dictionary for easy programmatic access.

--Technologies/Tools Used--

Language: Python 3.x (The script uses features compatible with Python 3 and later versions).

Modules: No external libraries or modules are required. The script uses only built-in Python functions (input(), print(), int(), float(), map(), split()).

--Steps to Install & Run the Project--

Prerequisites:
You must have Python 3 installed on your system. You can check your version by running:
python --version
# or
python3 --version


Running the Script:
Save the Code: Save the provided code into a file named health_report.py.
Open Terminal: Navigate to the directory where you saved the file.
Execute: Run the script using the Python interpreter:

python health_report.py

Follow Prompts: The application will guide you to enter the required health metrics one by one.

--Instructions for Testing--

To ensure the conditional logic works correctly, test the application with inputs designed to trigger each outcome for BMI, Temperature, and Blood Pressure.

1. BMI Logic Test Cases

Status               Input Weight (kg)        Input Height (m)        Expected BMI Range

Underweight                50                     1.80                 15.4 (below 18.5)

Normal Weight              68                     1.75                 22.2 (18.5-24.9)

Overweight                 85                     1.70                 29.4 (25.0-29.9)

Obese                      100                    1.65                 36.7 (30.0 and above)

2. Blood Pressure Logic Test Cases

Status                  Input BP (Systolic/Diastolic)               Expected Output

Normal                          110/70                                  normal

Elevated                        125/75                                 elevated

Stage 1 Hypertension            135/85                       high blood pressure (stage 1)

Stage 2 Hypertension            150/95                       high blood pressure (stage 2)

Hypertensive Crisis             185/115                           hypertensive crisis

3. Temperature Logic Test Cases

Status             Input Temperature (°C)                   Expected Output

Normal                     36.8                      Your body temperature is normal.

Fever                      38.0                             You have a fever.
