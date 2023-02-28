from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS=[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Tampa, Florida',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Infosec',
    'location': 'Sarasota, Florida',
    'salary': '$120,000'
  },
  {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Remote, Florida',
    'salary': '$80,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Fransico, California',
    'salary': '$200,000'
  }

]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name="Jacobs")
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

print(__name__)
if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True)