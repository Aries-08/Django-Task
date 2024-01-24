import pandas as pd 
from firstPage.models import ipl

df = pd.read_csv('/Users/radhikaagrawal/Downloads/CSV Files/matches - matches.csv')

cols = ['team1', 'team2', 'season']
selected_data = df[cols]

matches_data = selected_data.to_dict(orient='records')

ipl.objects.bulk_create([ipl(**data) for data in matches_data])