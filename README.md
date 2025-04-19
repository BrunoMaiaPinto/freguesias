Freguesias SQL Generator

This simple Python script generates a complete SQL INSERT statement for all freguesias (civil parishes) in Portugal.

Portugal has over 3,000 freguesias. Manually creating a database table with all that data would be time-consuming — but with just a few lines of Python, you can generate the entire SQL query in seconds.

🛠 What It Does
Fetches a list of freguesia names from the GeoAPI.

Writes a single SQL INSERT statement into a file called querie.txt.

If the API is unreachable (due to no internet or server issues), the script automatically falls back to a local list of freguesias in freguesiasList.py.
