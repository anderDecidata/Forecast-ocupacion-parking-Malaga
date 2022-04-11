# Load libraries
from datetime import datetime
import os
import pandas as pd
import yaml

# Load parameters
params = yaml.safe_load(open('params.yaml'))['data_extract']

# Set data
url = params['url']
path = params['path']
filename = params['filename']
output_path = path + '/' + filename

# Extract raw data
data = pd.read_csv(url)

# Add Timestamp
data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:00:00')

# Create folder if it does not exist
os.makedirs(path, exist_ok=True)

# Check if file exists in path
if filename not in os.listdir(path):
    # If it does not exist, save it
    data.to_csv(output_path, index = False)

else:
    # If exists, append it
    previous = pd.read_csv(output_path)
    complete = pd.concat([previous, data])
    complete.to_csv(output_path, index = False)
