import statistics

# Sample dataset: Daily website visits
traffic_data = [120, 145, 130, 180, 210, 195, 230]

mean_traffic = statistics.mean(traffic_data)
max_traffic = max(traffic_data)

print(f"Dataset: {traffic_data}")
print(f"Average traffic: {mean_traffic:.2f}")
print(f"Peak traffic: {max_traffic}")