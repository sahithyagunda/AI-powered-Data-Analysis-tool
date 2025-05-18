# AskTheData - Data Analysis Tool

## Overview

**AskTheData** is a powerful and user-friendly data exploration tool built using **Streamlit** and **Pandas**. It allows users to easily upload CSV files, explore datasets, and generate data visualizations through natural language prompts. The tool leverages **AI-powered code generation** to produce custom visualizations based on user queries, helping users better understand their data with minimal effort.

## Features

- **Upload CSV files**: Users can upload their own CSV datasets for analysis.
- **Data Preprocessing**: Automatically converts data types for ease of analysis.
- **Data Preview**: Displays a preview of the dataset for quick insights.
- **Natural Language Prompts**: Users can provide natural language descriptions to generate visualizations.
- **AI-Powered Visualizations**: Automatically generates code for creating visualizations using **Seaborn** and **Matplotlib**.
- **Error Handling**: Provides clear feedback if issues arise during file upload or code execution.

Tech Stack for AskTheData

Backend & Logic

Python — Core programming language

pandas — For data loading, preprocessing, and manipulation

seaborn & matplotlib — For data visualization

exec — To dynamically execute AI-generated Python code

Google Gemini (via get_visualization_code) — AI-generated visualization code from user prompts

 Web Framework

Streamlit — For building the interactive UI and data upload interface

File Handling

CSV file parsing using pandas
