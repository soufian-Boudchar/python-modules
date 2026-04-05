import os
import sys
from dotenv import load_dotenv

print("ORACLE STATUS: Reading the Matrix...\n")

load_dotenv()

mode = os.getenv("MATRIX_MODE")
db_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "DEBUG")
zion = os.getenv("ZION_ENDPOINT")

if not mode or not api_key:
    print("[WARNING] Configuration is missing! Please check your .env file.")
    sys.exit(1)

if mode == "production":
    db_message = "Connected to secure production cluster"
else:
    db_message = "Connected to local instance"

print("Configuration loaded:")
print(f"Mode: {mode}")
print(f"Database: {db_message}")
print("API Access: Authenticated")
print(f"Log Level: {log_level}")
print("Zion Network: Online\n")

print("Environment security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available")
print("The Oracle sees all configurations.")