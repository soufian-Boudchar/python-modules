#!/usr/bin/env python3
    
def garden_operations():
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
        print(plant["missing\_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\_plant'\n")
    
    try:
        print("Testing multiple errors together...")
        12 / 0
        int("abc")
    except:
        print("Caught an error, but program continues!\n")

def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")
test_error_types()