import streamlit as st

def homepage():
    st.title("Disaster Recovery Supporting Tools")
    st.subheader("Your one-stop platform for managing and analyzing Disaster Recovery data.")

    st.markdown("""
    Welcome to the DR Supporting Tools app. This platform is designed to help you manage, compare, and analyze raw data from your Disaster Recovery operations.
    More tools will be added to enhance your workflow, making DR processes seamless and efficient.
    """)

    st.markdown("## Available Tools")
    st.markdown("""
    - **Changes Tool**: Upload and compare raw data files to track differences.
    - **Search Tool**: Upload data files and perform keyword searches.
    """)

    st.markdown("### Coming Soon")
    st.markdown("""
    - **Analysis Tool** (Coming Soon): Gain insights and perform detailed data analysis.
    - **Dashboard** (Coming Soon): Visualize your DR data using custom dashboards.
    """)

    with st.expander("How to Use the App"):
        st.write("""
        - **Changes Tool**: Upload old and recent data files to compare differences.
        - **Search Tool**: Upload a data file and search for specific keywords or entries.
        
                 More features and tools will be added in the future!
        """)

# Call the homepage function in your Streamlit app
if __name__ == "__main__":
    homepage()
