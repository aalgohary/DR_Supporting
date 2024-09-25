import streamlit as st
import pandas as pd

def changes_page():
    """
    Page to upload old and recent raw data and compare the differences.
    If the files are Excel files with multiple sheets, allow the user to select sheets.
    The differences will be displayed in a DataFrame.
    The user can select which columns to compare based on.
    """
    st.title("Changes - Data Comparison")

    # Step 1: Upload buttons for old and recent data
    old_file = st.file_uploader("Upload Old Raw Data (CSV or XLSX)", type=['csv', 'xlsx'], key='old_data')
    recent_file = st.file_uploader("Upload Recent Raw Data (CSV or XLSX)", type=['csv', 'xlsx'], key='recent_data')

    old_data, recent_data = None, None

    # Step 2: Handle file uploads and sheet selection
    if old_file:
        old_data, old_sheets = load_file(old_file)
        if old_sheets:
            selected_old_sheet = st.selectbox("Select sheet from Old File", options=old_sheets)
            old_data = pd.read_excel(old_file, sheet_name=selected_old_sheet)
        st.success(f"Old data uploaded successfully (Sheet: {selected_old_sheet if old_sheets else 'N/A'}).")

    if recent_file:
        recent_data, recent_sheets = load_file(recent_file)
        if recent_sheets:
            selected_recent_sheet = st.selectbox("Select sheet from Recent File", options=recent_sheets)
            recent_data = pd.read_excel(recent_file, sheet_name=selected_recent_sheet)
        st.success(f"Recent data uploaded successfully (Sheet: {selected_recent_sheet if recent_sheets else 'N/A'}).")

    # Step 3: If both files are uploaded, proceed to comparison
    if old_data is not None and recent_data is not None:
        # Step 4: Get columns common to both datasets
        common_columns = list(set(old_data.columns).intersection(set(recent_data.columns)))

        if len(common_columns) == 0:
            st.error("The datasets do not have any common columns for comparison.")
            return

        # Step 5: Let the user select which columns to compare
        selected_columns = st.multiselect(
            "Select columns to compare:",
            options=common_columns,
            default=common_columns  # Default to all common columns
        )

        # If columns are selected, compare data
        if selected_columns:
            st.subheader("Differences Between Old and Recent Data (based on selected columns)")
            differences = compare_dataframes(old_data[selected_columns], recent_data[selected_columns])
            
            # Check if there are any differences to display
            if not differences.empty:
                # Step 6: Sorting options
                st.markdown("### Sorting Options")
                sort_column = st.selectbox("Select column to sort by:", options=selected_columns)
                sort_order = st.radio("Sort order:", options=["Ascending", "Descending"])

                # Sort the DataFrame based on the selected column and order
                sorted_differences = differences.sort_values(
                    by=sort_column, 
                    ascending=(sort_order == "Ascending")
                )

                st.dataframe(sorted_differences, hide_index=True)  # Display sorted DataFrame
            else:
                st.info("No differences found between the selected columns.")
        else:
            st.warning("Please select at least one column to compare.")
    else:
        st.info("Please upload both old and recent data to proceed with comparison.")

def load_file(file):
    """
    Helper function to load a file into a pandas DataFrame based on its type (CSV or XLSX).
    Returns the DataFrame and a list of sheet names if it's an Excel file.
    """
    file_extension = file.name.split('.')[-1]
    if file_extension == 'csv':
        return pd.read_csv(file, index_col=None), None  # index_col=None prevents pandas from using the first column as an index
    elif file_extension == 'xlsx':
        # Load the sheet names first for selection
        xls = pd.ExcelFile(file)
        sheet_names = xls.sheet_names
        # Return None for data until sheet selection is made
        return None, sheet_names
    else:
        st.error("Unsupported file format. Please upload a CSV or XLSX file.")
        return None, None

def clean_column_data(df):
    """
    Function to clean column data for comparison.
    Converts all columns to strings, replaces placeholders like '-' with None, and handles specific data types.
    """
    # Replace common placeholders
    df.replace("-", None, inplace=True)
    
    # Convert columns to strings for comparison, except dates which should be handled separately
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].dtype == 'O':
            df[col] = df[col].fillna("").astype(str)
        # Handle date columns
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = pd.to_datetime(df[col], errors='coerce')

    return df

def compare_dataframes(old_df, recent_df):
    """
    Compare two DataFrames by concatenating and removing duplicates.
    Adds a 'Source' column to indicate whether the row belongs to the old or recent DataFrame.
    Keeps only the rows with differences.
    """
    try:
        # Add a 'Source' column to differentiate between old and recent data
        old_df['Source'] = 'Old'
        recent_df['Source'] = 'Recent'

        # Concatenate the two DataFrames
        combined_df = pd.concat([old_df, recent_df])

        # Clean the data in the combined DataFrame
        combined_df = clean_column_data(combined_df)

        # Remove duplicates excluding the 'Source' column
        deduplicated_df = combined_df.drop_duplicates(subset=combined_df.columns.difference(['Source']), keep=False)

        return deduplicated_df

    except ValueError as e:
        st.error(f"An error occurred during comparison: {e}")
        return pd.DataFrame()

# Add this function call in your main app file to display the "Changes" page
if __name__ == "__main__":
    changes_page()
