import sys

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

print("Initializing new storage unit: new_discovery.txt")
file = open("new_discovery.txt", "w")
print("Storage unit created successfully...\n")
print("Inscribing preservation data...")

data1 = "{[}ENTRY 001{]} New quantum algorithm discovered\n"
file.write(data1)
print(data1, end="")

data2 = "{[}ENTRY 002{]} Efficiency increased by 347%\n"
file.write(data2)
print(data2, end="")

data3 = "{[}ENTRY 003{]} Archived by Data Archivist trainee\n"
file.write(data3)
print(data3, end="")




print("\nData inscription complete. Storage unit sealed")
print("Archive 'new_discovery.txt' ready for long-term preservation.")

    