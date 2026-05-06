import pandas as pd
import matplotlib.pyplot as plt

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'

print("--START--")
print(f'Reading JSON file {input_file}')

# Read the data from JSON file into a pandas dataFrame
# eva stands for extra vehicular activity
eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
eva_df['eva'] = eva_df['eva'].astype(float)
# Clean data by removing any rows where duration is missing
eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)

print(f'Saving to CSV file {output_file}')
# Save the dataFrame to CSV file for later analysis
eva_df.to_csv(output_file, index=False, encoding='utf-8') # convert to csv file

# Sort the dataFrame, ready to be plotted with data on x-axis
eva_df.sort_values('date', inplace=True)

eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60) # convert duration from minutes to hours
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()  # compute comulative duration for the spacewalks over time

# Plot cumulative time spent in space over years
print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()

print("--END--")