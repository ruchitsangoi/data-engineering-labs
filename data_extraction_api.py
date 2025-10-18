import requests
import pandas as pd

# Example public API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# Check for success
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv("users_data.csv", index=False)
    print("✅ Data extracted and saved as users_data.csv")
else:
    print("❌ Failed to fetch data:", response.status_code)
