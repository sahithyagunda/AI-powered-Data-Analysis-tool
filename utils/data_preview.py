import streamlit as st

def preview_data(df):
    st.subheader("dataset preview")
    st.dataframe(df.head())
    st.subheader("🔍 Dataset Info")
    st.write(f"**Shape:** {df.shape}")
    st.write(f"**Columns:** {list(df.columns)}")

    st.write("**Data Types:**")
    st.write(df.dtypes)