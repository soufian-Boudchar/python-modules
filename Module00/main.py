#!/usr/bin/env python3

"""
Helper file for Growing Code.
This file helps you test your exercises easily.
Just run: python3 main.py
"""

import importlib
import sys
import os


def test_ft_exercise(folder, exercise_file_name):
    """
    Run one exercise function from a folder.
    folder: ex0, ex1, etc.
    exercise_file_name: name of the Python file and function (without .py)
    """
    print(f"\n=== Testing {exercise_file_name} ===")

    try:
        # Path to the exercise folder
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(base_dir, folder)

        if not os.path.isdir(folder_path):
            raise ImportError(f"Folder {folder} not found")

        if folder_path not in sys.path:
            sys.path.insert(0, folder_path)

        # Import the module
        ft_module = importlib.import_module(exercise_file_name)

        # Get the function
        ft_function = getattr(ft_module, exercise_file_name)

        # Special handling for ft_seed_inventory
        if exercise_file_name == "ft_seed_inventory":
            ft_function("tomato", 15, "packets")
            ft_function("carrot", 8, "grams")
            ft_function("lettuce", 12, "area")
            ft_function("basil", 5, "unknown")
        else:
            ft_function()

    except ImportError as e:
        print(f"❌ Import error: {e}")

    except AttributeError:
        print(f"❌ Function {exercise_file_name}() not found")
        print(f"   Make sure you have: def {exercise_file_name}()")

    except TypeError as e:
        print(f"❌ Type error: {e}")

    except Exception as e:
        print(f"❌ Runtime error: {e}")


def main():
    print("🌱 Welcome to Growing Code! 🌱\n")
    print("Choose exercise:")
    print("0 - ft_hello_garden")
    print("1 - ft_plot_area")
    print("2 - ft_harvest_total")
    print("3 - ft_plant_age")
    print("4 - ft_water_reminder")
    print("5 - ft_count_harvest (iterative & recursive)")
    print("6 - ft_garden_summary")
    print("7 - ft_seed_inventory")
    print("a - test all")
    print()

    choice = input("Enter your choice: ")

    if choice == "0":
        test_ft_exercise("ex0", "ft_hello_garden")
    elif choice == "1":
        test_ft_exercise("ex1", "ft_plot_area")
    elif choice == "2":
        test_ft_exercise("ex2", "ft_harvest_total")
    elif choice == "3":
        test_ft_exercise("ex3", "ft_plant_age")
    elif choice == "4":
        test_ft_exercise("ex4", "ft_water_reminder")
    elif choice == "5":
        test_ft_exercise("ex5", "ft_count_harvest_iterative")
        test_ft_exercise("ex5", "ft_count_harvest_recursive")
    elif choice == "6":
        test_ft_exercise("ex6", "ft_garden_summary")
    elif choice == "7":
        test_ft_exercise("ex7", "ft_seed_inventory")
    elif choice.lower() == "a":
        # Test all exercises one by one
        test_ft_exercise("ex0", "ft_hello_garden")
        test_ft_exercise("ex1", "ft_plot_area")
        test_ft_exercise("ex2", "ft_harvest_total")
        test_ft_exercise("ex3", "ft_plant_age")
        test_ft_exercise("ex4", "ft_water_reminder")
        test_ft_exercise("ex5", "ft_count_harvest_iterative")
        test_ft_exercise("ex5", "ft_count_harvest_recursive")
        test_ft_exercise("ex6", "ft_garden_summary")
        test_ft_exercise("ex7", "ft_seed_inventory")
    else:
        print("❌ Invalid choice! Enter 0-7 or a")

        
if __name__ == "__main__":
    main()
