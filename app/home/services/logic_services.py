import psycopg2

def connect_db():
    conn = psycopg2.connect(dbname="db_contac", user="user", password="1234", port="5432", host="localhost")
    cur = conn.cursor()

    return conn, cur

def query_create(my_query):
    conn, cur = connect_db()

    cur.execute(my_query)

    result = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    res = list()

    for item in result:
        item_dict = {"id": item[0],"name": item[1], "email": item[2], "description": item[3]}

        res.append(item_dict)

    return res

def create_item_data_base(query, data):
    conn, cur = connect_db()

    cur.execute(query)

    try:
        cur.fetchall()
    except:
        result_end = data        

    conn.commit()
    cur.close()
    conn.close()

    return result_end