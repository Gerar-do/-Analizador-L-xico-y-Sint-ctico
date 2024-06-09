from flask import Flask, request, jsonify
from flask_cors import CORS
import analizador_lexico
import analizador_sintactico

app = Flask(__name__)
CORS(app)

@app.route('/analisis_lexico', methods=['POST'])
def analisis_lexico():
    codigo_fuente = request.json['codigo_fuente']
    resultado = analizador_lexico.prueba(codigo_fuente)
    return jsonify({'resultado': resultado})

@app.route('/analisis_sintactico', methods=['POST'])
def analisis_sintactico():
    codigo_fuente = request.json['codigo_fuente']
    resultado = analizador_sintactico.prueba_sintactico(codigo_fuente)
    return jsonify({'resultado': resultado})

@app.route('/analisis_lexico_tabla', methods=['POST'])
def analisis_lexico_tabla():
    codigo_fuente = request.json['codigo_fuente']
    resultado = analizador_lexico.prueba2(codigo_fuente)
    return jsonify({'resultado': resultado})

@app.route('/conteo_tokens', methods=['POST'])
def conteo_tokens():
    codigo_fuente = request.json['codigo_fuente']
    resultado = analizador_lexico.contar_tokens(codigo_fuente)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
