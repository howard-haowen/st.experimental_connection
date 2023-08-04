import streamlit as st
import sys
sys.path.insert(0, ".")
from connection import RestCountriesConnection, filter_by_population

st.title('🎈Demo app for connecting Streamlit with Restful API')
st.markdown("""
            - Author: [Haowen Jiang](https://howard-haowen.rohan.tw)
            - Data source: [REST Countries](https://restcountries.com/)
            - Dependencies:
                - `streamlit`
                - `requests`
                - `tinydb` 
            """)


# =================== #
# Step 0
# =================== #
st.markdown("""
            ## Step 0: Import dependencies 
            
            ```python
            import streamlit as st
            import sys
            sys.path.insert(0, ".")
            from connection import RestCountriesConnection, filter_by_population
            ```
            
            """)

# =================== #
# Step 1
# =================== #

conn = st.experimental_connection(
        "api",
        type=RestCountriesConnection,
        )

st.markdown("""
            ## Step 1: Initialize the connection
            - Signature: `st.experimental_connection({connection_name}, type={connection_class})`
            
            ```python
            conn = st.experimental_connection(
            "api",
            type=RestCountriesConnection,
            )
            ```
            
            """)

# =================== #
# Step 2 
# =================== #

fields = 'name,flag,population,region,capital,languages'
res = conn.query('region', 'asia', fields)

st.markdown("""
            ## Step 2: Search by a region name with certain fields
            - Signature: `conn.query({endpoint}, {query}, {fields})`

            ```python
            fields = 'name,flag,population,region,capital,languages'
            res = conn.query('region', 'asia', fields)
            ```
            
            """)
st.info(f"Found {len(res)} countries from the database!")
with st.expander("Click to see the results"):
    st.write(res)
    
# =================== #
# Step 3
# =================== #

filtered_res = filter_by_population(res, 1_000_000)

st.markdown("""
            ## Step 3: Filter results by population size using TinyDB search syntax 
            - Signature: `filter_by_population({result_list}, {population})`

            ```python
            filtered_res = filter_by_population(res, 1_000_000)
            ```
            
            """)

st.info(f"Found {len(filtered_res)} countries from the database!")
with st.expander("Click to see the results"):
    st.write(filtered_res)

