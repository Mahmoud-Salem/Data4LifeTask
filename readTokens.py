"""
    The DB schema consists of two column one for the token and one for the frequency.
    Insertion of the tokens :
        First check if this token is already existing: 
                Using a dictionary which can check in O(1) for the sake of insertion and clearing it afterwards to free up memory.
            if yes : update the entry by increasing the frequency by 1 
            else : we insert the token by frequency 1 


    Other Approach : Other approach is to store the frequency of the duplicates in memory such as (dictionary, hashmap, redis) and removing frequencies column in table.

    Justification for this approach : 
            * Not using memory storage :
                Storing frequencies in memory is faster than in disk and can free some disk by deleting frequency column.
                However, In real-life situation :
                    Firstly, the list of duplicates should be presistent data ,so it should not be on memory
                        considering the occurence of some issues to the server, which will lead for the data to be lost .
                    Secondly, Caching so much data can take much space, which can lead the system to run out of memory
                        and considering if in some situations the duplicates are in huge numbers such as if every token is repeated once
                        it will eventually leads to 5 millions token stored in memory. Thus it could go worse with >10m .
            * Getting duplicates from the DB :
                The frequency column has a B-Tree index.
                B-tree index is effecient in getting range queries as the query is a range query where frequency > 1 
                which helps the fetching to quickly skipped all entries with frequency = 1 and start from the leaf node that >1 
                and just return all entries from there .
"""

import psycopg2


# Connect to the database .
def connectToDB():
    database = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    print('Successfully connected to the postgres database')
    cursor = database.cursor()
    return database, cursor




# inserting tokens to the tokens table 
def insertToDB(database,cursor,generatedTokens):
    # to keep track of number of duplicates and progress
    insertions= 0
    updates =0 
    progress =0 
    # dictionary is used to check if token already in the db instead of checking with query to speed up checking 
    existing = {}
    for token in generatedTokens :
        progress+=1 
        print("progress :"+str(progress)+" out of "+str(10000000))
        token = token.strip("\n")
        # query to check if this token exists
        if (token not in existing):
            insertions+=1
            insertQuery = "INSERT INTO tokens ( token, frequency ) VALUES ('"+token+"',1);"
            cursor.execute(insertQuery)
            existing[token] = 1
        else :
            updates+=1
            existing.update({token : existing.get(token)+1 })
            current = str(existing.get(token)) 
            updateQuery = "UPDATE tokens SET frequency = "+current+" WHERE token = '"+ token+"';"
            cursor.execute(updateQuery)
    # Clearing cached tokens to free up memory.
    existing.clear()
    # commit the transaction to the db .
    database.commit()
    print('number of unique insertions :'+ str(insertions))
    print('number of updates : '+ str(updates))
    print('Tokens added to the database successfully')



# returning all the duplicate tokens in the table 
def getDuplicates(cursor):
    query = "SELECT * FROM tokens WHERE frequency > 1 ;"
    cursor.execute(query)
    duplicates = cursor.fetchall()
    return duplicates



# Open the file to read from it .
generatedTokens = open("tokens.txt", "r")
database,cursor = connectToDB()
insertToDB(database,cursor,generatedTokens)
duplicates = getDuplicates(cursor)
print(duplicates)

