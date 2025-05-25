# magazine-code
This project models the relationship between Authors, Articles, and Magazines using Python and a SQL database.

An Author can write many Articles

A Magazine can publish many Articles

Each Article belongs to one Author and one Magazine

# Features
Raw SQL queries within Python classes

Full CRUD and relationship methods for all models

Database schema and seed scripts included

Example scripts to set up, seed, and query the database
# Installations
### OPTION 1
1. Install dependencies
```pipenv install pytest sqlite3```
2. Activate the virtual environment
```pipenv shell```
### OPTION 2
1. Create a virtual environment
python -m venv env
2. Activate virtual environment (Mac/Linux)
source env/bin/activate
#### OR (Windows)
#### env\Scripts\activate
3. Install dependencies
pip install pytest

# running the code 
To run this program ensure you are in the parent folder this is ```user:~/magazine-code/magazine-coding$```

Run this scripts in the terminal:
``` 
PYTHONPATH=. python scripts/setup_db.py
PYTHONPATH=. python -m lib.db.seed
PYTHONPATH=. python scripts/run_queries.py 
```

