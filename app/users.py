  import sqlite3


  def find_by_name(conn, name):
      query = f"SELECT id, name FROM users WHERE name = '{name}'"
      return conn.execute(query).fetchall()
