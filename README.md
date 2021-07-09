# Data4LifeTask
  Service for Reading a file containing random tokens and store them in the database as quickly and efficiently as possible
  
  without storing any token twice and create a list of all non-unique tokens. 
  
  
  Technologies used : Python 3 , PostgreSQL 
  
  
## generateTokens.py :

Responsible for generating file with 10 million random tokens .
> Python3 generateTokens.py
    
## readTokens.py

Responsible for reading tokens from file and storing it in the database .
> Python3 readTokens.py

## database.sql :

Responsible for creating postgres tables .
