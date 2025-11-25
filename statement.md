----Project Statement: Health Metric Analyzer---

--Problem Statement--
Individuals often collect multiple personal health metrics (such as weight, height, blood pressure, and temperature)
but lack a quick, standardized, and automated method to consolidate this data and receive instantaneous, 
generalized health assessments based on established public health guidelines. Manually performing calculations 
(like BMI) or referencing charts for classification (like blood pressure staging) is time-consuming and prone to human error.

The problem this project addresses is the need for a simple, accessible, and automated command-line utility to calculate, consolidate, 
and classify primary health indicators, providing the user with immediate feedback on their status according to common health benchmarks.

--Scope of the Project--

The scope of the Health Metric Analyzer is strictly defined as follows:

In-Scope:
Collecting seven key health metrics from the user via command-line input.
Calculating Body Mass Index (BMI).
Categorizing BMI, blood pressure, and body temperature against simplified, general health ranges.
Generating a structured, human-readable report summarizing all inputs and assessments.
Storing the final data set in a local Python dictionary.

Out-of-Scope:
Providing personalized medical advice or diagnoses. (The assessments are purely based on general formulas and classifications.)
Persistent storage (e.g., using a database or file system).
Advanced features like trend analysis, historical data tracking, or data visualization.
Web-based or graphical user interfaces (GUIs).

The project is limited to a single-use, single-session Python script.

--Target Users--

The primary target users for this project are:

Programming Students & Beginners: Individuals learning basic Python programming concepts 
(input/output, data types, control flow, functions) who need a simple, practical example.

Developers Needing Quick Calculations: Programmers or data analysts who require a fast,
non-GUI tool to perform and verify BMI and simple health classifications.

Health and Wellness Enthusiasts: Individuals who want a quick way to compute and check their
health metrics against standard categories without relying on third-party websites or complex applications.

--High-Level Features--

The Analyzer provides three high-level capabilities built around data management and analysis:

Metric Input & Consolidation: Allows users to input all necessary health data interactively
and combines it into a comprehensive data structure.

Automated Calculation & Assessment:
Calculates BMI automatically.
Provides quick-check status for weight classification, blood pressure stage, and fever 
detection based on input values.

Reporting: Generates a clean, readable, command-line report that presents all the raw data,
calculated results, and resulting classifications in an organized format.
