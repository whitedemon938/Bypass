gunicorn -b :$PORT app:app & python3 update.py && python3 -m Bypass & python3 alive.py
