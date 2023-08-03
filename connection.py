import pathlib
import requests
import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
from tinydb import TinyDB, Query

class RestCountriesConnection(ExperimentalBaseConnection):

    def _connect(self):
        self.api_url = 'https://restcountries.com/v3.1/{endpoint}/{query}?fields={fields}'
        
    def query(self, endpoint: str, query: str, fields: str, ttl=600):
        
        @st.cache_data(ttl=ttl)
        def _fetch(endpoint, query, fields):
            url = self.api_url.format(endpoint=endpoint, query=query, fields=fields)
            res = requests.get(url).json()
            return res
        
        res = _fetch(endpoint, query, fields)
        return res

def filter_by_population(data: list, pop: int):
    db_path = './data.json'
    db_file = pathlib.Path(db_path)
    
    # Remove existing db_file 
    if db_file.exists():
        db_file.unlink()
        
    db = TinyDB(db_path)
    db.insert_multiple(data)
    q = Query()
    res = db.search(q['population'] > pop)
    return res
