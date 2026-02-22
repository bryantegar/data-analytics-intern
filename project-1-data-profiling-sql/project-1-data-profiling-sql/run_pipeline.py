import os

print("=== START PIPELINE ===")

print("\n[1] Scraping...")
os.system("python scripts/scraping.py")

print("\n[2] Cleaning...")
os.system("python scripts/cleaning.py")

print("\n[3] Dashboard...")
os.system("python scripts/dashboard.py")

print("\n=== DONE ===")
