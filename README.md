🇵🇹 Freguesias SQL Generator
This simple Python script generates a complete SQL INSERT statement for all freguesias (civil parishes) in Portugal.

Portugal has over 3,000 freguesias. Manually creating a database table with all that data would be time-consuming — but with just a few lines of Python, you can generate the entire SQL query in seconds.

🛠 What It Does
Takes a list of freguesia names.

Escapes any special characters (like ') to ensure SQL compatibility.

Outputs a single SQL INSERT query with all freguesias into a file called querie.txt.

Example output:

sql
Copiar
Editar
INSERT INTO freguesias (freguesia) VALUES
  ('A dos Francos (Caldas da Rainha)'),
  ('A dos Negros (Óbidos)'),
  ('Abade de Neiva (Barcelos)'),
  ...
  ('Abiul (Pombal)');
🚀 How to Use
Clone the repo:

bash
Copiar
Editar
git clone https://github.com/your-username/freguesias-sql-generator.git
cd freguesias-sql-generator
Make sure you have Python 3 installed.

Run the script:

bash
Copiar
Editar
python generate_sql.py
The file querie.txt will be created with the full SQL INSERT statement.

📝 Notes
The list of freguesias is included directly in the script (generate_sql.py). You can update or extend it as needed.

Ideal for seeding your database with Portuguese administrative data.

📂 Files

File	Description
generate_sql.py	Python script that generates the SQL query
querie.txt	Output file containing the SQL query
📄 License
MIT — feel free to use, share, and modify.

Let me know if you want to make it bilingual (PT/EN), add a logo, or link to an official list of freguesias.
