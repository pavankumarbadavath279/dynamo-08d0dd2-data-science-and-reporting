import pandas as pd
import numpy as np
import os

df = pd.DataFrame({
    "respondent_id": np.arange(1, 101),
    "group_id": np.random.randint(1, 6, size=100),
    "age": np.random.randint(18, 65, size=100),
    "gender": np.random.choice(["Male", "Female"], size=100),
    "response": np.random.randint(1, 6, size=100)
})

df.to_csv("survey_dataset.csv", index=False)
print("✅ Saved survey_dataset.csv in:", os.getcwd())
