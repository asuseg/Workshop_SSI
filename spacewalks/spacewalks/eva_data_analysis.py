import pandas as pd
import matplotlib.pyplot as plt

def read_json_to_dataframe(input_file):
    print(f'Reading JSON file {input_file}')
    eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    eva_df['eva'] = eva_df['eva'].astype(float)
    # Clean data by removing any rows where duration is missing
    eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return eva_df

def write_dataframe_to_csv (df, output_file):
    print(f'Saving to CSV file {output_file}')
    df.to_csv(output_file, index=False, encoding='utf-8')

def plot_df (df, output_graph_file):
    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(output_graph_file)
    plt.show()

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'

print("--START--")

# Read the data from JSON file into a pandas dataFrame
# eva stands for extra vehicular activity
eva_data = read_json_to_dataframe(input_file)

# Convert and export data to CSV file for later analysis
write_dataframe_to_csv(eva_data, output_file)

# Sort the dataFrame, ready to be plotted with data on x-axis
eva_data.sort_values('date', inplace=True)

eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()  

# Plot cumulative time spent in space over years
plot_df(eva_data, graph_file)

print("--END--")