import requests

try:
  res = requests.get('https://json.geoapi.pt/freguesias', timeout=10)
  res.raise_for_status()
  freguesias = res.json()
except Exception as e:
  print(f'{e}')
  from freguesiasList import freguesias
  

with open("querie.txt", "w", encoding="utf-8") as f:
    f.write("INSERT INTO freguesias (freguesia) VALUES \n")

    for i, freguesia in enumerate(freguesias):
        safe_freg = freguesia.replace("'", "''")
        line_end = ",\n" if i < len(freguesias) - 1 else ";\n"
        f.write(f"  ('{safe_freg}'){line_end}")