import psutil

# Kill a process
pid_to_kill = 13140
# Replace with the process ID to kill
process_to_kill = psutil.Process(pid_to_kill)
process_to_kill.terminate()
