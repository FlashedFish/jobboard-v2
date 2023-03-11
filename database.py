from sqlalchemy import create_engine, text

db_connection_string ="mysql+pymysql://rdzrj81c4vert9a48bcz:pscale_pw_TfBMGVbfcTr2ezsK7mVpl3BcEm9ujCEpbDg7pNgXV2k@us-east.connect.psdb.cloud/jobboard?charset=utf8mb4"
engine= create_engine(
  db_connection_string,
  connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
