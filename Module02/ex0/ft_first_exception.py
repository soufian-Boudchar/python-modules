#!/usr/bin/env python3
def check_temperature(temp_str: str) -> int:
    """Validates if the input is a number and within
    the safe range (0-40) for plants."""
    print(f"Testing temperature: {temp_str}")

    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        return temp


def test_temperature_input() -> None:
    """Runs tests with valid, invalid,
    and extreme inputs to demonstrate error handling."""
    print("=== Garden Temperature Checker ===\n")
    result = check_temperature("25")
    print(f"Temperature {result}°C is perfect for plants!\n")
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


test_temperature_input()
