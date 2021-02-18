# Database

## Terms

* Lake
  * vast pool of raw data, the purpose for which is not yet defined

* Warehouse
  * repository for structured, filtered data that has already been processed for a specific purpose

* Silo
  * Data produced from an organization that is spread out
  * Bad unsynchronized and invisible data

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

```sql
-- single line comment
/* multi-line
   coment */
```

> Terms

* Constraints
  * PRIMARY, FOREIGN, UNIQUE, CHECK, NOT NULL

> Key

* Candidate Keys
  * Minimal Super Keys
* Foriegn Keys
  * FOREIGN KEY \(PersonID\) REFERENCES Persons\(PersonID\)
  * PersonID column in the Orders table is a FOREIGN KEY in the Orders table
* Primary Keys
  * Chosen candidate keys, cannot have null values in any tuple
  * table can have only one primary
* Super keys
  * A set of attributes SK of R such that no two tuples in any valid
  * relation instance r\(R\) will have the same value for SK

> Query

* What is a correlated query?
  * A type of query that contains a subquery that requires information from a query one level up

> MySQL

```text
mysql -u user -p -e 'show databases;'

# mysql
SHOW DATABASES / SCHEMAS;
```

> Relational algebra

* Find directors of current movies

{t: title | $$ \exists $$ s $$ \in $$ schedule [s(title) = t(title)]}

### Create

### Read

> Where

```sql
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

-- Multiple equality
LEAST(a, b, c, d, e) = GREATEST(a, b, c, d, e)
```

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
```

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
```

## Update

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

### NoSQL

## Elastic Search

### Terms

> Cluster

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

## Hadoop
![alt](images/20210205_170217.png)

* A framework that allows us to store and process large data sets in parallel and distributed fashion
* Scalability commodity hardware for data storage
* Availability commodity hardware for distributed processing
* JVMs do not share state
* JVM processes differ between Hadoop 1.0 and 2.0

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