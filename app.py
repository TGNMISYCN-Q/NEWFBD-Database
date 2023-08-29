from flask import Flask, render_template, request, jsonify
from db import feedback_db, questionform

app=Flask(__name__)

@app.route("/")
def FBD():
  f=feedback_db()
  return render_template('home.html', feedback=f)  #for using, use 'feedback'
  
@app.route('/api/feedback')
def feedback():
  F=feedback_db()
  return jsonify(F)   #for storing: feedback is hoping to be a list

@app.route("/")
def QS():
  qs=questionform()
  return render_template('home.html', questionstore=qs)  #for using, use 'questionstore'

@app.route('/api/questionstore', methods=['post'])
def questionstore():
  QUESTION=request.form
  Q=questionform()
  #store into db
  return jasonify(QUESTION, Q)
  #for storing: feedback is hoping to be a list which contain the question that the users enter

@app.route('/')
def index():
    return render_template('add_input_box.html')
           
Questions=[]
@app.route('/questionupdate', methods=['POST'])
def Question():
  Question=request.form.get('question')
  if not question:
    return render_template('home.html')
  Questions.append(f'{Question}')
  return redirect('/questionstore')


if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)





