from flask import Flask, render_template, request

app = Flask(__name__)

value = "Olá"

@app.route('/pagina.py',)
@app.route('/',)
def hello():
    msg = request.args.get('mensagem', value)
    return render_template('index.html', **{'msg': msg})

if __name__ =='__main__':
    app.run()