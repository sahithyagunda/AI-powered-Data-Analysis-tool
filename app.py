import streamlit as st
import pandas as pd
from utils.data_preview import preview_data
#from utils.column_describer import display_column_descriptions
#from utils.auto_visualizer import plot_basic_visuals
from utils.llm_visualizer import get_visualization_code

st.set_page_config(page_title='AskTheData', layout='centered')
st.title("📊 AskTheData — Upload & Explore Your Dataset")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        df.columns = df.columns.str.strip().str.lower()

        st.success("✅ File loaded successfully")
        df = df.convert_dtypes()

        # Convert data types
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = pd.to_numeric(df[col], errors="coerce")
            elif pd.api.types.is_object_dtype(df[col]):
                df[col] = df[col].astype(str)

        # Show dataframe and EDA
        #st.dataframe(df)
        preview_data(df)
        #display_column_descriptions(df)
        #plot_basic_visuals(df)

        # Gemini AI Visualization
        user_prompt = st.text_area("Enter your visualization prompt:")

        if st.button("Generate Visualization"):
            with st.spinner("Thinking..."):
                full_prompt = f"{user_prompt}. Use the DataFrame named df only. Do not create a new one."

                code = get_visualization_code(full_prompt)
                st.code(code if code else "⚠️ No code generated", language='python')
                st.write("🔍 Raw code output (repr):")
                st.text(repr(code))

                # Check if LLM generated fake data
                if "pd.DataFrame" in code or "data =" in code:
                    st.warning("⚠️ The AI may have generated sample data instead of using your actual dataset. Try rephrasing your prompt.")

                # Try to run the generated code
                try:
                    import seaborn as sns
                    import matplotlib.pyplot as plt
                    local_vars = {"df": df, "pd": pd, "sns": sns, "plt": plt}
                    exec(code, {}, local_vars)
                    st.pyplot(plt)
                except Exception as e:
                    st.error(f"Error running the generated code: {e}")


    except Exception as e:
        st.error(f"❌ Failed to open file: {e}")
else:
    st.info("📂 Please upload a CSV file to get started.")
