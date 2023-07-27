# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %%
datafile = "../datasets/data.csv"

# %%
data = pd.read_csv(datafile)

# %% [markdown]
# ### Data Exploration Analysis(EDA)

# %%
data

# %%
data.head()

# %% [markdown]
# #### The columns names are quite inconsistent, therefore, normalizing the columns names as well as string values across the dataset is advised. These are the normalization steps I'll take.
# - Change all values to lowercase. Columns inclusive
# - replace all whitespace inbetween characters with an underscore

# %%
data.columns = data.columns.str.lower().str.replace(" ", "_")

# %%
data.head()

# %%



