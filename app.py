from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db,load_job_from_db,add_application_to_db,add_job_to_db


app = Flask(__name__)

@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('jobboard.html', jobs=jobs, company_name="Jacobs")
  return render_template('home.html')
  
@app.route("/resume")
def jobboard():
  
  return render_template('home.html')

@app.route("/wip")
def work_in_progress():
  return render_template('wip.html')
  

@app.route("/api/jobs")
def list_jobs():
  jobs =load_jobs_from_db()
  
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job=load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',job=job)


@app.route("/post")
def create_job_form():
  return render_template('createjob.html')
  
@app.route("/post/sent", methods=['post'])
def create_job():  
  job_data =request.form
  add_job_to_db(job_data)
  return render_template('jobcreated.html',job=job_data)




@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):

  
  data =request.form
  job = load_job_from_db(id)

  add_application_to_db(id, data)
  
  return render_template('application_submitted.html', application=data, job=job)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)