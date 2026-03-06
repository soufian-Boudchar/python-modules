print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")


def crisis_handler(file_name, acces=False):
    try:
        if acces:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        with open(f"{file_name}", "r"):
            print("SUCCESS: Archive recovered - ", end="")
            print("``Knowledge preserved for humanity''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


crisis_handler("lost_archive.txt")

print()
crisis_handler("classified_data.txt")
print()
crisis_handler("standard_archive.txt", True)
print("\nAll crisis scenarios handled successfully. Archives secure.")
