import pandas as pd
from pathlib import Path
from importlib import resources

from activities import data

def drop_a_column(df, col_name) :
    """Drop a column from a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        col_name (str): The name of the column to drop.

    Returns:
        pd.DataFrame: The DataFrame with the specified column dropped.
    """
    return df.drop(columns=[col_name])

def drop_a_row(df, row) :
    """Drop a row from a DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        index (int): The index of the row to drop.
    Returns:
        pd.DataFrame: The DataFrame with the specified row dropped.
    """
    return df.drop(index=row)

def remove_missing_values(df):
    missing_value_row=df.isnull().any(axis=1)
    return df[-missing_value_row]

def save_csv_to_data(df):
    try:
        path_to_save = Path(__file__).parent.parent / 'data' / 'paralympics_cleaned.csv'
        df.to_csv(path_to_save, index=False)
        print(f"DataFrame saved successfully to {path_to_save}")
    except Exception as e:
        print(f"An error occurred while saving the DataFrame: {e}")

pd.set_option('display.max_columns', None)
if __name__ == '__main__':
    path_para_raw = resources.files(data).joinpath("paralympics_raw.csv")
    path_to_npc_csv_file = resources.files(data).joinpath("npc_codes.csv")

    cols = ['type', 'year', 'country', 'host', 'start', 'end', 'countries', 'events', 'sports',
            'participants_m', 'participants_f', 'participants']

    df_selected_cols = pd.read_csv(path_para_raw, usecols=cols)
    df_npc = pd.read_csv(path_to_npc_csv_file, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])
    #print(df_selected_cols.head()) # Head means the first 5 rows

df_dropped = drop_a_column(df_selected_cols, 'type')
df_dropped1 = drop_a_row(df_selected_cols, 3)
NaN_deleted=remove_missing_values(df_selected_cols)# Remove rows with NaN values
df = NaN_deleted.reset_index(drop=True)# Reset index after removing rows with NaN values

# Correct specific data issues
index = df_selected_cols.query("type == 'Summer'").index[0]
df_selected_cols.at[index, 'type'] = df_selected_cols.at[index, 'type'].lower()
index2 = df_selected_cols.query("type == 'winter '").index[0]
df_selected_cols.at[index2, 'type'] = df_selected_cols.at[index2, 'type'].strip()

# Convert columns to appropriate data types
columns_to_change= ['countries', 'events', 'participants_m', 'participants_f', 'participants']
df_selected_cols[columns_to_change].fillna(0)  # Replaces the missing values with 0
df_selected_cols[columns_to_change] = df_selected_cols[columns_to_change].astype('Int64')# Convert columns to integer type
df_selected_cols['start'] = pd.to_datetime(df['start'], format='%d/%m/%Y')
df_selected_cols['end'] = pd.to_datetime(df['end'], format='%d/%m/%Y')
#print(df_selected_cols.dtypes)
columns_object= ['country', 'host', 'type']
df_selected_cols[columns_object] = df_selected_cols[columns_object].astype('string')# Convert columns to string type
#print(df_selected_cols)

# Add a new column 'duration' representing the duration of each event in days
df_selected_cols['duration'] = df_selected_cols['end'] - df_selected_cols['start']
duration_values = (df_selected_cols['end'] - df_selected_cols['start']).dt.days.astype('Int64')
df_selected_cols.insert(df_selected_cols.columns.get_loc('end') + 1, 'duration!', duration_values)
print(df_selected_cols)
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
save_csv_to_data(df_merged)