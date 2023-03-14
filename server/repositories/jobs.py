import sqlite3
from models.jobs import JobInternal

class JobsRepository:
  def __init__(self):
    connection = sqlite3.connect("avodah.db")
    cursor = connection.cursor()

    self.connection = connection
    self.cursor = cursor

    cursor.execute("CREATE TABLE IF NOT EXISTS job (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, image TEXT)")
  
  def __del__(self):
    self.connection.commit()

  def create(self, job: JobInternal) -> int:
    query_string = "INSERT INTO job (name, image) VALUES ('{}', '{}')".format(job.name, job.image)
    self.cursor.execute(query_string)
    return self.cursor.lastrowid
  
  def get(self) -> list[JobInternal]:
    query_string = "SELECT * FROM job".format(id)
    returned_rows = self.cursor.execute(query_string).fetchall()
    
    jobinternals = list[JobInternal]()
    for row in returned_rows:
      jobinternals.append(JobInternal(*row))

    return jobinternals

  def get_by_id(self, id: str) -> JobInternal:
    query_string = "SELECT * FROM job WHERE id = '{}'".format(id)
    returned_rows = self.cursor.execute(query_string).fetchall()
    if len(returned_rows) != 1:
      raise Exception("No Job Found")

    return JobInternal(*returned_rows[0])
    
    
  def get_by_name(self, name: str) -> JobInternal:
    query_string = "SELECT * FROM job WHERE name = '{}'".format(id)
    return self.cursor.execute(query_string).fetchall()
  
  def delete(self, id: str):
    query_string = "DELETE FROM job WHERE id = '{}'".format(id)
    self.cursor.execute(query_string).fetchall()

  def delete_by_name(self, name: str):
    query_string = "DELETE FROM job WHERE name = '{}'".format(name)
    self.cursor.execute(query_string).fetchall()