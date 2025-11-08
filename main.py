import sys

temp_anomaly_data = [
    (1980, 0.26),
    (1990, 0.44),
    (2000, 0.61),
    (2010, 0.81),
    (2020, 1.02),
    (2025, 1.20)
]


def analyze_global_anomaly(data):
    years = [item[0] for item in data]
    anomalies = [item[1] for item in data]

    start_year = years[0]
    end_year = years[-1]
    start_anomaly = anomalies[0]
    end_anomaly = anomalies[-1]

    time_span = end_year - start_year
    total_increase = end_anomaly - start_anomaly

    if time_span > 0:
        avg_rate = total_increase / time_span
    else:
        avg_rate = 0.0

    print("GLOBAL TEMPERATURE ANOMALY ANALYSIS")
    print("-" * 45)
    print(f"Data Span: {start_year} - {end_year} ({time_span} years)")
    print(f"Starting Anomaly ({start_year}): {start_anomaly}°C")
        print(f"Ending Anomaly ({end_year}): {end_anomaly}°C")
        print("-" * 45)

    change_color_start = "\033[91m"
    change_color_end = "\033[0m"

    print(f"Total Increase in Anomaly: {change_color_start}{total_increase:.2f}°C{change_color_end}")
    print(f"Average Rate of Increase: {avg_rate:.3f}°C per year")
    print("-" * 45)
    print("Meaning of this: The global temperature has increased by the total increase over the period analyzed.")


if __name__ == "__main__":
    analyze_global_anomaly(temp_anomaly_data)
