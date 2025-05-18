
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_basic_visuals(df):
    st.subheader("📊 Auto-Generated Visualizations")

    # Distribution plots for numerical columns
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in num_cols[:3]:  # show top 3 to avoid clutter
        st.markdown(f"**Distribution of {col}**")
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, ax=ax, color='skyblue')
        st.pyplot(fig)

    # Bar plots for categorical columns
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols[:3]:  # show top 3 to avoid clutter
        if df[col].nunique() <= 20:  # skip huge cardinality
            st.markdown(f"**Counts of {col}**")
            fig, ax = plt.subplots()
            sns.countplot(y=col, data=df, order=df[col].value_counts().index[:10], palette="pastel", ax=ax)
            st.pyplot(fig)

    # Correlation heatmap if there are enough numeric columns
    if len(num_cols) >= 3:
        st.markdown("**Correlation Heatmap**")
        corr = df[num_cols].corr()
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        st.pyplot(fig)
