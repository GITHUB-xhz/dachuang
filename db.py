import pymysql


def get_conn():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='100110',
        database='行星坐标',
        charset='utf8'
    )


def query_data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()


if __name__ == "__main__":
    sql = "select * from user"
    datas = query_data(sql)
    import pprint

    pprint.pprint(datas)
