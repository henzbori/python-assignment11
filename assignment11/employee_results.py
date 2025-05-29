import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

with sqlite3.connect('/Users/boriskhenzykhenov/Desktop/Code the Dream/python_class/python-assignment11/db/lesson.db') as conn:
    sql_statement = """SELECT last_name, SUM(price * quantity) AS revenue 
        FROM employees e 
        JOIN orders o ON e.employee_id = o.employee_id 
        JOIN line_items l ON o.order_id = l.order_id 
        JOIN products p ON l.product_id = p.product_id 
        GROUP BY e.employee_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    df.plot(kind='bar', x='last_name', y='revenue', color='green', legend=False)
    plt.title("Revenue by Employee")
    plt.xlabel("Employee's Last Name")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()