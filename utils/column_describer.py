import streamlit as st
import pandas as pd


def describe_column(col_name, col_data):
    dtype = col_data.dtype
    num_nulls = col_data.isnull().sum()
    num_unique = col_data.nunique()
    per_nullvalues = (num_nulls / len(col_data)) * 100

    raw_samples = col_data.dropna().unique()[:5]
    sample_values = [str(val) for val in raw_samples]  # <- convert to readable format

    # Determine the type
    if pd.api.types.is_numeric_dtype(col_data):
        col_type = "Numeric"
        desc = f"'{col_name}' is a numerical column with {num_unique} unique values."
    elif pd.api.types.is_datetime64_any_dtype(col_data):
        col_type = "DateTime"
        desc = f"'{col_name}' is a DateTime column."
    else:
        col_type = "Categorical"
        desc = f"'{col_name}' is a Categorical column."

    return {
        "name": col_name,
        "type": col_type,
        "nulls": num_nulls,
        "uniques": num_unique,
        "sample_values": sample_values,
        "description": desc
    }


## to display in UI

def display_column_descriptions(df):
    st.subheader("Column Descriptions")

    for col in df.columns:
        info = describe_column(col, df[col])
        with st.expander(f"🔹 {info['name']} ({info['type']})"):
            st.markdown(f"**Description:** {info['description']}")
            st.markdown(f"**Null values:** {info['nulls']}")
            st.markdown(f"**Unique values:** {info['uniques']}")
            st.markdown(f"**Sample values:** {list(info['sample_values'])}")
