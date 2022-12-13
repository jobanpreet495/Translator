from flask import Flask,render_template,request
from googletrans import Translator, constants
from pprint import pprint


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate',methods=['POST'])
def translate():
    translator = Translator()
    to_lang=request.form['to_lang']
    text=request.form['text']
    translations = translator.translate(text, dest=to_lang)
    result=translations.text
    return render_template('index.html',result=result)



    

if __name__=="__main__":
    app.run(debug=True)
