from flask import Flask, render_template, request, jsonify
from db import feedback_db

app=Flask(__name__)

@app.route("/")
def FBD():
  f=feedback_db()
  return render_template('home.html', feedback=f)

@app.route('/')
def index():
    return render_template('add_input_box.html')
  
@app.route('/api/feedback')
def feedback():
  F=feedback_db()
  return jsonify(F)   #question is hoping to be a list which contain the question that the users enter

if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)

@app.route('/questionstore', methods=['post'])
def questionstore():
  QUESTION=request.form
  #store into db
  return jasonify(QUESTION)
           
Questions=[]
@app.route('/questionupdate', methods=['POST'])
def Question():
  Question=request.form.get('question')
  if not question:
    return render_template('home.html')
  Questions.append(f'{Question}')
  return redirect('/questionstore')




