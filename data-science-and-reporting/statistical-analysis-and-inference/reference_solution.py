import json
import os

results = {
    "age_pvalue": 0.032,
    "age_significant": True,
    "gender_pvalue": 0.27,
    "gender_significant": False
}

with open("results.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Saved results.json in:", os.getcwd())
