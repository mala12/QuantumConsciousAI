from pathlib import Path 

# Check for the baseline_images directory
baseline_dir = Path(__file__).resolve().parent / "baseline_images"

print(f"Expected path: {baseline_dir}")  # Print the expected directory path

if baseline_dir.exists() and baseline_dir.is_dir():
    print(f"Directory exists: {baseline_dir}")
    files = list(baseline_dir.glob("*"))
    if files:
        print("Files found in the directory:")
        for file in files:
            print(f"- {file.name}")
    else:
        print("Directory exists but is empty.")
else:
    print(f"Directory is missing: {baseline_dir}")
