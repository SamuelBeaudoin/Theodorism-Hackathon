import pandas as pd
from compute_scores import preprocess_crime_data, proprocess_car_crash_data, preprocess_rue_pieton
import os
import glob

def merge_data():
    # Get all the files in the data directory
    df1 = preprocess_crime_data()
    df2 = preprocess_rue_pieton()
    df3 = pd.read_csv("data/feux-pietons.csv")
    df4 = proprocess_car_crash_data()
    df5 = pd.read_csv("data/travaux.csv")


    # Renaming latitude and longitude columns for consistency and adding 'Type' column
    df1 = df1.rename(columns={'LATITUDE': 'Latitude', 'LONGITUDE': 'Longitude'})
    df1['Type'] = 'actes-criminels'#score: 10

    df2 = df2.rename(columns={'LATITUDE': 'Latitude', 'LONGITUDE': 'Longitude'})
    df2['Type'] = 'rues-pietonnes'#score: 1

    df3 = df3.rename(columns={'Latitude': 'Latitude', 'Longitude': 'Longitude'})
    df3['Type'] = 'feux-pietons'
    df3['COST'] = 5

    
    df4 = df4.rename(columns={'LOC_LAT': 'Latitude', 'LOC_LONG': 'Longitude'})
    df4['Type'] = 'collisions-routieres'#score: 7

    df5 = df5.rename(columns={'latitude': 'Latitude', 'longitude': 'Longitude'})
    df5['Type'] = 'travaux'
    df5['COST'] = 2

    # Selecting only the required columns
    df1 = df1[['Type', 'Latitude', 'Longitude', 'COST']]
    df2 = df2[['Type', 'Latitude', 'Longitude', 'COST']]
    df3 = df3[['Type', 'Latitude', 'Longitude', 'COST']]
    df4 = df4[['Type', 'Latitude', 'Longitude', 'COST']]
    df5 = df5[['Type', 'Latitude', 'Longitude', 'COST']]

    # Concatenating all dataframes
    merged_df = pd.concat([df1, df2, df3, df4, df5])

    # Drop rows with missing values
    merged_df = merged_df.dropna()

    # Saving the merged dataframe to a new CSV file
    output_file = 'data/merged_data.csv'
    merged_df.to_csv(output_file, index=False)

    return merged_df