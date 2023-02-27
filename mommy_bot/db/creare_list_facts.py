import sqlite3


insert_facts = [
    (1, "мама милая"),
    (2, "мама замечательная"),
    (3, "мама красивая"),
    (4, "мама вкусно готовит"),
    (5, "мы с Ксюшей любим маму"),
    (6, "мама заботливая")
]


with sqlite3.connect('facts.db') as db: 

    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS facts(id, content)")
    db.commit()
    #cursor.executemany(""" INSERT INTO facts(id, content) VALUES(?, ?) """, insert_facts)
    #db.commit()

    query = """ SELECT * FROM facts"""
    all_f = cursor.execute(query).fetchall()
