from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('index.html')
@app.route('/calculate',methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression)
    except Exception as e:
        result = "Erro "+str(e)
    return render_template('index.html',display=expression+" = "+str(result))
if __name__ == '__main__':
    app.run(debug=True)
    