import sys
import os
import site

py_path = sys.executable
if sys.base_prefix == sys.prefix:
    # if the virtual environment is off:
    print("MATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate    # On Windows")
    print("\nThen run this program again.")
else:
    # if the virtual environment is on:
    venv_path = sys.prefix
    venv_name = os.path.basename(venv_path)
    site_path = [p for p in site.getsitepackages() if "site" in p]
    print("MATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: {py_path}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting\nthe global system.")
    print("\nPackage installation path:")
    print(*site_path)