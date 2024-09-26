import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
from datetime import datetime  # Corrected import

def get_file(event):
    data = {
        'file_path': [event.src_path],
        'timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        'event_type': [event.event_type]
    }
    
    new_df = pd.DataFrame(data)
    
    # Append the DataFrame to the existing CSV file
    # Check if file exists to decide whether to write header or not
    try:
        with open("created_files.csv", 'r') as f:
            # If file is not empty, write without header
            new_df.to_csv("created_files.csv", mode='a', index=False, header=False)
    except FileNotFoundError:
        # If file does not exist, write with header
        new_df.to_csv("created_files.csv", mode='a', index=False, header=True)

class CreateOnlyEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        # This method is called when a file or directory is created
        if not event.is_directory:  # Checks if the created object is not a directory
            logging.info(f"Created file: {event.src_path}")
            get_file(event)

if __name__ == "__main__":
    # Set the format for logging info
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Get the path from command line arguments or use the current directory
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    # Initialize the custom event handler that logs only file creations
    event_handler = CreateOnlyEventHandler()

    # Initialize Observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    # Start the observer
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
