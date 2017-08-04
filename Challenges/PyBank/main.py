import pandas as pd
import glob

data_sets = glob.glob( "*.csv")
data_frames = (pd.read_csv(f) for f in data_sets)
combined = pd.concat(data_frames, ignore_index=True)
combined.to_csv("budget_data", index=False)

