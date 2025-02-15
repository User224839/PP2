import json
import math

with open("sampledata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Берем первое значение "delay" и переводим в радианы
degree = float(data["imdata"][0]["l1PhysIf"]["attributes"]["delay"])
radian = degree * (math.pi / 180)

print(f"Delay in degrees: {degree}")
print(f"Converted to radians: {radian:.6f}")
