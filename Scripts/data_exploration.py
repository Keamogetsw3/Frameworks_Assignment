"""
This script handles loading and basic exploration of the CORD-19 metadata.csv dataset.

Steps:
1. Load the dataset into a pandas DataFrame.
2. Explore the dataset by viewing:
   - The first few rows
   - Dataset structure and column data types
   - Summary statistics
   - Missing values
   - Duplicate paper titles

Usage:
    python scripts/data_exploration.py

"""

import pandas as pd
import os

