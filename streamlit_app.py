import requests
import streamlit as st
from tinydb_connection.connection import TinyDBConnection

def fetch_dog_facts(num=100):
    url = f"https://dog-api.kinduff.com/api/facts?number={num}"
    facts = requests.get(url).json()['facts']
    facts_dict = [{"fact": doc} for doc in facts]
    return facts_dict

st.title('🎈Demo app for connecting TinyDB with Streamlit')

st.write('Here are some fun facts about dogs!')

conn = st.experimental_connection(
        "tinydb",
        type=TinyDBConnection
        )
data = fetch_dog_facts()
conn.insert_multiple(data)
df = conn.query('fact', 'smell')
st.dataframe(df)
