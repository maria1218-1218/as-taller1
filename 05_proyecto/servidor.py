# Servidor

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secreto!'
socketio = SocketIO(app)

@app.route('/')
def index():
    # Jinja2 renderiza el archivo index.html de la carpeta /templates
    return render_template('index.html')

@socketio.on('mensaje_cliente')
def manejar_mensaje(data):
    print(f"Mensaje de {data['usuario']}: {data['mensaje']}")
    # Reenviamos el mensaje a todos los conectados
    emit('mensaje_servidor', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)