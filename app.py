from flask import Flask, render_template, request, jsonify

@app.route("/")
def FBD():
    return render_template('home.html')

@app.route('/api/jobs')
def question():
  return jsonify(question)   #question is going to be a list which contain the question that the users enter

if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)

@app.route('/questionstore')
def questionstore():
  return render_template('QUESTION.html', Questions=Questions)
           
Questions=[]
@app.route('/questionupdate', methods=['POST'])
def Question():
  Question=request.form.get('question')
  if not question:
    return render_template('home.html')
  Questions.append(f'{Question}')
  return redirect('/questionstore')




