# Module

## log4j

* log4j.appender.A1.layout.ConversionPattern=%d{HH:mm:ss,SSS} %-5p %c{1}.%M %L %x - %m%n

```sh
%c        # Class name
%M        # Method name
%L        # Line number
%p        # debug strength
%20c      # Left pad if less than 20 char
%-20c     # Right pad if less than 20 char
```

## sql

```sh
execute(String sql)         // return whether statement has returned a ResultSet object
executeQuery(String sql)    // java.sql.ResultSet object which contains the data returned by the query
executeUpdate(String sql)   // int value which represents the number of rows affected by the query
```

> Size of stmt

```java
int size=0;
while (rset.next()) {
    size++;
}

public static void main(String[] args) throws SQLException, ClassNotFoundException {
    // Load PostgreSQL driver
    Class.forName("org.postgresql.Driver");
    // Connect to the local database
    Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/pa2", id, pw);

    Statement stmt = con.createStatement();
    stmt.executeUpdate("DROP TABLE influence");
    stmt.executeUpdate("CREATE TABLE influence as SELECT DISTINCT d1.cname as \"from\", d2.cname as \"to\" FROM transfer t JOIN depositor d1 ON t.src = d1.ano JOIN depositor d2 ON t.tgt = d2.ano;");
    stmt.executeUpdate("CREATE TABLE delta as SELECT DISTINCT d1.cname as \"from\", d2.cname as \"to\" FROM transfer t JOIN depositor d1 ON t.src = d1.ano JOIN depositor d2 ON t.tgt = d2.ano;");

    stmt.executeUpdate("DROP VIEW G");

    // Close the result set, statement, and the connection
    rset.close();
    stmt.close();
    con.close();
}

con.setAutoCommit(false);     # Commit all changes at once
con.commit();
con.setAutoCommit(true);
```
