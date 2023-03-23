from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id =" + id))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._mapping)


def add_job_to_db(job_data):
  with engine.connect() as conn:

    query =text(
      "INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements) VALUES (:title, :location, :salary, :currency, :responsibilities, :requirements)"
    )
    conn.execute(query,dict(
                         
                         title=job_data['title'],
                         location=job_data['location'],
                         salary=job_data['salary'],
                         currency=job_data['currency'],
                         responsibilities=job_data['responsibilities'],
                         requirements=job_data['requirements']))


  

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    conn.execute(query,dict(
                         job_id=job_id,
                         full_name=data['full_name'],
                         email=data['email'],
                         linkedin_url=data['linkedin_url'],
                         education=data['education'],
                         work_experience=data['work_experience'],
                         resume_url=data['resume_url']))
