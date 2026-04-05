import sys, importlib

print("LOADING STATUS: Loading programs...\n")


print("Checking dependencies:")


packages_import = {
    "pandas": "Data manipulation ready",
    "matplotlib": "Visualization ready",
    "numpy": "Numerical computations ready"
}

missing = False

for i in packages_import.items():
    name = i[0]
    message = i[1]
    try:
        module = importlib.import_module(name)
        print(f"[OK] {name} ({module.__version__}) - {message}")
    except ImportError:
        print(f"[ERROR] {name} is missing :(")
        missing = True
if missing:
    print("\nMissing packages? Run: pip install -r requirements.txt")
    sys.exit(1)
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



base_price = 70000
price_change = np.random.randn(1000)
bitcoin_prices = base_price + np.cumsum(price_change)
p = pd.DataFrame(bitcoin_prices)

file_name = "matrix_analysis.png"
print("\nAnalyzing Matrix data...")
print("Processing 1000 data points...")
print("Generating visualization...")
plt.plot(p, linewidth=1.5)
plt.title("Bitcoin (BTC) Price Volatility Simulation")
plt.xlabel("Time (Hours)")
plt.ylabel("Price (USD)")
plt.savefig(file_name)

print("\nAnalysis complete!")
print(f"Results saved to: {file_name}")
