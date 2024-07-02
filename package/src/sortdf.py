
def sorted_dataset_by_times(df):
    df['times'] = df['times'].astype(int)
    df_sorted =  df.sort_values(by='times')
    return df_sorted