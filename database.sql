

/* 
    Creating table with two attributes :
        1- token which is a string of size 7 -- the token to be saved.
        2- frequency which is a integer -- the frequency of the token.
    Primary key on token : token are unique and always not null so it can be used as primary key 
                  sql put default index on primary key for quick searching.

    Btree index on frequency : when getting the duplicates tokens it can helps to optimize the query 
                               because the query is a range query it can jumps to the first leaf node with freq >1
                               and return all the leaf nodes to the right .

*/
CREATE TABLE tokens (
   token CHAR(7) PRIMARY KEY,
   frequency INT NOT NULL
);

CREATE INDEX btree_freq ON tokens USING btree (frequency) ;