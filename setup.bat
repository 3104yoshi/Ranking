python3 -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python3 .\db\accessor\createDB.py

python3 .generateSecretKey.py