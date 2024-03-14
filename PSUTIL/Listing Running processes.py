import psutil

# List running processes
for process in psutil.process_iter():
    print(process.pid, process.name())
