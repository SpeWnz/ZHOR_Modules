import sqlite3
import pandas
import hashlib
import json
from typing import Any, Tuple, Optional


# takes a "cursor.execute" result and returns a list of 
# column names
# example:
# res   = cursor.execute("some sql here")
# names = getColumnNames(res)
def getColumnNames(cursorExecuteResult):
    columnNames = [description[0] for description in cursorExecuteResult.description]
    return columnNames

# takes a "cursor.execute" and an index, and returns a list of 
# elements of a specific column, based on the index.
# example:
# res    = cursor.execute("some sql here")
# myList = columnToList(res)
def columnToList(cursorExecuteResult,index: int):
    results = cursorExecuteResult.fetchall()
    if len(results) > 0:
        return [x[index] for x in results]
    return []

# performs a query and transforms its result into a pandas dataframe object
# which then can be used to do other things (such as further convert it into
# an excel or csv file)
def queryToDataframe(query: str, connectionObject: sqlite3.Connection):
    df = pandas.read_sql_query(query,connectionObject)
    return df


'''
class used to cache tuples
usage:

cache = sqliteUtils.TupleCache('some_db.db')

someTuple = (a,b,c)


# check if tuple is in cache
jsonObject = cache.get(someTuple)
if jsonObject != None:
    # the tuple exists, do what you need to to
    foo = jsonObject[0]
    bar = jsonObject[1]
    biz = jsonObject[2]
    ... = ......


# store in cache
cache.set(someTuple,someResultTuple)


# when you're done, close the cache object
cache.close()

'''
class TupleCache:
    def __init__(self, db_path: str = "tuple_cache.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS cache (
                hash TEXT PRIMARY KEY,
                tuple_data TEXT NOT NULL,
                result TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    # ---- Core utility ----
    def _hash_tuple(self, data: Tuple[Any, ...]) -> str:
        """
        Generate SHA256 hash of tuple.
        Deterministic using JSON serialization.
        """
        serialized = json.dumps(data, sort_keys=True)
        return hashlib.sha256(serialized.encode()).hexdigest()

    # ---- Public API ----
    def exists(self, data: Tuple[Any, ...]) -> bool:
        h = self._hash_tuple(data)
        cursor = self.conn.execute(
            "SELECT 1 FROM cache WHERE hash = ?", (h,)
        )
        return cursor.fetchone() is not None

    def get(self, data: Tuple[Any, ...]) -> Optional[Any]:
        h = self._hash_tuple(data)
        cursor = self.conn.execute(
            "SELECT result FROM cache WHERE hash = ?", (h,)
        )
        row = cursor.fetchone()
        if row and row[0] is not None:
            return json.loads(row[0])
        return None

    def set(self, data: Tuple[Any, ...], result: Any = None):
        h = self._hash_tuple(data)
        serialized_tuple = json.dumps(data, sort_keys=True)
        serialized_result = json.dumps(result) if result is not None else None

        self.conn.execute("""
            INSERT OR IGNORE INTO cache (hash, tuple_data, result)
            VALUES (?, ?, ?)
        """, (h, serialized_tuple, serialized_result))
        self.conn.commit()

    def upsert(self, data: Tuple[Any, ...], result: Any = None):
        """
        Insert or overwrite result.
        """
        h = self._hash_tuple(data)
        serialized_tuple = json.dumps(data, sort_keys=True)
        serialized_result = json.dumps(result) if result is not None else None

        self.conn.execute("""
            INSERT INTO cache (hash, tuple_data, result)
            VALUES (?, ?, ?)
            ON CONFLICT(hash) DO UPDATE SET result=excluded.result
        """, (h, serialized_tuple, serialized_result))
        self.conn.commit()

    def close(self):
        self.conn.close()
