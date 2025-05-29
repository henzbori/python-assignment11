import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

with sqlite3.connect('/Users/boriskhenzykhenov/Desktop/Code the Dream/python_class/python-assignment11/db/lesson.db') as conn:
    sql_statement = """SELECT o.order_id, SUM(p.price * l.quantity) AS total_price 
        FROM orders o
        JOIN line_items l ON o.order_id = l.order_id 
        JOIN products p ON l.product_id = p.product_id 
        GROUP BY o.order_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    df['cumulative'] = df['total_price'].cumsum()
    df.plot(x='order_id', y='cumulative', kind='line', color='red')
    plt.title("Cumulative Revenue by Order")
    plt.xlabel("Order ID")
    plt.ylabel("Cumulative Revenue")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
