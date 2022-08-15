import psycopg2


def insert_or_update(full_name, username, phone_number, user_id):
    try:
        is_updated = False
        conn = psycopg2.connect(
            host='ec2-54-86-106-48.compute-1.amazonaws.com',
            database='df54l86vpk4abu',
            user='amwwsumvwyurje',
            password='9b021f7784a46f4768e6a6c25a7681dd2b425a30d5268c9a425bfd3af74bfbc2'
        )

        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM users WHERE user_id={user_id}")
        if cursor.fetchone():
            sql = """UPDATE users SET full_name=%s, username=%s, phone_number=%s WHERE user_id=%s;"""
            is_updated = True
        else:
            sql = """INSERT INTO users(full_name, username, phone_number, user_id) VALUES(%s, %s, %s, %s);"""

        cursor.execute(sql, (full_name, username, phone_number, user_id))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

    return is_updated
