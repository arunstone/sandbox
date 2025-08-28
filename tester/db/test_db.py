def test_insert_and_select(db_cursor):
    db_cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT)")
    db_cursor.execute("INSERT INTO users (name) VALUES ('Arun') RETURNING id")
    user_id = db_cursor.fetchone()[0]

    db_cursor.execute("SELECT name FROM users WHERE id = %s", (user_id,))
    name = db_cursor.fetchone()[0]

    assert name == "Arun"
