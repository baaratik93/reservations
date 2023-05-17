def requete(sql):
    import psycopg2
    conn = psycopg2.connect(
        host= "localhost",
        database = "auto-reserv",
        user="mahmoud",
        password="passer"
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return cursor
    cursor.close()
    conn.close()