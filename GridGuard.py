def calculate_daily_energy(appliances):
    total_energy = 0
    for appliance in appliances:
        power = appliance["power"]
        quantity = appliance["quantity"]
        hours = appliance["hours"]
        daily_energy = power*quantity*hours
        total_energy += daily_energy
    return total_energy/1000

def calculate_peak_load(appliances):
    total_load = 0
    for appliance in appliances:
        power = appliance["power"]
        quantity = appliance["quantity"]
        daily_load = power*quantity
        total_load += daily_load
    return total_load

def find_highest_consumer(appliances):
    highest = None
    for appliance in appliances:
        power = appliance["power"]
        quantity = appliance["quantity"]
        hours = appliance["hours"]
        energy = power*quantity*hours
        if highest is None or energy > highest["power"] * highest["quantity"] * highest["hours"]:
            highest = appliance
    return highest

def calculate_solar_capacity(daily_energy, peak_sun_hours, efficiency):
    solar_capacity = daily_energy/(peak_sun_hours * efficiency)
    return solar_capacity

def calculate_backup_energy(daily_energy, backup_hours):
    backup_energy = daily_energy/24*backup_hours
    return backup_energy

def calculate_battery_capacity(backup_energy, voltage, dod, efficiency):
    backup_energy_wh = backup_energy * 1000
    battery_capacity = backup_energy_wh /(voltage*dod*efficiency)
    return battery_capacity

def calculate_inverter_capacity(peak_load):
    inverter_capacity = peak_load * 1.25
    return inverter_capacity

def generate_recommendations(appliances):
    recommendations = []

    highest = find_highest_consumer(appliances)

    if highest is not None:
        recommendations.append(
            f"Consider reducing the usage of {highest['name']}, "
            f"which is your highest energy consumer."
        )

    peak_load = calculate_peak_load(appliances)

    if peak_load > 3000:
        recommendations.append(
            "Your connected load is relatively high. "
            "Consider checking which appliances need to operate simultaneously."
        )

    daily_energy = calculate_daily_energy(appliances)

    if daily_energy > 10:
        recommendations.append(
            "Daily energy consumption is high. "
            "Consider improving energy efficiency or reducing unnecessary usage."
        )

    if not recommendations:
        recommendations.append(
            "Your current energy usage appears relatively moderate."
        )

    return recommendations

def export_report(appliances):
    daily_energy = calculate_daily_energy(appliances)
    peak_load = calculate_peak_load(appliances)
    highest = find_highest_consumer(appliances)

    with open("gridguard_report.txt", "w") as file:
        file.write("GRIDGUARD ENERGY REPORT\n")
        file.write("=======================\n\n")

        file.write("APPLIANCES\n")
        file.write("----------\n")

        for appliance in appliances:
            file.write(
                f"{appliance['name']} | "
                f"Quantity: {appliance['quantity']} | "
                f"Power: {appliance['power']} W | "
                f"Hours/day: {appliance['hours']}\n"
            )

        file.write("\nENERGY ANALYSIS\n")
        file.write("----------------\n")
        file.write(f"Daily energy: {daily_energy:.2f} kWh\n")
        file.write(f"Peak load: {peak_load:.0f} W\n")

        if highest is not None:
            file.write(f"Highest consumer: {highest['name']}\n")

    print("Report exported successfully!")
def main():
    appliances = []
    while True:
        print("\nGRIDGUARD")
        print("1. Add Appliance")
        print("2. View Appliances")
        print("3. Energy Analysis")
        print("4. Solar Advisor")
        print("5. What-If Simulator")
        print("6. Recommendations")
        print("7. Export Report")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Appliance name: ").strip()
            if not name:
                print("Appliance name cannot be empty.")
                continue
            try:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
            except ValueError:
                print("Please enter a valid whole number for quantity.")
                continue
            try:
                power = float(input("Power (W): "))
                if power <= 0:
                    print("Power must be greater than 0.")
                    continue
            except ValueError:
                print("Please enter a valid number for power.")
                continue
            try:
                hours = float(input("Hours/day: "))
                if hours < 0 or hours > 24:
                    print("Hours must be between 0 and 24.")
                    continue
            except ValueError:
                print("Please enter a valid number for hours.")
                continue
            appliance = {
                "name": name,
                "quantity": quantity,
                "power": power,
                "hours": hours
            }
            appliances.append(appliance)
            print(f"{name} added successfully!")

        elif choice == "2":
            if not appliances:
                print("No appliances added yet.")
            else:
                print("Your Appliances")
                print("--------------------------------")
                for appliance in appliances:
                    name = appliance["name"]
                    quantity = appliance["quantity"]
                    power = appliance["power"]
                    hours = appliance["hours"]
                    print(f"{name} | {quantity} | {power} | {hours}")


        elif choice == "3":
            if not appliances:
                print("Please add at least one appliance first." )
            else:
                daily_energy = calculate_daily_energy(appliances)
                peak_load = calculate_peak_load(appliances)
                highest = find_highest_consumer(appliances)
                print("\nENERGY ANALYSIS")
                print("----------------------------")
                print(f"Daily energy: {daily_energy:.2f} kWh")
                print(f"Peak load: {peak_load:.0f} W")
                print(f"Highest consumer: {highest['name']}")

        elif choice == "4":
            if not appliances:
                print("Please add at least one appliance first.")
            else:
                try:
                    peak_sun_hours = float(
                        input("Peak sun hours/day: ")
                    )
                    if peak_sun_hours <= 0:
                        print("Peak sun hours must be greater than 0.")
                        continue
                    efficiency = float(
                        input("System efficiency (e.g. 0.80): ")
                    )
                    if efficiency <= 0 or efficiency > 1:
                        print("Efficiency must be between 0 and 1.")
                        continue
                    backup_hours = float(
                        input("Backup hours required: ")
                    )
                    if backup_hours < 0 or backup_hours > 24:
                        print("Backup hours must be between 0 and 24.")
                        continue
                    voltage = float(
                        input("Battery voltage (V): ")
                    )
                    if voltage <= 0:
                        print("Battery voltage must be greater than 0.")
                        continue
                    dod = float(
                        input("Battery depth of discharge (e.g. 0.80): ")
                    )
                    if dod <= 0 or dod > 1:
                        print("Depth of discharge must be between 0 and 1.")
                        continue
                    battery_efficiency = float(
                        input("Battery efficiency (e.g. 0.90): ")
                    )
                    if battery_efficiency <= 0 or battery_efficiency > 1:
                        print("Battery efficiency must be between 0 and 1.")
                        continue
                except ValueError:
                    print("Please enter valid numbers.")
                    continue
                daily_energy = calculate_daily_energy(appliances)
                solar_capacity = calculate_solar_capacity(
                    daily_energy,
                    peak_sun_hours,
                    efficiency
                )
                peak_load = calculate_peak_load(appliances)
                backup_energy = calculate_backup_energy(
                    daily_energy,
                    backup_hours
                )
                battery_capacity = calculate_battery_capacity(
                    backup_energy,
                    voltage,
                    dod,
                    battery_efficiency
                )
                inverter_capacity = calculate_inverter_capacity(
                    peak_load
                )
                print("\nSOLAR ADVISOR")
                print("----------------------------")
                print(f"Daily energy: {daily_energy:.2f} kWh")
                print(
                    f"Estimated solar capacity: "
                    f"{solar_capacity:.2f} kW"
                )
                print(
                    f"Required backup energy: "
                    f"{backup_energy:.2f} kWh"
                )
                print(
                    f"Estimated battery capacity: "
                    f"{battery_capacity:.2f} Ah"
                )
                print(
                    f"Estimated inverter capacity: "
                    f"{inverter_capacity:.0f} W"
                )

        elif choice == "5":
            if not appliances:
                print("Please add at least one appliance first.")
            else:
                name = input("Enter appliance name: ")
                for appliance in appliances:
                    if appliance["name"].lower() == name.lower():
                        print(f"Found: {appliance['name']}")
                        try:
                            new_hours = float(
                                input("New hours/day: ")
                            )
                            if new_hours < 0 or new_hours > 24:
                                print(
                                    "Hours must be between 0 and 24."
                                )
                                break
                        except ValueError:
                            print("Please enter a valid number.")
                            break
                        current_energy = calculate_daily_energy(
                            appliances
                        )
                        old_energy = (
                            appliance["power"]
                            * appliance["quantity"]
                            * appliance["hours"]
                        ) / 1000
                        new_energy = (
                            appliance["power"]
                            * appliance["quantity"]
                            * new_hours
                        ) / 1000
                        new_total_energy = (
                            current_energy
                            - old_energy
                            + new_energy
                        )
                        difference = (
                            new_total_energy - current_energy
                        )
                        print("\nWHAT-IF SIMULATION")
                        print("----------------------------")
                        print(
                            f"Current daily energy: "
                            f"{current_energy:.2f} kWh"
                        )
                        print(
                            f"New daily energy: "
                            f"{new_total_energy:.2f} kWh"
                        )
                        print(
                            f"Change: "
                            f"{difference:+.2f} kWh/day"
                        )
                        break
                else:
                    print("Appliance not found.")
        elif choice == "6":
            if not appliances:
                print("Please add at least one appliance first.")
            else:
                recommendations = generate_recommendations(appliances)

                print("\nRECOMMENDATIONS")
                print("----------------------------")

                for recommendation in recommendations:
                    print(f"- {recommendation}")

        elif choice == "7":
            if not appliances:
                print("Please add at least one appliance first.")
            else:
                export_report(appliances)
        elif choice == "8":
            print("Goodbye!")
            break



if __name__ == "__main__":
    main()


