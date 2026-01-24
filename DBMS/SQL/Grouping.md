# GROUPING

## Count

#### Count the number of rows. Aggregation functions help you analyze and summarize data.

COUNT(*) counts all rows. We have 25 orders total. COUNT is the most basic aggregation function.

#### Count the total number of orders in the orders table.

```
SELECT COUNT(*) FROM orders
```

## Sum

#### Calculate the total of a numeric column. Products table tracks inventory in the stock column.

SUM adds up all values in a column. This tells us total inventory across all 20 products in our catalog.

#### Calculate the total stock quantity across all products.

```
SELECT SUM(stock) FROM products
```

## Avg

#### Calculate the average of a numeric column. Our 10 employees have varying salaries.

AVG computes the mean value. This shows the typical employee salary in our company.

#### Calculate the average salary of all employees.

```
SELECT AVG(salary) FROM employees
```

## MIN and MAX

#### Find the minimum and maximum values in a column. Useful for finding ranges.

MIN and MAX find the smallest and largest values. This shows the price range in our product catalog.

#### Find the minimum and maximum price from the products table.

```
SELECT MIN(price), MAX(price) FROM products
```

## Group By

#### Group rows with the same values and apply aggregation to each group. Our users are distributed across 4 countries.

GROUP BY creates groups for each unique value, then applies COUNT to each group. This shows user distribution by country.

#### Count the number of users in each country. Show country name and count.

```
SELECT country, COUNT(*) FROM users GROUP BY country
```

## Having Clause

#### Filter groups after aggregation. WHERE filters rows before grouping, HAVING filters groups after.

HAVING filters the grouped results. It's like WHERE, but for groups. Only countries with 3+ users will appear.

#### Show countries that have more than 3 users. Display country and user count.

```
SELECT country, COUNT(*) FROM users GROUP BY country HAVING COUNT(*)>3
```


