#!/usr/bin/python3

import datetime
import psycopg2


def print_most_popular_articles():
    '''
    This function answers below question:
    1. What are the most popular three articles of all time?
    '''
    db = psycopg2.connect(database='news')
    c = db.cursor()
    SQL = '''
        SELECT a.title, COUNT(*) AS views
        FROM log JOIN
            (SELECT title, ('/article/' || slug) AS article_slug
                FROM articles) AS a
        ON log.path = a.article_slug
        GROUP BY a.title
        ORDER BY views DESC
        LIMIT 3;
        '''
    c.execute(SQL)
    result = c.fetchall()
    for r in result:
        print('"{}" — {} views'.format(r[0], r[1]))
    db.close()


def print_most_popular_authors():
    '''
    This function answers below question:
    2. Who are the most popular article authors of all time?
    '''
    db = psycopg2.connect(database='news')
    c = db.cursor()
    SQL = '''
        SELECT a.name, COUNT(*) AS views
        FROM log JOIN
            (SELECT title, name, ('/article/' || slug) AS article_slug
                FROM articles JOIN authors
                ON articles.author = authors.id) AS a
        ON log.path = a.article_slug
        GROUP BY a.name
        ORDER BY views DESC;
        '''
    c.execute(SQL)
    result = c.fetchall()
    for r in result:
        print('{} — {} views'.format(r[0], r[1]))
    db.close()


def print_days_of_most_errors():
    '''
    This function answers below question:
    3. On which days did more than 1% of requests lead to errors?
    '''
    db = psycopg2.connect(database='news')
    c = db.cursor()
    SQL = '''
        SELECT e.day, (100*e.errors/r.requests) AS errors_percent
        FROM (SELECT date(time) AS day, COUNT(*) AS errors
                FROM log
                WHERE status = '404 NOT FOUND'
                GROUP BY day) AS e
            JOIN
            (SELECT date(time) AS day, COUNT(*) AS requests
                FROM log
                GROUP BY day) AS r
        ON e.day = r.day
        WHERE (100*e.errors/r.requests) > 1
        ORDER BY e.errors DESC;
        '''
    c.execute(SQL)
    result = c.fetchall()
    for r in result:
        d = datetime.date.strftime(r[0], '%b %d, %Y')
        print('{} — {}% errors'.format(d, r[1]))
    db.close()


# Output the analysis
print('************************************')
print('**** Log Analyzer for news blog ****')
print('************************************\n')

print('The most popular three articles of all time:')
print('--------------------------------------------')
print_most_popular_articles()
print('\n')

print('The most popular article authors of all time:')
print('---------------------------------------------')
print_most_popular_authors()
print('\n')

print('The days with more than 1% of requests lead to errors:')
print('-------------------------------------------------------')
print_days_of_most_errors()
print('\n')

print('************************************')
print('**** End of Log Analyzer output ****')
print('************************************')
