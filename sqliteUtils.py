import sqlite3
import pandas

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