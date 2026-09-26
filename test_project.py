from project import (
    calculate_daily_energy,
    calculate_peak_load,
    find_highest_consumer,
    calculate_solar_capacity,
    calculate_inverter_capacity
)


def test_calculate_daily_energy():
    appliances = [
        {
            "name": "Fan",
            "quantity": 3,
            "power": 80,
            "hours": 8
        },
        {
            "name": "AC",
            "quantity": 1,
            "power": 1200,
            "hours": 5
        }
    ]

    assert calculate_daily_energy(appliances) == 7.92


def test_calculate_peak_load():
    appliances = [
        {
            "name": "Fan",
            "quantity": 3,
            "power": 80,
            "hours": 8
        },
        {
            "name": "AC",
            "quantity": 1,
            "power": 1200,
            "hours": 5
        }
    ]

    assert calculate_peak_load(appliances) == 1440


def test_find_highest_consumer():
    appliances = [
        {
            "name": "Fan",
            "quantity": 3,
            "power": 80,
            "hours": 8
        },
        {
            "name": "AC",
            "quantity": 1,
            "power": 1200,
            "hours": 5
        }
    ]

    highest = find_highest_consumer(appliances)

    assert highest["name"] == "AC"


def test_calculate_solar_capacity():
    result = calculate_solar_capacity(
        7.92,
        5,
        0.80
    )

    assert result == 1.98


def test_calculate_inverter_capacity():
    result = calculate_inverter_capacity(1440)

    assert result == 1800
