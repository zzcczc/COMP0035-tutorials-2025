import pandas as pd
from pathlib import Path
from importlib import resources

from activities import data
pd.set_option('display.max_columns', None)

if __name__ == '__main__':
    path_para_raw = resources.files(data).joinpath("paralympics_raw.csv")
    path_to_npc_csv_file = resources.files(data).joinpath("npc_codes.csv")

    cols = ['type', 'year', 'country', 'host', 'start', 'end', 'countries', 'events', 'sports',
            'participants_m', 'participants_f', 'participants']

    df_selected_cols = pd.read_csv(path_para_raw, usecols=cols)
    df_npc=pd.read_csv(path_to_npc_csv_file, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])

# Standardize country names for merging
df_selected_cols = df_selected_cols.replace({
    'UK': 'Great Britain',
    'USA': 'United States of America',
    'Korea': 'Republic of Korea',
    'Russia': 'Russian Federation',
    'China': "People's Republic of China"
})

# Merge DataFrames to add NPC codes
df_merged = df_selected_cols.merge(df_npc, how='left', left_on='country', right_on='Name')
print(df_merged[['country', 'Code', 'Name']])
df_merged= df_merged.drop(columns=['Name'])  # Drop the redundant 'Name' column after merging
print(df_merged)
