"""This module contains functions for cleaning and transforming data."""

import hashlib

import numpy as np
import pandas as pd


def convert_area_to_sqm(area: int | float | str) -> float:
    """Cleans, checks, and converts the manually collected floor space information to square meters.

    There are four options for the input value:
    - A float or int, which is already in square meters. If the value is 0, it is converted to NaN.
    - A string with a number followed by 'sq.f.' or'f', which is in square feet.
    - A string with a number followed by 'sq.m.', which is in square meters.
    - An empty string or a dash, which is converted to NaN.
    """
    if isinstance(area, int | float):
        if area == 0:
            return np.nan
        return area
    if isinstance(area, str):
        area = area.strip()

        # If the string is empty or a dash, return NaN
        if area in ("", "-"):
            return np.nan

        # Extract the value before the first whitespace and remove commas
        area_num = area.split(" ")[0].replace(",", "")

        # Convert to float
        area_num = float(area_num)

        # Check if the value is in square feet and convert to square meters if needed
        if "f" in area.lower():
            return area_num * 0.092903
        return float(area_num)

    err_msg = "Invalid input type. Please provide a string or a number."
    raise ValueError(err_msg)


def anonymize_data_centers(
    df: pd.DataFrame, sensitive_columns: list[str] | None = None
) -> pd.DataFrame:
    """Replaces identifiable information with a random ID and removes sensitive columns."""
    if sensitive_columns is None:
        sensitive_columns = ["name", "company", "address", "notes"]
        
    # Copy to avoid setting values on a slice of another dataframe
    df = df.copy()

    # Generate a string combining identifiers
    unique_series = df.apply(
        lambda row: f"{row.get('name', '')}_{row.get('latitude', '')}_{row.get('longitude', '')}", 
        axis=1
    )
    
    # Map every truly unique row signature to a distinct 10-character hash
    # Using unique() ensures we don't accidentally enforce duplicates during mapping
    unique_signatures = unique_series.unique()
    id_mapping = {
        sig: hashlib.sha256(sig.encode()).hexdigest()[:10] 
        for sig in unique_signatures
    }
    
    # Assign the IDs via mapping
    df["id"] = unique_series.map(id_mapping)

    # CRITICAL: Reset the index to prevent Pandas from hitting structural layout conflicts 
    # when doing multiple concatenations/merges later
    df = df.reset_index(drop=True)

    # Drop columns that exist in the dataframe
    cols_to_drop = [col for col in sensitive_columns if col in df.columns]
    return df.drop(columns=cols_to_drop)
