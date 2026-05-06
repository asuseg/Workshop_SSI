import pandas as pd
import matplotlib.pyplot as plt

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a pandas dataFrame.
    Clean the data by removing any rows where the duration is missing.

    Args:
        input_file (file or str): The file object or the path to a JSON file.

    Returns:
        eva_df (pd.DataFrame): The clean data as a datFrame structure
    """
    print(f'Reading JSON file {input_file.name}')
    eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return eva_df

def write_dataframe_to_csv (df, output_file):
    """
    Write dataframe to CSV file.

    Args:
        df (pd.DataFrame): Input dataframe.
        output_file (file or str): The file object or the path to a CSV file.
    """
    print(f'Saving to CSV file {output_file.name}')
    df.to_csv(output_file, index=False, encoding='utf-8')

def plot_cumulative_time_in_space (df, output_graph_file):
    """
    Plot the cumulative time in space over years.
    Convert the duration column from strings to number of hours.
    Calculate cumulative sum of durations.
    Generate a plot of cumulative time spent in space as a function of the date. 

    Args:
        df (pd.DataFrame): Data containting a "data" conlumn and a "cumulative_time" column
        output_graph_file (file or str): The file object or the path to a figure file (.png)
    """
    df['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    df['cumulative_time'] = eva_data['duration_hours'].cumsum()  
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

# Plot cumulative time spent in space over years
plot_cumulative_time_in_space(eva_data, graph_file)

print("--END--")