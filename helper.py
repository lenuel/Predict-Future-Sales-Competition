import pandas as pd
import numpy as np

def downgrade_dtypes(df):
    """Downgrade column types in the dataframe from float64/int64 type to float32/int32 type
    
    Parameters
    ----------
    df : DataFrame
    
    Returns
    -------
    df: DataFrame
        the output column types will be changed from float64/int64 type to float32/int32 type
           
    """

    # Select columns to downcast
    float_cols = [c for c in df if df[c].dtype == "float64"]
    int_cols =   [c for c in df if df[c].dtype == "int64"]
    
    # Downcast
    df[float_cols] = df[float_cols].astype(np.float32)
    df[int_cols]   = df[int_cols].astype(np.int32)
    
    return df

def create_submission_csv(file_name, test, y_test):
    """Create csv file for submission
    
    Parameters
    ----------
    file_name : str
        The string represents the name of csv file or filepath. 
        Csv will consists of two columns: "ID" and "item_cnt_month"
    test : DateFrame
        DataFrame with test submission
    y_test : ndarray
        An array object of (n,) shape where n is number of submission instances in the order given in test.csv file
    
    Returns
    -------
    None
    
    """
    y_test = np.clip(y_test, 0,20)
    submission = pd.DataFrame({"ID": test.index, "item_cnt_month": y_test})
    submission.to_csv(file_name, index=False)
    

def rename_shop_ids(df):
    """Rename shop ids in Data Frame 10 -> 11, 0 -> 57, 1 -> 58, 
    
    Parameters
    ----------
    df : DataFrame
        DateFrame should contain "shop_id" column
    
    Returns
    -------
        None
    
    """

    df.loc[df["shop_id"]==11,"shop_id"] = 10
    df.loc[df["shop_id"]==0,"shop_id"] = 57
    df.loc[df["shop_id"]==1,"shop_id"] = 58


def get_X_y(df, target_name):
    """Split DataFrame to feature and target
    
    Parameters
    ----------
    df : DataFrame
    target_name : str
        Name of target column present in DataFrame
    
    Returns
    -------
    X : DataFrame
        Original DataFrame without target column
    y : Series
        Target Series
    
    """
    
    y = df[target_name]
    X = df.drop(target_name, axis=1)
    return X, y
