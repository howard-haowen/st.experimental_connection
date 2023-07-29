import pandas as pd
import re
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
from tinydb import TinyDB, Query

class TinyDBConnection(ExperimentalBaseConnection[TinyDB]):
    """Basic st.experimental_connection implementation for TinyDB"""

    def _connect(self, **kwargs) -> TinyDB:
        # if 'database' in kwargs:
        #     db = kwargs.pop('database')
        # else:
        #     db = self._secrets['database']
        # 
        conn = TinyDB('./data.json', **kwargs)
        return conn
    
    def query(self, field: str, query: str, ttl: int = 3600) -> pd.DataFrame:
        @cache_data(ttl=ttl)
        def _query(field: str, query: str) -> pd.DataFrame:
            q = Query()
            results = self.search(q[field].search(query, flags=re.IGNORECASE))
            doc_ids = [doc.doc_id for doc in results]
            df = pd.DataFrame(results, index=doc_ids)
            return df
        
        return _query(field: str, query: str)
