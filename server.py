from flask import Flask, escape, request, render_template   
import os.path

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/som1')
def som1():
    som = "som/tt1.ogg"
    return render_template('tt1.html', som=som)


@app.route('/som/<codtxt>')
def som(codtxt):
    texto = "som%s.txt" % codtxt
    som = "som%s.ogg" % codtxt
#    return render_template('sons.html', som=som, texto=texto)
    return render_template('tt%s.html'%codtxt, som=som, texto=texto)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=80)
# env FLASK_APP=server.py flask run -h 0.0.0.0
