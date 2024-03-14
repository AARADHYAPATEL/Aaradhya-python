import psutil

# Get information for a specific process
pid = 1132
process = psutil.Process(pid)

print("Process Name:", process.name())
print("Process Status:", process.status())
print("Process CPU Percent:", process.cpu_percent(interval=1))
print("Process Memory Info:", process.memory_info())
