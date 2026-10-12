# GridGuard

#### Video Demo: https://youtu.be/bxmvYoG_OU4

#### Description:

GridGuard is a Python-based energy management and planning tool that helps users understand household electricity consumption and estimate basic solar, battery, and inverter requirements. It is a menu-driven command-line application that allows users to enter household appliances, analyze their energy usage, explore alternative usage scenarios, and generate an energy analysis report.

I developed GridGuard as my final project for CS50's Introduction to Programming with Python (CS50P). As an Electronics Engineering student, I wanted to build a project that connects my engineering background with the programming skills I learned throughout the course. Electricity consumption, connected load, and solar power calculations are practical topics in electrical and electronics engineering, and Python provides a way to organize these calculations into a useful tool.

The main purpose of GridGuard is to make basic household energy calculations easier to perform and understand. Instead of calculating the energy consumption of each appliance manually, users can enter appliance information and let the program calculate the results. The application also helps users explore how changes in daily appliance usage can affect total energy consumption.

### Features

GridGuard includes the following features:

- **Add Appliances:** Enter an appliance's name, quantity, power rating in watts, and daily operating hours.
- **View Appliances:** Display the appliances entered by the user.
- **Energy Analysis:** Calculate estimated daily energy consumption in kilowatt-hours, total connected load in watts, and the appliance with the highest energy consumption.
- **Solar Advisor:** Estimate solar capacity, backup energy requirements, battery capacity, and inverter capacity using user-provided system parameters.
- **What-If Simulator:** Change an appliance's daily operating hours and compare the resulting energy consumption with the original scenario.
- **Energy-Saving Recommendations:** Provide suggestions based on appliance information and energy analysis.
- **Report Export:** Save the energy analysis to a text file for later reference.
- **Automated Testing:** Use pytest to test important calculation functions.

### How It Works

When adding an appliance, the user provides its name, quantity, power rating in watts, and operating hours per day. GridGuard uses these inputs to estimate daily energy consumption.

The daily energy consumption of an appliance is calculated using:

Energy (kWh) = Power (W) × Quantity × Hours per Day / 1000

The program adds the consumption of all entered appliances to estimate the total daily energy demand. It also calculates the combined connected load and identifies the appliance with the highest daily energy consumption.

The Solar Advisor uses the estimated energy demand along with parameters such as peak sun hours, system efficiency, backup duration, battery voltage, depth of discharge, and battery efficiency. These values help the program estimate the system capacity needed for basic planning. The results are preliminary estimates rather than professional installation specifications, because actual systems also depend on environmental conditions, equipment ratings, and other design requirements.

The What-If Simulator allows users to change the operating hours of an appliance and observe how the total daily energy consumption changes. For example, reducing an air conditioner's usage from five hours to three hours per day can demonstrate the potential effect of reducing electricity usage. This feature helps users compare scenarios before deciding how they might manage their appliance usage.

### Project Files

The project contains the following files:

- **`project.py`:** The main application. It contains the menu system, user input handling, energy calculations, solar and battery estimates, recommendations, and report export functionality.
- **`test_project.py`:** Contains automated tests for the project's calculation functions and helps verify that important computations produce the expected results.
- **`requirements.txt`:** Lists the external Python packages required by the project, if any.
- **`README.md`:** Documents the project's purpose, features, setup instructions, calculations, and testing process.

### Requirements and Installation

GridGuard requires Python 3. The main application uses Python's standard library for its core functionality. If pytest is listed in `requirements.txt`, it is needed to run the automated test suite.

To start the application, run:

```bash
python project.py
```

The program displays a menu through which users can select the available operations. Users can add appliances, view their entries, perform energy analysis, use the Solar Advisor, run the What-If Simulator, view recommendations, export a report, or exit the application.

### Example Usage

A user might add a fan with a power rating of 80 watts, a quantity of one, and eight operating hours per day. The fan's estimated daily energy consumption would be:

80 × 1 × 8 / 1000 = 0.64 kWh

The user could then add an air conditioner rated at 1,000 watts operating for five hours per day. Its estimated daily energy consumption would be 5 kWh. Together, these appliances consume an estimated 5.64 kWh per day.

These examples demonstrate how GridGuard converts basic appliance information into understandable energy estimates. Actual consumption can differ depending on operating conditions and the appliance's real power demand.

### Report Export

The report export feature allows users to save their energy analysis in a text file named `gridguard_report.txt`. Depending on the information supported by the application, the report includes appliance details and calculated energy results. This provides a convenient record that users can review after completing an analysis.

### Testing

GridGuard includes automated tests written with pytest. The tests are intended to check important calculations, including daily energy consumption, connected load, highest energy consumer, and solar or inverter capacity estimates.

To run the test suite, use:

```bash
pytest -v
```

The command displays the individual test results and indicates whether the tests pass or fail. Automated testing helps identify calculation errors and makes it easier to maintain the application as it develops.

### Design Decisions and Learning Outcomes

I chose a command-line interface because it allowed me to focus on Python fundamentals and the energy calculations rather than spending time building a graphical interface. Separating the program into functions makes the calculations easier to understand, test, and maintain. Input validation also helps the program handle incorrect user entries more appropriately.

One important design choice was to include the What-If Simulator alongside the basic energy analysis. Rather than only displaying a consumption value, GridGuard allows users to explore how different usage habits affect their estimated energy demand. The Solar Advisor extends this idea by connecting energy consumption to preliminary renewable-energy planning.

Developing GridGuard helped me practise functions, loops, conditional statements, user input, numerical calculations, file handling, testing, and project documentation. Most importantly, it allowed me to apply Python programming to a practical problem related to my engineering field.

### Author

Rafia Burdi Baloch

Electronics Engineering Student  
Mehran University of Engineering & Technology (MUET)  
Hyderabad, Sindh, Pakistan
