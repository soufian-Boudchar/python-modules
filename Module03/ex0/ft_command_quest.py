import sys

length = len(sys.argv)

print("=== Command Quest ===")

if length == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {length}")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {length - 1}")
    for i in range(1, length):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {length}")
