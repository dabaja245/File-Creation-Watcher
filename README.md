#File Creation Watcher

This Python script uses the watchdog library to monitor a directory for newly created files. When a new file is detected, it logs the event and appends the file's details (path, timestamp, and event type) to a CSV file. Key features include:

Real-Time Monitoring: The script continuously monitors a specified directory (or the current directory if none is provided).

File Logging: Every time a new file is created, its path and creation time are recorded in a CSV file (created_files.csv).

Custom Event Handler: A custom event handler filters out directories and logs only newly created files.

Error Handling: Handles situations where the CSV file doesn't exist by creating a new one with headers.

Dependencies
watchdog: For file system event monitoring.
pandas: For handling data and appending to CSV.
logging: To log file creation events.


Usage:python file_creation_watcher.py /path/to/directory


