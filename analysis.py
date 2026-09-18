import pandas as pd

data = pd.read_csv("experiment_results.csv")

# Q1: overall conversion
for variant in ["control", "treatment"]:
    x = data[data["variant"] == variant]
    print(variant, len(x), x["converted"].mean())

control_rate = data.loc[data["variant"] == "control", "converted"].mean()
treatment_rate = data.loc[data["variant"] == "treatment", "converted"].mean()
print("Naive lift (pp):", (treatment_rate - control_rate) * 100)

# Q2 and Q3: segment results
for segment, g in data.groupby("segment"):
    c = g[g["variant"] == "control"]
    t = g[g["variant"] == "treatment"]

    c_rate = c["converted"].mean()
    t_rate = t["converted"].mean()
    lift_pp = (t_rate - c_rate) * 100
    share = len(g) / len(data)

    print(
        segment,
        "control:", len(c), c_rate,
        "treatment:", len(t), t_rate,
        "lift_pp:", lift_pp,
        "share:", share
    )

# Q3: mix-adjusted lift
mix_adjusted = 0
for segment, g in data.groupby("segment"):
    c_rate = g.loc[g["variant"] == "control", "converted"].mean()
    t_rate = g.loc[g["variant"] == "treatment", "converted"].mean()
    share = len(g) / len(data)
    mix_adjusted += share * (t_rate - c_rate) * 100

print("Mix-adjusted lift (pp):", mix_adjusted)

# Q5: treatment/control split inside each segment
split = pd.crosstab(data["segment"], data["variant"])
split["total"] = split["control"] + split["treatment"]
split["control_pct"] = split["control"] / split["total"] * 100
split["treatment_pct"] = split["treatment"] / split["total"] * 100
print(split)
