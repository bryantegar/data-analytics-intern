import os

print("=== START PIPELINE ===")

print("\n[1] Scraping data...")
os.system("python scripts/scraping.py")

print("\n[2] Cleaning data...")
os.system("python scripts/cleaning.py")

print("\n[3] Generating dashboard...")
os.system("python scripts/dashboard.py")

print("\n=== PIPELINE SELESAI ===")
