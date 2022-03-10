import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import sys
import os

data_path = sys.argv[1]
engine = create_engine("postgresql://postgres@db:5432/postgres")
df = pd.read_csv(data_path+'/'+os.listdir(data_path)[0], index_col='number')
df.to_sql('sample', engine)
print('Database created', flush=True)
print(pd.read_sql_query("select * from sample", con=engine))
