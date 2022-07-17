from datetime import datetime

# Create function to return datetime across the entire project
def create_timestamp_value():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"