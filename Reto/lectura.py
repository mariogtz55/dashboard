import psycopg2

def lect():
    host = "cncciber.postgres.database.azure.com"
    dbname = "postgres"
    user = "AlejandroDuran@postgresciberfisico"
    password = "noviembre2022@"
    sslmode = "require"
    
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cnc;")
    rows = cursor.fetchall()
    print("Read")
    conn.commit()
    cursor.close()
    conn.close()
    return rows