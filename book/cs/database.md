# Database

* 6V of Big data
  * Volumes : brings cost, scalability, and performance related to their storage access and processing
  * Variety : structure (formats, models), media, semantic(interpret), availability(realtime vs intermittent)
  * Velocity : Data is being generated at an alarming rate (batch processing vs real-time processing)
  * Veracity : Uncertainty and inconsistencies in the data (data provenance)
  * Valence : Connectedness of big data in form of graphs (Complex Data Exploration Algorithm)
  * Value : Finding correct meaning out of the data

> Question

* How to solve challenges in big data integration?
  * Probabilistic Schema Mapping vs Pay-as-you-go Model

* 5 key points in order to categorize big data systems?
  * Execution model, Latency, Scalability, Programming Language, Fault Tolerance

* Why do companies use big data?
  * Higher scales | Improved Safety | Customer Satisfaction | Better Profit Margins
  * Efficient operations | Improved Product Placement (Personalized marketing)

* Why is it rising?
  * Access of larger storage becomes easier for everyone

* Why is mobile advertising related to big data?
  * Mobile advertising benefits from data integration with location which requires big data

* What are Big data policies?
  * privacy and lifetime | interoperability and regulation | curation and quality

* What is denormalization of data?
  * improve the read performance, at expense of write performance, add redundant copies | grouping data

* Three types of source
  * Business data | Sensor data | User data

* Things to take account
  * Frequency of updates | Consolidation rule → linking, missing data, dirty data (negative age)

| Sql                       | NoSQL                                                          |
| ------------------------- | -------------------------------------------------------------- |
| ACID compliance           | scalability (variaty of data), processing speed (high traffic) |
| structured and unchanging | cloud computing, storage / Rapid development                   |

> Terms

* Data parallelism
  * parallelization across multiple processors focusing on distributing data across different nodes
  * can be applied on regular data structures like arrays and matrices by working on each element in parallel

* Data Science

![](images/20210304_233946.png)

* Dashboard
  * automatic data pipelines : dashboard
  * promotes trasnparency, accountability
  * purpose, scope, layout + flow, consistent naming structure

* ETL (Extraction, Translation, Loading)

![](images/20210304_233925.png)

* Execution model
  * Batch vs Streaming

* integration
  * Reduce data complexity | Adds value to data | Increase collaboration, availability | Unify data system
  * combining data from different sources into a single, unified view

* Lambda Architecture
  * data-processing architecture designed to handle massive quantities of data both batch, stream processing

* Latency
  * Low : Game, Traffic
  * High : Search engine indexing

* ORM (Object Relation Mapping)
  * Remove dependency : Doesn't depends on speicific database (MySQL, MongoDB)
  * Reduce error, automatically detect changes

* Schema on read
  * creates the schema only when reading the data → NoSql

* Schema on write
  * defined as creating a schema for data before writing into the database → SQL

* smart
  * Connect with other devices and have knowledge of the environment.

* in situ
  * Bringing the computation to the location of the data.

* rollback
  * process that reverts writes operations to ensure the consistency of all replica set members

* sharding
  * architecture that partitions data by key ranges, distributes data among two or more database instances
  * enables horizontal scaling

* Transaction
  * a single logical operation on the data → must provide ACID

> Types

* Lake
  * vast pool of raw data, the purpose for which is not yet defined

* Warehouse
  * repository for structured, filtered data that has already been processed for a specific purpose

* Silo
  * Data produced from an organization that is spread out
  * Bad unsynchronized and invisible data

![](images/20210304_233808.png)

> Property

* CAP
  * Can only achieve two of following
  * Consistency : Every read receives the most recent write or an error
  * Availability : Every request receives response, without guarantee that it contains the most recent write
  * Partition : Continues to operate despite any number of messages dropped by network between nodes

![](images/20210304_233840.png)

* ACID
  * Atomicity : all changes that we need to do for these promotions must happen altogether
  * Concurrency : multiple people updating a database simultaneously
  * Isolation : context of concurrency, multiple people updating a database simultaneously
  * Durability : once a transaction has been committed, it will remain so

* BASE
  * Basic Availability, Soft state, Eventual Consistency

* Fault Tolerance
  * enables a system to continue operating properly in the event of the failure of some of its components
  * Commodity cluster \(redundant data storage\)

> Providers

* IaaS
  * User must install and maintain an operating system, and other applications
  * virtual machines, servers, storage, load balancers, network
  * Amazon EC2 cloud
* PaaS
  * Provided with entire computing platform
  * Execution runtime, database, web server, development tools
  * Google App engine, Microsoft Azure
* SaaS
  * cloud service provides hardware, software environment \(operating system, application software\)
  * Dropbox

> Roles

* Data Analyst
  * Discover Problem & Potential solution → Visualize, dashboard
  * Focus on Past & Present
* Scientist
  * Modeling
* Data Engineer
  * Data Architecture, Database maintenance \(Schema\), quality and pipelines

* BDMS
  * Continuous data ingestion
  * Support for common “Big Data” data types
  * A full query language
  * A flexible semi-structured data model

> B tree

* B tree
  * Every node has at most M children
  * Every internal node has at least ⌈M|2⌉children
  * The root has at least 2 children if it is not a leaf
  * An internal node with k children contains k - 1 keys
  * All leaves appear on the same level of the tree
  * Property
  * parameter n: a node holds n search key values (sorted) and n+1 pointers (to interior nodes or records)
  * left key ≤ pointed-to value < right key
  * choose n so large that a node fits in a block
  * interior node    # between half and all of the n+1 pointers are used
  * leaf node    # rightmost pointer to the next leaf

* B+ Tree
  * Internal nodes contain only search keys (no data)
  * leaves have at least ⌈L | 2⌉ keys up to L keys
  * Balanced (equal length paths) trees for minimizing disk I|O
  * logarithmic levels maintained w.r.t. size of the data file
  * no overflow blocks (but insert, delete more complex)
  * guaranteed upper limits on access, insert, delete times
  * data file not sorted, then leafs have to constitute a dense index
  * data file sorted, then leafs may constitute a sparse index
  * number of children for a node, ⌈b | 2⌉ m  b     (only root can have two children)
  * In order to access a particular byte, track #, sector #, offset needed.
  * Each block usually contains 512 bytes.
  * Data must be brought to main memory (RAM)

![](images/20210305_193812.png)

## Sql

* Language used to access and control RDBMSs
* Set up databases and modify them, as well as accessing them
* MySQL, Oracle, MS SQL Server, SQLite, Postgres, and MariaDB
* SQL are vertically scalable, increasing the horsepower \(higher Memory, CPU, etc.\) of the hardware
* Joins can be costly
* What does it mean for a query to be declarative?
  * Language specifies what data to obtain
* What is a global indexing table?
  * An index table in order to keep track of a given data type that might exist within multiple machines.
* Aggregate
  * A function that combines multiple values to produce a single new value
  * AVG, COUNT, MAX, MIN, SUM

> RDBMS

* ACID(Atomicity, Consistency, Isolation, Durability) Compliance
* Declarative query languages → No need to tell how to extract | join
* software package designed to define, manipulate, retrieve, manage data in a database
* Solve data redundancy | inconsistency | difficulty in accessing | Integrity | atomicity of updates
* Concurrent access by users | Security | Provide meaning-based view of data | Support operations on data
* consistent data without massive growth that would require more servers
* useful for rapid development as it doesn’t need to be prepped ahead of time

{% tabs %}
{% tab title='comment.sql' %}

```sql
-- single line comment
/* multi-line
   coment */
```

{% endtab %}
{% endtabs %}

> Terms

* Constraints
  * PRIMARY, FOREIGN, UNIQUE, CHECK, NOT NULL
* Key
  * Alternative : combination of columns that could be a primary key, but isn't
  * Candidate : Minimal Super Keys
  * Foriegn
    * FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
    * PersonID column in the Orders table is a FOREIGN KEY in the Orders table
  * Primary : Chosen candidate keys
    * cannot have null values in any tuple, table can have only one primary
  * Super : A set of attributes SK of R such that no two tuples in any valid
    * relation instance r(R) will have the same value for SK
  * composite : a candidate key that consists of two or more attributes (table columns) that together uniquely identify an entity occurrence (table row)
  * compound : a composite key for which each attribute that makes up the key is a simple (foreign) key in its own right

![Key](images/20210325_232848.png)

* Non-prime attribute
  * Attributes which are not part of any candidate key

* Query
  * correlated : contains a subquery that requires information from a query one level up

* Repeated fields
  * Optimize repeating duplicate infromation to speed up query

> Errors

* Data truncated for column 'authProvider' at row 1
  * Your problem is that at the moment your incoming_Cid column defined as CHAR(1) when it should be CHAR(34).

> Index

* Data structures used for quickly locating tuples that meet a specific type of condition
ex) equality, range
* Many types of indexes. Evaluate them on access, insertion, deletion item, Disk Space needed

* Primary index
  * the index on the attribute (a.k.a. search key) that determines the sequencing of the table on disk

* Secondary index
  * index on any other attribute

* Dense index
  * every value of the indexed attribute appears in theindex

* Sparse index
  * many values do not appear

* insertion
  * if no new block is created then do nothing else create an index entry with the new value
  * how to find space: find nearby free space and slide blocks backward, or use an overflow block

* deletion
  * if the deleted entry appears in the index replace it with the next search-key value 
  * (leave deleted value assuming no part of the system assume it still exists without checking the block)

* Multi-level indices
  * treat the index as data and build an index on it

> Null

* Null Check # A is null, A is not null
* Arithmetic operations involving any null return null
* Comparisons involving null return unknown new truth value
* Aggregate will ignore null values
* Null is treated like any other value in group-by

```sql
SELECT name FROM employee WHERE salary <= 100 OR salary > 100   -- ignore name with null salary
SELECT count(*) FROM customer   -- Count total number of customers
       count(credit)            -- Count number of customers who have credit
```

> UDF

```sql
CREATE TEMP FUNCTION DATE_FORMAT(x STRING) AS (CAST(CONCAT(SUBSTR(x, 0, 4), '-', SUBSTR(x, 5, 2), '5', SUBSTR(x, 7)) AS DATE));
```

> MySQL

```text
mysql -u user -p -e 'show databases;'

# mysql
SHOW DATABASES / SCHEMAS;
```

> Big Query

* FORMAT_TIMESTAMP("%F", timestamp, "America/Los_Angeles") AS purchase_date

{% tabs %}
{% tab title='big_query.sql' %}

```sql
CREATE OR REPLACE TABLE
```

{% endtab %}
{% endtabs %}

> Relational algebra

```txt
// Find directors of current movies
{t: title | $$ \exists $$ s $$ \in $$ schedule [s(title) = t(title)]}

// Find the titles and the directors of all currently playing movies
{t: title, director | ∃s ∈schedule ∃m ∈ movie [s(title) = m(title) ∧ t(title) = m(title) ∧ t(director) = m(director)]}

// Find actors playing in every movie by Berto
{ a : actor |  y  movie [a(actor) = y(actor) m movie [m(dir) = ”Berto” t movie(m(title) = t(title)  t(actor) = y(actor))]]}
```

### Design

> Term

* Functional Dependency
  * A->B holds if two tuples having same value of attribute A also have same value for attribute B

| STUD_NO | STUD_NAME | STUD_PHONE | STUD_STATE | STUD_COUNT RY | STUD_AG E |
| ------- | --------- | ---------- | ---------- | ------------- | --------- |
| 1       | RAM       | 9716271721 | Haryana    | India         | 20        |
| 2       | RAM       | 9898291281 | Punjab     | India         | 19        |
| 3       | SUJIT     | 7898291981 | Rajsthan   | India         | 18        |
| 4       | SURESH    |            | Punjab     | India         | 21        |

* Functional Dependencies STUD_NO->STUD_NAME, STUD_NO->STUD_PHONE hold but STUD_NAME->STUD_STATE do not hold

* Normalize
  * process of minimizing redundancy from a relation or set of relations

* One to Many

![](images/20210321_212309.png)

* Many to Many
  * Requires intermediary table

![](images/20210321_212400.png)

> First Normal Form

* Relation is in first normal form if it does not contain any composite or multi-valued attribute
* There are only Single Valued Attributes.
* Attribute Domain does not change.
* There is a Unique name for every Attribute/Column.
* The order in which data is stored, does not matter.

| STUD_NO | STUD_NAME | STUD_PHONE             | STUD_STATE | STUD_COUNTRY |
| ------- | --------- | ---------------------- | ---------- | ------------ |
| 1       | RAM       | 9716271721, 9871717178 | HARYANA    | INDIA        |
| 2       | RAM       | 9898297281             | PUNJAB     | INDIA        |
| 3       | SURESH    |                        | PUNJAB     | INDIA        |

* Multi-valued attributes in the table

| STUD_NO | STUD_NAME | STUD_PHONE | STUD_STATE | STUD_COUNTRY |
| ------- | --------- | ---------- | ---------- | ------------ |
| 1       | RAM       | 9716271721 | HARYANA    |              |
| 1       | RAM       | 9871717178 | HARYANA    | INDIA        |
| 2       | RAM       | 9898297281 | PUNJAB     | INDIA        |
| 3       | SURESH    |            | PUNJAB     | INDIA        |

> Second Normal Form

* a relation must be in first normal form and relation must not contain any partial dependency
* dependent on any proper subset of any candidate key of the table
* [-] If we update only one tuple and not the other, the database would be in an inconsistent state.

* Question: Make following table into 2NF

| STUD_NO | COURSE_NO | COURSE_FEE |
| ------- | --------- | ---------- |
| 1       | C1        | 1000       |
| 2       | C2        | 1500       |
| 1       | C4        | 2000       |
| 4       | C3        | 1000       |
| 4       | C1        | 1000       |
| 2       | C5        | 2000       |

* COURSE_FEE cannot alone decide the value of COURSE_NO or STUD_NO;
* COURSE_FEE together with STUD_NO cannot decide the value of COURSE_NO;
* COURSE_FEE together with COURSE_NO cannot decide the value of STUD_NO;
* COURSE_FEE would be a non-prime attribute, as it does not belong to one only candidate key {STUD_NO, COURSE_NO}
* But, COURSE_NO -> COURSE_FEE, which is a proper subset of the candidate key
* Non-prime attribute COURSE_FEE is dependent on a proper subset of the candidate key, which is a partial dependency and so this relation is not in 2NF.

| Table 1 |           | Table 2   |
| ------- | --------- | --------- | ---------- |
| STUD_NO | COURSE_NO | COURSE_NO | COURSE_FEE |
| 1       | C1        | C1        | 1000       |
| 2       | C2        | C2        | 1500       |
| 1       | C4        | C3        | 1000       |
| 4       | C3        | C4        | 2000       |
| 4       | C1        | C5        | 2000       |
| 2       | C5        |

* Third Normal Form
  * reduce the duplication of data, avoid data anomalies, ensure referential integrity, simplify data management
  * free of insertion, update, deletion anomalies, and ensures functional dependency preserving and lossless

| STUD_NO | STUD_NAME | STUD_STATE | STUD_COUNTRY | STUD_AGE |
| ------- | --------- | ---------- | ------------ | -------- |
| 1       | RAM       | HARYANA    | INDIA        | 20       |
| 2       | RAM       | PUNJAB     | INDIA        | 19       |
| 3       | SURESH    | PUNJAB     | INDIA        | 21       |

* {STUD_NO -> STUD_NAME, STUD_NO -> STUD_STATE, STUD_STATE -> STUD_COUNTRY, STUD_NO -> STUD_AGE}

```sql
STUDENT (STUD_NO, STUD_NAME, STUD_PHONE, STUD_STATE, STUD_AGE)
STATE (STATE, COUNTRY)
```

* Algebra

* Projection

$$ \pi%0 $$

* Selection

$$ \sigma $$

* Union

$$ \cup $$

* Difference

$$ - $$

* Join

$$ \bowtie $$

* Attribute Renaming

$$ \delta $$

> Calculus

```sh
# Find theaters showing movies by Bertolucci
{t : theater |  s ∈ schedule  m ∈ movie
  [t(theater) = s(theater) ∧ s(title) = m(title) ∧ m(director) = Bertolucci}

# Find the titles of all movies by “Berto”
{t: title| ∃m ∈ movie [m(director) = “Berto” ∧ t(title) = m(title)]}

# Find the pairs of actors acting together in some movie
π actor 1, actor2 ( δactor → actor1 (movie) ⋈ δactor → actor2( movie ) )

# Find the actors playing in every movie by Berto
π actor ( movie ) - πactor [ ( πactor ( movie ) ⋈ πtitle ( σdir=BERTO( movie ) ) ) - πactor, title( movie ) ]

# Find the actors playing in every movie by Berto
π title,actor(movie) ÷ πtitle(σdir=berto(movie))

# Find the names of customers who took every loan.
π cname,lno(borrower) ÷ π lno(δ no → lno(loan))     # fail when loan is empty
π name(customer) - πname ( πname(customer) ⋈ πno(loan) - δcname→name, lno→no(πcname,lno(borrower)) )

# List the directors such that every actor is cast in one of his|her movies.
π director,actor(movie) ÷ πactor(movie).        # fail when there is no actor
π director(movie) − πdirector[πdirector(movie) ⋈ πactor(movie) − πdirector,actor(movie)]

# The directors of all movies playing elsewhere than Hillcrest
π director[σtheater ≠ ‘Hillcrest’(movie ⋈ schedule)]    || expensive join
π director[π title, director(movie) ⋈ πtitle(σtheater ≠ 'Hillcrest'(schedule))]

# List the drinkers that frequent only bars that serve some beer that they like.
# (Assume each drinker likes at least one beer and frequents at least one bar.)
[frequents | drinker bar]
[serves | bar beer]
[likes | drinker beer]

πdrinker(frequents) − πdrinker[frequents−πdrinker,bar(serves ⋈ likes)]

# List the drinkers that frequent no bar that serves a beer that they like
πdrinker(frequents) − πdrinker(frequents ⋈ serves ⋈ likes)
```

### Create

> Database

{% tabs %}
{% tab title='create_insert.sql' %}

```sql
Create database
CREATE DATABASE name
    [ [ WITH ] [ OWNER [=] user_name ]
           [ TEMPLATE [=] template ]
           [ ENCODING [=] encoding ]
           [ LC_COLLATE [=] lc_collate ]
           [ LC_CTYPE [=] lc_ctype ]
           [ TABLESPACE [=] tablespace ]
           [ CONNECTION LIMIT [=] connlimit ] ]

INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

-- Insert into table
INSERT INTO movie VALUES ("kim", "monster", 2016)

-- Insert with null values
INSERT INTO movie(title) VALUES ("Harry Potter")

-- Result of query for insertion
INSERT INTO r SELECT ... FROM ... WHERE
```

{% endtab %}
{% tab title='create_tables.sql' %}

```sql
CREATE TABLE DEPT
( DNAME VARCHAR(10) NOT NULL,
DNUMBER INTEGER NOT NULL,
MGRSSN CHAR(9),
MGRSTARTDATE CHAR(9),
PRIMARY KEY (DNUMBER),
UNIQUE (DNAME),
FOREIGN KEY (MGRSSN) REFERENCES EMP ) ;

CREATE TABLE customer (
  name varchar(255) primary key,
  credit integer
);

CREATE TABLE loan (
  no varchar(255) primary key,
  type varchar(255),
  minCredit integer
);

CREATE TABLE borrower (
  cname varchar(255) primary key,
  lno varchar(255),
  due date,
  FOREIGN KEY (cname) REFERENCES customer(name),
  FOREIGN KEY (lno) REFERENCES loan(no)
);

INSERT INTO customer (name, credit) VALUES
  ('sean', 1),
  ('tom', 2),
  ('jason', 3);

INSERT INTO loan (no, type, minCredit) VALUES
  ('jumbo mortgage', 'student', 1),
  ('b', 'y', 2),
  ('c', 'z', 3);

INSERT INTO borrower (cname, lno, due) VALUES
  ('sean', 'jumbo mortgage', '1-1-1'),
  ('tom', 'jumbo mortgage', '2-2-2'),
  ('jason', 'c', '3-3-3');
```

{% endtab %}
{% endtabs %}

> View

```sql
CREATE VIEW Berto-Movies AS SELECT title FROM Movie WHERE director = 'Berto';

-- Return the teams defeated only by the leading teams
CREATE VIEW Leaders (name) AS
  SELECT s.name FROM Standings s
  WHERE NOT EXISTS
  (SELECT * FROM Standings s1 WHERE s.points < s1.points)

SELECT name FROM Teams
  WHERE name NOT IN
    (SELECT t.name FROM Teams t, Matches m
    WHERE t.name = m.aTeam AND m.aScore < m.hScore AND m.hTeam NOT IN Leaders
           OR  t.name = m.hTeam AND m.hScore < m.aScore AND m.aTeam NOT IN Leaders)
```

> Index

```sql
CREATE INDEX index_name ON table_name (column_name);
CREATE INDEX index_name ON table_name (column1, column2, ...);
```

> Delete

```sql
DELETE FROM table        -- Delete Everything
```

> Drop

```sql
DROP TABLE table_name;   -- Drop table

-- ALL databases where the role owns anything or has any privileges
DROP OWNED BY ryan;
DROP USER ryan;
```

> TRUNCATE

```sql
TRUNCATE TABLE <table_name>    -- Clear Table
```

> INSERT

```sql
INSERT INTO loan (no, type, minCredit) VALUES
  ('jumbo mortgage', 'student', 1),
  ('b', 'y', 2),
  ('c', 'z', 3);
```

> Alter

```sql
ALTER TABLE table_name ADD column_name d_type DEFAULT 3;  -- Add Column
ALTER TABLE table_name RENAME TO new_table_name;          -- Change table name
ALTER table PERSON ADD primary key (persionId,Pname,PMID) -- Add primary key
```

### Read

```sql
SELECT credit, count(credit) C FROM customer GROUP BY credit
```

| credit | C   |
| ------ | --- |
| 100    | 2   |
| Null   | 3   |

{% tabs %}
{% tab title='table_existence.sql' %}

```sql
-- Check existence of tables
select exists(select * from information_schema.tables where table_name='dictionary');
SELECT DISTINCT name AS n                # Find all unique names
SELECT COUNT(distinct(l.type)) FROM bank.loan l        # Count number of type from loan
```

{% endtab %}
{% endtabs %}

> Where

```sql
LIKE           -- % any string, _ any character
WHERE A and B  -- where A in (where B)
EXIST <query>  -- Check the result of <query> is non-empty

-- Multiple equality
LEAST(a, b, c, d, e) = GREATEST(a, b, c, d, e)

-- Find theaters showing movies by Bertolucci
SELECT s.theater FROM schedule s, movie m
  WHERE s.title = m.title AND m.director = “Bertolucci”

-- Find 11- 20th row
SELECT name FROM mydb ORDER BY score DESC LIMIT 10,10;

-- SELECT o.OrderId, maximum(o.NegotiatedPrice, o.SuggestedPrice) FROM Order o
SELECT
  o.OrderId,
  CASE WHEN o.NegotiatedPrice > o.SuggestedPrice THEN o.NegotiatedPrice
     ELSE o.SuggestedPrice
  END
FROM Order o

-- Get overlap between (begin <> end) and start <> finish
SELECT SUM(1 + GREATEST( datediff( LEAST(Book.endDate, finishDate), GREATEST(Book.beginDate, startDate)), -1 ))
  FROM Book WHERE Book.roomID = Room.id

-- Customers’ credit rating may decrease after they get a loan.
-- Find (customer, loan) pairs that no longer satisfies minimum credit required by loan (name, no).
SELECT c.name as name, l.no as no FROM bank.customer c, bank.loan l WHERE c.credit < l."minCredit";
```

* WITH
  * Exists only in single query

```sql
-- Create a temporary table
WITH berto-movies AS SELECT title FROM movie WHERE director = 'berto'

SELECT m.actor FROM Movie m, berto-movies WHERE berto-movies.title NOT IN
  (SELECT title FROM movies WHERE actor = m.actor)

-- List the loan type(s) with the smallest number of borrowers. (loanType)
SELECT l.no as loanType FROM bank.loan l LEFT JOIN bank.borrower b ON l.no = b.lno
  GROUP BY l.no ORDER BY COUNT(b.lno) LIMIT 1;
```

* If

```sql
SELECT IF(500<1000, "YES", "NO");
```

* HAVING
  * Used with group by

* GROUP BY
  * Any aggregated term can appear in a HAVING clause.
  * Null group-by attributes are treated like any other value

* Date Range

| ID  | Qty | From_date  | To_date    |
| --- | --- | ---------- | ---------- |
| 3   | 12  | 2013-01-05 | 2013-01-07 |
| 6   | 22  | 2013-01-06 | 2013-01-10 |
| 8   | 11  | 2013-02-05 | 2013-02-11 |

```sql
-- sales data from 2013-01-03 to 2013-01-09
SELECT * FROM Product_sales
  WHERE NOT (From_date > @RangeTill OR To_date < @RangeFrom)
```

![overlap](images/20210218_145536.png)

```sql
-- check range overlap
SELECT * FROM tbl WHERE existing_start BETWEEN $newSTart AND $newEnd OR
                        $newStart BETWEEN existing_start AND existing_end
```

> Group

```sql
-- daily visit
SELECT date, source.medium, COUNT(DISTINCT(visiterId)) AS visits FROM table, GROUP BY 1, 2 ORDER BY 1 DESC, 2;
```

> Sum

* 0 if negative

```sql
SUM(GREATEST(ordered_item.amount, 0)) as purchases
```

* sum vs +

| ID  | VALUE1 | VALUE2 |
| --- | ------ | ------ |
| 1   | 1      | 2      |
| 1   | 2      | 2      |
| 2   | 3      | 4      |
| 2   | 4      | 5      |

```sql
SELECT  ID, SUM(VALUE1), SUM(VALUE2) FROM tableName GROUP BY ID
```

| ID  | SUM(VALUE1) | SUM(VALUE2) |
| --- | ----------- | ----------- |
| 1   | 3           | 4           |
| 2   | 7           | 9           |

```sql
SELECT  ID, VALUE1 + VALUE2 FROM TableName
```

| ID  | VALUE1 + VALUE2 |
| --- | --------------- |
| 1   | 3               |
| 1   | 4               |
| 2   | 7               |
| 2   | 9               |

```sql
SELECT ID, SUM(VALUE1 + VALUE2) FROM tableName
  GROUP BY ID
```

| ID  | SUM(VALUE1 + VALUE2) |
| --- | -------------------- |
| 1   | 7                    |
| 2   | 16                   |

> cast

* CONVERT allows more options, such as changing character set with USING.

```sql
SELECT * FROM contacts WHERE contact_id BETWEEN 100 AND 200;

-- SQL Server string to date / datetime conversion - datetime string format sql server
-- MSSQL string to datetime conversion - convert char to date - convert varchar to date
-- Subtract 100 from style number (format) for yy instead yyyy (or ccyy with century)
SELECT convert(datetime, 'Oct 23 2012 11:01AM', 100) -- mon dd yyyy hh:mmAM (or PM)
SELECT convert(datetime, 'Oct 23 2012 11:01AM') -- 2012-10-23 11:01:00.000

-- Without century (yy) string date conversion - convert string to datetime function
SELECT convert(datetime, 'Oct 23 12 11:01AM', 0) -- mon dd yy hh:mmAM (or PM)
SELECT convert(datetime, 'Oct 23 12 11:01AM') -- 2012-10-23 11:01:00.000

-- Convert string to datetime sql - convert string to date sql - sql dates format
-- T-SQL convert string to datetime - SQL Server convert string to date
SELECT convert(datetime, '10/23/2016', 101) -- mm/dd/yyyy
SELECT convert(datetime, '2016.10.23', 102) -- yyyy.mm.dd ANSI date with century
SELECT convert(datetime, '23/10/2016', 103) -- dd/mm/yyyy
SELECT convert(datetime, '23.10.2016', 104) -- dd.mm.yyyy
SELECT convert(datetime, '23-10-2016', 105) -- dd-mm-yyyy

-- mon types are nondeterministic conversions, dependent on language setting
SELECT convert(datetime, '23 OCT 2016', 106) -- dd mon yyyy
SELECT convert(datetime, 'Oct 23, 2016', 107) -- mon dd, yyyy

-- 2016-10-23 00:00:00.000
SELECT convert(datetime, '20:10:44', 108) -- hh:mm:ss
```

### Join

![alt](images/20210212_024840.png)

```sql
Natural [ (FULL | LEFT | RIGHT) OUTER | INNER ] JOIN table_name ON _.a = _.b
```

> Semijoin

* step includes Project, Ship, Reduce
* increase the efficiency of sending data across multiple machines

> Natural Join

* associated tables have one or more pairs of identically named columns
* Equivalent to “on c1 and c2” and “using (c1, c2)”

```sql
-- Find the director of all movies showing in seoul
SELECT director FROM movie
  NATURAL JOIN schedule WHERE theater = 'seoul'
```

> Left Join

* returns all records from the left table (table1), and the matched records from the right table (table2)
* The result is NULL from the right side, if there is no match.

```sql
-- Find for each customer number of taken loans. If no loans, with zero. (name, loanCount).
SELECT c.name as name, COUNT(b.cname) as loanCount FROM bank.customer c
  LEFT JOIN bank.borrower b ON c.name = b.cname
  GROUP BY c.name;

-- List customers who took every type of loan (at least one loan from every type) (name)
SELECT c.name as name FROM bank.customer c
  LEFT JOIN bank.borrower b ON c.name = b.cname
  GROUP BY c.name HAVING COUNT(b.cname) = (SELECT COUNT(*) FROM bank.loan);
```

> Right Join

* returns all records from the right table (table2), and the matched records from the left table (table1)
* The result is NULL from the left side, when there is no match

| OrderID | CustomerID | EmployeeID | OrderDate  | ShipperID |
| ------- | ---------- | ---------- | ---------- | --------- |
| 10308   | 2          | 7          | 1996-09-18 | 3         |
| 10309   | 37         | 3          | 1996-09-19 | 1         |
| 10310   | 77         | 8          | 1996-09-20 | 2         |

| EmployeeID | LastName  | FirstName | BirthDate | Photo      |
| ---------- | --------- | --------- | --------- | ---------- |
| 1          | Davolio   | Nancy     | 12/8/1968 | EmpID1.pic |
| 2          | Fuller    | Andrew    | 2/19/1952 | EmpID2.pic |
| 3          | Leverling | Janet     | 8/30/1963 | EmpID3.pic |

```sql
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName FROM Orders
  RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
  ORDER BY Orders.OrderID;
```

| OrderID | LastName  | FirstName |
| ------- | --------- | --------- |
| Null    | West      | Adam      |
| 10248   | Buchanan  | Steven    |
| 10249   | Suyama    | Michael   |
| 10250   | Peacock   | Margaret  |
| 10251   | Leverling | Janet     |
| 10252   | Peacock   | Margaret  |
| 10253   | Leverling | Janet     |
| 10254   | Buchanan  | Steven    |

> Inner Join

* by default
* rows from either table that are unmatched in the other table are not returned

> Outer

* null pad when there is no matching pair

### Nested

* Queries are monotonic if DB1 $$ \subseteq $$ DB2 implies Query(DB1) $$ \subseteq $$ Query(DB2)
* Queries involving no negation can be unnested

```sql
-- Find directors of current movies

SELECT director FROM movie WHERE title IN (SELECT title FROM schedule)
-- ==
SELECT director FROM movie, schedule WHERE movie.title = schedule.title

-- Find directors of movies showing in seoul
SELECT m.director FROM movie m, (SELECT title FROM schedule WHERE theater = 'seoul') t
  WHERE m.title = t.title

-- Find actors playing in some movie by Berto
SELECT actor FROM movie WHERE title IN (SELECT title FROM movie WHERE director = 'Berto')
-- ==
SELECT m1.actor FROM movie m1, movie m2 WHERE m1.title = m2.title AND m2.director = 'berto'

-- Find all movies in which Berto does not act
SELECT title FROM movie WHERE title NOT IN (SELECT title FROM movie WHERE actor = 'berto')

-- Find theaters showing only movies by Berto
SELECT theater FROM schedule WHERE theater NOT IN
    (SELECT theater FROM schedule NATURAL LEFT OUTER JOIN
      (SELECT title, director FROM movie WHERE director = 'Berto') WHERE director IS NULL)

-- Loans who have a strictly greater number of borrowers than the average number of borrowers over all loans of that type
SELECT l.no FROM bank.loan l JOIN bank.borrower b ON l.no = b.lno
  GROUP BY l.no HAVING COUNT(*) >
    (SELECT COUNT(*) FROM bank.borrower b2 JOIN bank.loan l2 ON b2.lno = l2.no
     GROUP BY l2.type HAVING l2.type = l.type) | (SELECT COUNT(*) FROM bank.loan l2 WHERE l2.type = l.type);


-- Find actors playing in some movie by Berto
SELECT actor FROM movie WHERE title IN (SELECT title FROM movie WHERE director = 'Berto')
-- ⇒
SELECT m1.actor FROM movie m1, movie m2 WHERE m1.title = m2.title AND m2.director = 'berto'

-- Find all movies in which Berto does not act
SELECT title FROM movie WHERE title NOT IN
  (SELECT title FROM movie WHERE actor = 'berto')

-- Find the names of employees with the maximum salary
-- salary is maximum if it is not among salaries e.salary lower than some f.salary
SELECT name FROM employee WHERE salary NOT IN
  (SELECT e.salary FROM employee e, employee f WHERE e.salary < f.salary)

SELECT actor FROM movie
WHERE actor NOT IN
  (SELECT s.actor FROM movie s, movie m WHERE m.dir = ‘Berto’ AND s.actor NOT IN (SELECT t.actor FROM movie t WHERE m.title = t.title ))

-- Find the unique pairs of customers who took the exact same loans
SELECT c1.name as name1, c2.name as name2 FROM bank.customer c1, bank.customer c2
WHERE c1.name < c2.name AND NOT EXISTS
  (SELECT * FROM bank.loan l WHERE
  (SELECT COUNT(*) FROM bank.borrower b WHERE b.cname = c1.name AND b.lno = l.no) !=
  (SELECT COUNT(*) FROM bank.borrower b WHERE b.cname = c2.name AND b.lno = l.no));

WHERE (NOT) EXISTS

-- Find titles of currently playing movies directed by Berto
SELECT s.title FROM schedule s WHERE EXISTS
(SELECT * FROM movie
WHERE movie.title = s.title AND movie.director = 'berto')

-- Find actors playing in every movie by Berto
SELECT a.actor FROM movie a WHERE NOT EXISTS
  (SELECT * FROM movie m WHERE m.director = 'berto' AND NOT EXISTS
  (SELECT * FROM movie t WHERE m.title = title AND t.actor = a.actor))

-- Find directors of currently playing movies.
SELECT director FROM movie
  WHERE title = ANY (SELECT title FROM schedule)

-- Find the employees with the highest salary
SELECT name FROM employee
  WHERE salary >= ALL (SELECT salary FROM employee)
```

{% tabs %}
{% tab title='path.sql' %}

```sql
-- SQL cannot express all computable queries ⇒ Is there a way to get from CITY1 to city2
-- Way from city1 to city2 with at most 2 stop over.
SELECT x.from z.to FROM flight x, flight y, flight z
WHERE x.from = 'city1' AND x.to = y.from AND y.to = z.from AND z.to = 'city2'

-- Way from city1 to city with at most k stopovers.
-- Intuition : (SELECT * FROM T_{k-1}) UNION (SELECT x.A, y.B FROM G x, T_{k - 1} y WHERE x.B = y.A)
WITH recursive T as (SELECT * FROM G) UNION
(SELECT x.A, y.B FROM G x, T y WHERE x.B = y.A) SELECT * FROM T;

-- Find transitive closure of friend (drinkers who frequent the same bar) / frequent = (frequents, drinker, bar)
CREATE RECURSIVE VIEW T as
  (SELECT f1.drinker AS drinker1, f2.drinker AS drinker2 FROM frequent f1, frequent f2
WHERE f1.bar = f2.bar) UNION
  (SELECT t1.drinker1, f2.drinker AS drinker2 FROM T t1, frequents f1, frequents f2
WHERE t1.drinker2 = f1.drinker AND f1.bar = f2.bar)
```

{% endtab %}
{% endtabs %}

### Union

```sql
-- For each team, return its name and total number of points. (name and points)
CREATE VIEW standings(name, points) AS
  SELECT name, SUM(pts) AS points FROM
  (SELECT aTeam AS name, 3 AS pts FROM matches WHERE ascore > hscore UNION ALL SELECT hTeam AS name AS pts FROM matches WHERE hscore > ascore UNION ALL
  SELECT aTeam AS name, 1 AS pts FROM Matches WHERE hScore = aScore UNION ALL
  SELECT hTeam AS name, 1 AS pts FROM Matches WHERE hScore = aScore UNION ALL
  SELECT name, 0 AS points FROM Teams)
  GROUP BY name

-- Find all actors or directors
(SELECT actor AS name FROM movie) UNION (SELECT director AS name FROM movie)

-- Find all actors who are not directors
(SELECT actor AS name FROM movie) EXCEPT( SELECT director AS name FROM movie)
```

### Update

```sql
-- change all 'berto' entries to 'bertolucci'
UPDATE movie SET director='bertolucci' WHERE director='berto';

-- Increase all salary in toys dept by 10%
UPDATE employee SET salary = 1.1 * salary
WHERE dept = 'toys'

-- Change type of all “jumbo” loans to “student” and type of all original “student” loans to “jumbo”.
UPDATE bank.loan SET type =
  CASE type
    WHEN 'jumbo' THEN 'student'
    WHEN 'student' THEN 'jumbo'
  END
WHERE type = 'jumbo' OR type = 'student';

```

### Delete

{% tabs %}
{% tab title='delete_all.sql' %}

```sql
TRUNCATE TABLE table_name;
DELETE * FROM table_name;

-- Delete every movie that is not currently playing
DELETE FROM movie WHERE title NOT IN (SELECT title FROM schedule)
```

{% endtab %}
{% endtabs %}

### psql (postgres)

* need semicolon, use single quote for string
* yum install postgres-server
* psql mydb < <PATH>

{% starttabs %}
{% tab title="postgres.sql" %}

```sql
-- Check Existence of table
SELECT EXISTS (select * from information_schema.tables where table_name='entity_keyphrases');
select * from information_schema.tables where table_schema = public;

-- Show running query
SELECT pid, client_addr, usename, datname, state, query FROM pg_stat_activity;
SELECT pg_cancel_backend(pid)        # Stop certain query
pg_terminate_backend(pid)             # terminates entire process | database connection

-- Kill all idle queries
SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state in ('idle', 'idle in transaction');
```

{% endtab %}
{% endtabs %}

> Error

* Got an error creating the test database: permission denied to create database
  * ALTER ROLE user1 WITH SUPERUSER;
* must be superuser to alter superusers.
  * sudo -u postgres psql

> Builtin

* pg_database
  * database
  * current_catalog
  * information_schema.tables : All table
  * pg_stat_activity : History

> CLI

* \d : list tables, views, sequences such as a column, type, modifiers of columns
* \df : list available functions in the current database
* \dg : list roles
* \dn : list all schemas of the currently connected database
* \dt : list all tables in the current database, you use \dt command
* \du : display users
* \l : list all databases in the current PostgreSQL database server
* \q : exit
* \connect template1 : connect to db

* psql
  * --help
  * -c `cmd` : to execute the given command
  * -d `dbname` : the name of the database to connect to
  * -h `hostname` : the host name of the machine on which the server is running
  * -U `postgres`

* createdb `user` : create db named `user`

> DDL

* Defualt Tables
  * SELECT * FROM pg_tables ORDER BY tableowner;

* ALTER
  * USER librarian WITH SUPERUSER
* GRANT
  * ALL ON ALL TABLES IN SCHEMA public to dbuser;
  * ALL ON ALL SEQUENCES IN SCHEMA public to dbuser;
  * ALL ON ALL FUNCTIONS IN SCHEMA public to dbuser;
* REASSIGN
  * OWNED BY old_role TO new_role

## NoSQL

* horizontally scalable, add servers in NoSQL database infrastructure to handle more traffic
* Flexible Schema: NoSQL support key-value structures which can be added as needed
* Distributed Data: Parallel read, write across multiple servers, incremental growth in cluster
* Replication: saving multiple copies of data single copies of data create bottlenecks (tune)
Eventual consistency

|      | nested                                        | subcollections                                    | root-level collections                                                 |
| ---- | --------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------- |
| pros | Simple, Easy <br> Three recently visited chat | Size of Parent same <br> Create users within chat | Many to many relation one for users and another for rooms and messages |
| cons | Not scalable                                  | Hard to delete subcollection                      | Getting data that is naturally hierarchical increase complexity        |

> Type

* Key-Value Stores
  * Data is stored in an array of key-value pairs
  * The ‘key’ is an attribute name which is linked to a ‘value’
  * Redis, Voldemort, Dynamo
  * [+]caching

* wide column
  * Have column families, which are containers for rows
  * Don’t need to know all the columns and row doesn’t have to have the same # of columns
  * [+] Best suited for analyzing large datasets.
  * Example : Cassandra, HBase

![wide column](images/20210220_191640.png)

* Graph
  * Store data whose relations are best represented in a graph.
  * Data is saved in graph with nodes (entities), properties (information), lines (connections)
  * Neo4J
  * solr (distributed indexing, replication, load-balanced querying, automated failover, recovery, centralized config, powers the search and navigation features)

### Redis

* In-memory key-value database with optional durability
* keys may have internal structure and expiry (captcha images)
* ziplist compacts size of list in memory without changing contents
* more complex for insertion and deletion
* support abstract data structure → str, list, map, set, sorted set, HyperLogLog, bitmap, stream, spatial index
* replication is accomplished through master-slave mode

### Elastic Search

> Terms

* Cluster

![alt](.gitbook/assets/20210205_165935.png)

> Nodes

* Part of the cluster that stores the data with search and index capabilities
* Node names are lower-case and can have many of them

> Shard, Replica

* portion of the index

> Indexes

* Collection of similar documents

> Types

* category or partition of index

> Documents

* For single customer or order or an event resides in index

```text
<REST verb> <Index> <Type> <ID>
```

### Mongo DB

![mongo db](images/20210220_192135.png)

> Configuration

```sh
systemctl start mongod   # start mongodb
systemctl status mongod  # show mongodb status

/etc/mongod.conf     # configuration
/data/db             # default dbpath
/var/lib/mongo       # data directory
/var/log/mongodb     # log directory

27017                # default port for mongod and mongos instances
27018                # when running with --shardsvr command-line option
27019                # when running with --configsvr command-line option
```

> cli

* mongod
  * help : Show help.
  * --repair : repair
  * show dbs : Print a list of all databases on the server
  * use <db> : Switch current database to <db>
  * db.help() : Show help for database methods
  * --dbpath arg : Directory for datafiles defaults to /data/db
  * db.<collection>.help() : help on collection methods. collection can be non-existing
  * show collections : Print a list of all collections for current database

* DDL

{% tabs %}
{% tab title='hello.js' %}

```js
db.dropDatabase()
db.createCollection('users')
```

{% endtab %}
{% endtabs %}

> DML

* count

```js
user_cl.count()                       // Count # of drinkers.
user_cl.count(addr: {$exists: true})  // with unique addresses
```

```js
// db.<collection>.find(<query filter>, <projection>).<cursor modifier>
// SELECT <projection> FROM <collection> WHERE <query filter>

user_cl.find(name: {$ne : null))   // Non null value
user_cl.find().pretty()            // pretty
user_cl.find().sort({title:-1})    // sort by title
user_cl.find(tags.1: "summer")     // 2nd element in tags is "summer"
user_cl.find().forEach(function(d){print(d.id)}) // forEach
user_cl.find({_id:{$gt:24}}, {email:1, _id:0})   // Grab email info for indexes gt 24
user_cl.find(name: {$regex: |^go.*le$|})         // RE: starts with go ends with le
user_cl.find({tags: {$in : ["popular", "smart"] } })    // users tagged as popular or smart
user_cl.find({tags: {$nin : ["popular", "organic"] } }) // not tagged as
user_cl.insert({ name:'sean', rating:5})   // insert sean’s rating
post_cl.remove({ name : 'Ryan' })          // insert post named ryan
user_cl.update({ _id: 1 }, { rating: 4 }, { upsert: true } ); // Add if not present
user_cl.update({ _id: 1 }, { $set: { rating: 4}});            // Only update without erasing
user_cl.update({ _id: 1 }, { $inc : { rating: 10 } })         // Increment
user_cl.update({ _id: 1 }, { $rename : { rating: 'rate'} })   // rename
```

### Spark

* Driver Program creates Resilient distributed datasets (RDDs)
* Low-latency for small micro-batch size
* Batch and stream processing using disk or memory storage
* SparkSQL, Spark streaming, MLlib, GraphX

> Commands

* lazy evaluation → transformations are not executed until the action stage
* Narrow: processing logic depends only on data, residing in the partition → no data shuffling necessary
* Wide : transformation that requires data shuffling across node partitions

```py
collect()    # copy all elements to the driver
take(n)      # copy first n elements
reduce(func) # aggregate elements with func
saveAsTextFile(filename) # Save to local file or HDFS
```

* Narrow Transformation

```py
coalesce()    # reduce number of partitions
filter(func)  # keep only elements where function is true
flatMap(func) # map then aggregate
map(func)     # apply function to each element of RDD
```

* Wide Transformation

```py
groupbykey
reducebykey
```

* MLlib

```py
from pyspark.mllib.stat import Statistics
dataMatrix = sc.parallelize([[1,2,3],[4,5,6], [7,8,9],[10, 11, 12]])
summary = Statistics.colStats(dataMatrix)
```

```py
from pyspark.mllib.clustering import KMeans, KMeansModel
import numpy as np
data = sc.textFile("data.txt")
parsedData = data.map(lambda line: np.array([float(x) for x in line.split(' ')]))
clusters = Kmeans.train(parsedData, k=3)
```

* GraphX
  * Uses property graph model → both nodes and edges can have attributes and values
  * triplet view → logically joins vortex and edge properties.

### Splunk

* Real-time log forwarding | syslog analysis | server monitoring | alerts, notification

![Splunk](images/20210225_180230.png)

* command

```sh
# return the average population of the counties in Georgia
source="census.csv" CTYNAME != "Georgia" STNAME="Georgia" | stats mean(CENSUS2010POP)

# state with the most counties
source="census.csv" | stats count by STNAME | sort count desc
```

### Hadoop

![alt](images/20210205_170217.png)

* A framework that allows us to store and process large data sets in parallel and distributed fashion
* Scalability commodity hardware for data storage
* Availability commodity hardware for distributed processing
* JVMs do not share state
* JVM processes differ between Hadoop 1.0 and 2.0
* Hadoop distributed file system
* Open-source data storage
* Hadoop cluster
* HDFS maintains three copies of every block
* Default chunk size, the size of each piece of a file is 64 megabytes
* hadoop fs -copyFromLocal words.txt
* copy into hadoop

> Pros

* Long term availability of data
* Future anticipated data growth
* Many platforms over single data store (facilitate shared environment)
* High volume | variety
* Behavioral data → batch process, health care
* Pre-built hadoop images → quick prototyping, deploying, and validating of projects

> Cons

* Small data processing, Task level parallelism
* Advanced algorithms (highly coupled data processing algorithm)
* Replacement to your infrastructure (may not be suitable solution for business case)
* Random data access
* Machine learning → HDFS Bottleneck | Mapreduce Computation | No interactive shell | Java
* Line of Business → usually transactional and not a good fit (X - use relational database)

> Hadoop vs HBase

* HBase is NoSQL, hadoop uses an alternative file system (HDFS)

> Three ways

* commercial distribution  # Cloudera, Hortonworks, MapR
* Open source     # apache
* public cloud    # Iaas(VM, docker), PaaS(AWS, HDinsight), some commercial available

> Three layers of ecosystem?

* Data Management and Storage
* Data Integration and Processing
* Coordination and Workflow Management

> Term

* Mapreduce
  * Processing API
  * Allow parallel & distributed processing using disk storage
  * High-latency
  * Map-Reduce consists of three main steps: Mapping, Shuffling and Reducing
  * Map: Apply same operation to each member of collection
  * Reduce: collecting things that have same 'key'
  * [+] Hides complexities of parallel programming  → search engine page ranking and topic mapping
  * [-] frequently changing data → slow, as it reads entire input data
dependent tasks, interactive analysis, Native support for Java only

* Yarn
  * Flexible scheduling and resource management
  * Allows various applications to run on the same Hadoop cluster

* NameNode
  * One per cluster
  * Maintains and manages DataNodes
  * records metadata (data blocks info, location of blocks stored, the size of files, permissions, hierarchy)

* editLog
  * only contain the most recent changes
  * reside in the RAM of the machine

* fsImage
  * contain all the details of all the changes

* Secondary NameNode
  * Takes over the responsibility of checkpointing, therefore, making NameNode more available
  * Allows faster Failover as it prevents edit logs from getting too huge

* Checkpointing
  * process of combining edit logs with FsImage
  * happens periodically (default: 1 hour)

* DataNode
  * Slave daemons
  * Stores actual data
  * Serves read and write requests from the clients

* fs
  * hadoop fs -[command_name]
  * copyFromLocal <fname>
  * copyToLocal <fname>

* jar
  * wordcount <ins> <out>
  * hadoop jar |usr|jars|hadoop-examples.jar wordcount
