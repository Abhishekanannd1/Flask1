from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/welcome')
def welcome():
    return "<h1>welcome to the first flask</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "the prson has passed and the score is"+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the score is" +str(score) 

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks=(maths+science+history)/3
        
       # return render_template('calculate.html',results=average_marks)
    

        #result=""
        #if average_marks>=50:
          #  result="success"
        #else:
          #  result="fail"
            
       # return redirect(url_for(result,score=average_marks))
       
    return render_template('result.html',results=average_marks)
   





if __name__=='__main__':
    app.run(debug=True)