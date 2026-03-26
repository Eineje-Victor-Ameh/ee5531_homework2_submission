import csv
import matplotlib.pyplot as plt

range_bearing_steps = []
range_bearing_spread = []
range_only_steps = []
range_only_spread = []

with open("activity2_data.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        config = row["config"].strip()
        step = int(row["step"])
        spread = float(row["spread"])

        if config == "range_bearing":
            range_bearing_steps.append(step)
            range_bearing_spread.append(spread)
        elif config == "range_only":
            range_only_steps.append(step)
            range_only_spread.append(spread)

plt.plot(range_bearing_steps, range_bearing_spread, marker="o", label="Range + Bearing")
plt.plot(range_only_steps, range_only_spread, marker="o", label="Range only")

plt.xlabel("Step")
plt.ylabel("Spread (sigma)")
plt.title("Spread vs Step Number")
plt.legend()
plt.grid(True)
plt.savefig("../screenshots/a2_p2_spread_plot.png", dpi=300, bbox_inches="tight")
plt.show()
