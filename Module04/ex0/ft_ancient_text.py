print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

print("Accessing Storage Vault: ancient\\_fragment.txt")
try:
    file = open("ancient_fragment.txt", "r")
    print("Connection established...")
    print("\nRECOVERED DATA:")
    
    content = file.read()
    
    print(content)
    
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError as e:
    print(f"ERROR: Storage vault not found. Run data generator first.")