print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

file_name = "classified_data.txt"
print("Initiating secure vault access...")
try:
    with open(file_name, "r") as file:
        print("Vault connection established with failsafe protocols\n")

        data = file.read()
        print("SECURE EXTRACTION:")
        print(data + "\n")

    with open(file_name, "w") as file:
        print("SECURE PRESERVATION:")
        print("{[}CLASSIFIED{]} New security protocols archived")
        file.write("\n[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")

except (FileNotFoundError, PermissionError) as e:
    print(f"ERROR: {e}")
