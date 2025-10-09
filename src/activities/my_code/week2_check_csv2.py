from pathlib import Path
# This script is located in a subfolder so you need to navigate up to the parent (src) and then its parent (project root), then down to the 'data' directory and finally the .csv file
csv_file = Path(__file__).parent.parent.joinpath('data', 'npc_codes.csv')
csv_file_v2 = Path(__file__).parent.parent / 'data' / 'npc_codes.csv' # also works
# Check if the file exists
if csv_file.exists():
    print(f"CSV file found: {csv_file}")
else:
    print("CSV file not found.")