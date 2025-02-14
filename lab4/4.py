from datetime import datetime

date1 = datetime(2024, 2, 10, 14, 30, 0)  # Example date
date2 = datetime(2024, 2, 14, 18, 15, 0)  # Another example date

difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)