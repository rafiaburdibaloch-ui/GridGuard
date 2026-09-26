# GridGuard

GridGuard is a Python-based energy management and planning tool that helps users analyze household appliance energy consumption and estimate basic solar, battery, and inverter requirements.

The program uses appliance information such as power rating, quantity, and daily operating hours to calculate energy consumption and connected load. It also provides a simple solar advisor, what-if simulation, energy-saving recommendations, and a text-based energy report.

## Features

* Add household appliances with input validation
* View the list of added appliances
* Calculate daily energy consumption in kWh
* Calculate connected peak load in watts
* Identify the highest energy-consuming appliance
* Estimate required solar capacity
* Estimate backup energy requirements
* Estimate battery capacity
* Estimate inverter capacity
* Simulate changes in appliance usage
* Generate energy-saving recommendations
* Export an energy analysis report to a text file
* Automated testing using pytest

## How It Works

For each appliance, the user enters:

* Appliance name
* Quantity
* Power rating in watts
* Operating hours per day

GridGuard uses this information to calculate total daily energy consumption and connected load.

The Solar Advisor uses user-provided system parameters such as:

* Peak sun hours
* Solar system efficiency
* Required backup hours
* Battery voltage
* Battery depth of discharge
* Battery efficiency

The program then provides estimated solar, battery, and inverter requirements.

## Project Structure

```text
GridGuard/
│
├── GridGuard.py
├── test_project.py
├── README.md
└── requirements.txt
```

### `GridGuard.py`

Contains the main GridGuard application, calculations, recommendations, report generation, input validation, and menu system.

### `test_project.py`

Contains automated tests for the main calculation functions.

### `requirements.txt`

Lists the external packages required by the project. The main application uses Python's standard library and does not require external packages.

### `README.md`

Contains project documentation and instructions.

## Requirements

* Python 3
* pytest for running automated tests

The main application itself does not require external Python libraries.

## How to Run

Open a terminal in the GridGuard folder and run:

```bash
python GridGuard.py
```

The program will display the main menu:

```text
GRIDGUARD
1. Add Appliance
2. View Appliances
3. Energy Analysis
4. Solar Advisor
5. What-If Simulator
6. Recommendations
7. Export Report
8. Exit
```

Select an option by entering its corresponding number.

## Example Workflow

First, select **Add Appliance** and enter the appliance details.

For example:

```text
Appliance name: Fan
Quantity: 3
Power (W): 80
Hours/day: 8
```

You can then add other appliances such as an air conditioner, refrigerator, lights, or television.

After adding appliances, **Energy Analysis** can be used to view:

```text
Daily energy: ... kWh
Peak load: ... W
Highest consumer: ...
```

The **Solar Advisor** can then be used to estimate solar capacity, backup energy, battery capacity, and inverter capacity based on the supplied system parameters.

## What-If Simulation

The What-If Simulator allows the user to change the operating hours of an existing appliance without changing the original appliance data.

It shows:

* Current daily energy
* New daily energy
* Change in energy consumption

This helps users understand how changing appliance usage affects overall energy consumption.

## Recommendations

GridGuard provides simple recommendations based on the entered appliance data.

For example, it can identify the highest energy-consuming appliance and provide suggestions when total connected load or daily energy consumption is relatively high.

## Exported Report

Using the **Export Report** option creates:

```text
gridguard_report.txt
```

The report contains:

* Appliance information
* Daily energy consumption
* Peak load
* Highest energy consumer

## Testing

The project includes automated tests using `pytest`.

Run the tests with:

```bash
pytest
```

or:

```bash
python -m pytest
```

The test suite checks five functions:

* `calculate_daily_energy()`
* `calculate_peak_load()`
* `find_highest_consumer()`
* `calculate_solar_capacity()`
* `calculate_inverter_capacity()`

The current test suite contains **5 tests**, and all tests pass successfully.

Expected result:

```text
5 passed
```

## Technologies Used

* Python
* Python standard library
* pytest
* Command-line interface

## Author

Rafia Burdi Baloch

Electronics Engineering
Mehran University of Engineering & Technology (MUET)
