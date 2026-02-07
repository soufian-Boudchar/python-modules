def garden_operations():
    """
    Triggers and catches common Python built-in exceptions to 
    demonstrate error handling in agricultural data pipelines.
    """
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        12 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        plant = {"type": "flower"}
        print(plant["missing\\_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    try:
        print("Testing multiple errors together...")
        12 / 0
        int("abc")
    except (ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    """
    Initializes the error demonstration and prints the required header format for the evaluation.
    """
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


test_error_types()
