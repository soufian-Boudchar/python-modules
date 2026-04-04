import sys, importlib

print("LOADING STATUS: Loading programs...\n")


print("Checking dependencies:")


packages_import = {
    "pandas": "Data manipulation ready",
    "matplotlib": "Visualization ready",
    "requests": "Network access ready",
    "numpy": "Numerical computations ready"
}

missing = False

for i in packages_import.items():
    name = i[0]
    message = i[1]
    try:
        module = importlib.import_module(name)
        print(f"[OK] {name}, ({module.__version__}) - {message}")
    except ImportError:
        print(f"[ERROR] {name} is missing :(")
        missing = True
if missing:
    print("\nMissing packages? Run: pip install -r requirements.txt")
    sys.exit(1)
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("\nAnalyzing Matrix data...")
data = np.random.randn(1000, 2)
p = pd.DataFrame(data, columns=['hello', 'world'])

plt.plot(p)
plt.savefig("hello.png")
