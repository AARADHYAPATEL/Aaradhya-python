import psutil

# Get memory information
memory = psutil.virtual_memory()

total_memory = memory.total
available_memory = memory.available
used_memory = memory.used
percent_memory = memory.percent

print("Total Memory:", total_memory)
print("Available Memory:", available_memory)
print("Used Memory:", used_memory)
print("Memory Percent:", percent_memory)
