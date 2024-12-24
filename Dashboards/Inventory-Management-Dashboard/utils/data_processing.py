import numpy as np
import pandas as pd

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Process the inventory data by cleaning and transforming it as needed.
    
    Args:
        df (pd.DataFrame): Raw inventory dataframe
        
    Returns:
        pd.DataFrame: Processed dataframe
    """
    # Create a copy to avoid modifying the original dataframe
    processed_df = df.copy()
    
    # Generate random stock values if needed (as in your original code)
    new_stock = np.random.normal(
        processed_df["stock"].mean(), 
        processed_df["stock"].std(), 
        processed_df.shape[0]
    )
    processed_df["stock"] = new_stock
    
    # Round stock values to 2 decimal places
    processed_df["stock"] = processed_df["stock"].round(2)
    
    # Ensure all required columns exist
    required_columns = ["name", "stock", "price"]
    for col in required_columns:
        if col not in processed_df.columns:
            raise ValueError(f"Required column '{col}' not found in dataframe")
    
    return processed_df