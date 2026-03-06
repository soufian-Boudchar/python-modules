import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

a = input("Input Stream active. Enter archivist ID: ")
s = input("Input Stream active. Enter status report: ")

sys.stdout.write("\n{[}STANDARD{]} Archive status from ARCH_7742: " + a + "\n")

sys.stderr.write("{[}ALERT{]} System diagnostic: " + s + "\n")
sys.stdout.write("{[}STANDARD{]} Data transmission complete")
print("\n\nThree-channel communication test successful.")
