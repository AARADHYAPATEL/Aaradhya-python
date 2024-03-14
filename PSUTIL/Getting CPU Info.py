import psutil

# Get CPU information
cpu_count = psutil.cpu_count()
cpu_percent = psutil.cpu_percent(interval=1)

print("CPU Count:", cpu_count)
print("CPU Percent:", cpu_percent)
