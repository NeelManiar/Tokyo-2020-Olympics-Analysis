import pandas as pd
from pandas_profiling import ProfileReport

medals = pd.read_csv('Medals.csv')
profile = ProfileReport(medals)
profile.to_file(output_file='medals.html')