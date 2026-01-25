# SubQueries

## Subquery in WHERE

#### Use a query result as a filter value. Find products more expensive than average.

The inner query (subquery) calculates AVG(price), then the outer query uses that value to filter. This finds above-average priced products.

#### Select name and price of products where price is greater than the average product price.

```
SELECT name, price FROM products WHERE price > (SELECT AVG(price) from products) 
```

## Subquery in FROM

#### Use a subquery as a temporary table (derived table). Query the results of another query.

The subquery creates a temporary result set that we can query. This finds USA users, then counts them.

#### Create a subquery that selects users from USA, then counts how many there are.

```
SELECT COUNT(*) FROM (SELECT * FROM users WHERE country= 'USA')
```

## EXISTS Operator

#### Check if subquery returns any rows. Find users who have placed any orders.

EXISTS returns true if the subquery finds any matching rows. This identifies the customers who have purchased something.

#### Select name and email of users who exist in the order table (have made orders).

```
SELECT  name, email FROM users WHERE EXISTS (SELECT 1 FROM orders WHERE users.id = orders.user_id)
```

# Set Operator

## UNION

#### Combine results from multiple queries, removing duplicates. Merge two result sets into one.

Union combines two select statements and removes duplicate rows. This gives us all unique cities/locations from both tables.

#### Select all cities from users, and all locations from departments. Combine into one list with no duplicates.

```
(SELECT city FROM users) UNION (SELECT location FROM departments)
```

## UNION ALL

#### Combine results from multiple queries, keeping all duplicates. Faster than UNION.

UNION ALL combines results but keeps duplicates. It's faster than Union since it doesn't check for duplicates. USA appears multiple times.

#### Select all countries from users and all countries from suppliers. Keep all rows including duplicates.

```
(SELECT country FROM users) UNION ALL (SELECT country FROM suppliers)
```