import csv
from collections import defaultdict
file_path = "data/clean_data.csv"

def calculate_decade_averages(file_path):
    """Calculate and print the average temperature anomaly for each decade, starting from 1881."""
    temperature_data_by_decade = defaultdict(list)

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            year = int(row[0])
            # Calculate the decade offset for years starting from 1881
            decade = ((year - 1881) // 10) * 10 + 1880
            anomalies = [float(value) for value in row[1:-1]]

            if anomalies:
                average_anomaly = sum(anomalies) / len(anomalies)
                temperature_data_by_decade[decade].append(average_anomaly)

    print( "Average Temperature Anomaly")
    # Iterate through the decades and calculate the average anomaly for each
    for decade, anomalies in sorted(temperature_data_by_decade.items()):
        decade_start = decade + 1
        decade_end = decade + 10
        decade_average = sum(anomalies) / len(anomalies)
        print(f"Decade {decade_start} to {decade_end}: {decade_average:.2f}°F")

if __name__ == "__main__":
    calculate_decade_averages(file_path)
