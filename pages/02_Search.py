import streamlit as st
import pandas as pd

def search_page():
    """
    This page allows the user to upload an Excel or CSV file, display its data, and search for multiple keywords.
    """
    st.title("Search Data")

    # Step 1: Upload file (Excel or CSV)
    uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["csv", "xlsx"])

    # Check if a file is uploaded
    if uploaded_file:
        # Step 2: If Excel, allow sheet selection
        file_extension = uploaded_file.name.split('.')[-1]
        
        if file_extension == 'csv':
            df = pd.read_csv(uploaded_file)
            st.success("CSV file loaded successfully!")
        elif file_extension == 'xlsx':
            # Load Excel file and show sheet names for selection
            xls = pd.ExcelFile(uploaded_file)
            sheet_names = xls.sheet_names
            selected_sheet = st.selectbox("Select sheet", options=sheet_names)
            df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)
            st.success(f"Excel file loaded successfully! (Sheet: {selected_sheet})")
        else:
            st.error("Unsupported file format. Please upload a CSV or XLSX file.")
            return

        # Step 3: Display the DataFrame
        st.subheader("Data Preview")
        st.dataframe(df, height=400)

        # Step 4: Search functionality
        search_keywords = st.text_input("Enter keywords to search (separate with spaces or commas)")

        if search_keywords:
            # Split the input keywords by spaces or commas
            keywords = [kw.strip() for kw in search_keywords.replace(",", " ").split()]

            # Filter the DataFrame based on the keywords
            filtered_df = df[df.apply(lambda row: row.astype(str).str.contains('|'.join(keywords), case=False).any(), axis=1)]

            if not filtered_df.empty:
                st.subheader("Search Results")
                st.dataframe(filtered_df)
            else:
                st.warning("No matching rows found.")
    else:
        st.info("Please upload a file to start searching.")

# Add this function call in your main app file to display the "Search" page
if __name__ == "__main__":
    search_page()
