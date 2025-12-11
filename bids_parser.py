
import pandas as pd
import numpy as np

# PROJECT: GSoC 2026 Preparation
# DATASET: MEG-BIDS Brainstorm data sample (ds000246)
# NOTE: Using direct URL to the participants.tsv file for cloud testing.

def load_and_inspect_data():
    """
    Loads the participants file from OpenNeuro and performs basic inspection
    to check for missing values and data types.
    """
    print("--- 1. Loading BIDS Data ---")
    
    # Direct link to the raw tsv file
    # In a real project, this would be a local path like 'ds000246/participants.tsv'
    url = "https://openneuro.org/crn/datasets/ds000246/snapshots/1.0.0/files/participants.tsv"
    
    try:
        # Crucial: BIDS files are tab-separated (.tsv), not comma-separated (.csv)
        df = pd.read_csv(url, sep='\t')
        print(f"Success: Loaded data with {df.shape[0]} rows and {df.shape[1]} columns.\n")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    print("--- 2. Data Structure Inspection ---")
    print(df.info())
    print("\n")

    print("--- 3. Previewing Data ---")
    print(df.head())
    print("\n")

    # Basic Data Integrity Check
    # Checking if 'participant_id' is unique (Critical for BIDS validity)
    if df['participant_id'].is_unique:
        print("Data Quality Check Passed: All participant IDs are unique.")
    else:
        print("Warning: Duplicate participant IDs found.")

    # Check for missing values in key columns
    missing_count = df.isnull().sum()
    if missing_count.sum() > 0:
        print("\nMissing Values Found:")
        print(missing_count[missing_count > 0])
    else:
        print("\nClean Data: No missing values detected in this file.")

if __name__ == "__main__":
    load_and_inspect_data()
  
