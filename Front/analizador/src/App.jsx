import axios from 'axios';
import React, { useState } from 'react';

function App() {
  const [codigoFuente, setCodigoFuente] = useState('');
  const [resultadoLexico, setResultadoLexico] = useState([]);
  const [resultadoSintactico, setResultadoSintactico] = useState([]);
  const [resultadoTabla, setResultadoTabla] = useState([]);
  const [conteoTokens, setConteoTokens] = useState({});

  const analizarCodigo = async () => {
    try {
      const responseLexico = await axios.post('http://localhost:5000/analisis_lexico', { codigo_fuente: codigoFuente });
      setResultadoLexico(responseLexico.data.resultado);

      const responseSintactico = await axios.post('http://localhost:5000/analisis_sintactico', { codigo_fuente: codigoFuente });
      setResultadoSintactico(responseSintactico.data.resultado);

      const responseTabla = await axios.post('http://localhost:5000/analisis_lexico_tabla', { codigo_fuente: codigoFuente });
      setResultadoTabla(responseTabla.data.resultado);

      const responseConteo = await axios.post('http://localhost:5000/conteo_tokens', { codigo_fuente: codigoFuente });
      setConteoTokens(responseConteo.data.resultado);
    } catch (error) {
      console.error('Error analizando código:', error);
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Analizador Léxico y Sintáctico</h1>
      <div className="mb-3">
        <div className="d-flex justify-content-between">
          <button className="btn btn-secondary mb-3" onClick={() => setCodigoFuente('')}>
            Subir Archivo
          </button>
          <button className="btn btn-danger mb-3" onClick={() => setCodigoFuente('')}>
            X
          </button>
        </div>
        <label htmlFor="codigoFuente" className="form-label">Texto</label>
        <textarea
          id="codigoFuente"
          className="form-control"
          rows="6"
          value={codigoFuente}
          onChange={(e) => setCodigoFuente(e.target.value)}
        />
      </div>
      <div className="d-flex justify-content-between mb-3">
        <button className="btn btn-primary" onClick={analizarCodigo}>Analizar Código</button>
      </div>
      <div className="row">
        <div className="col-md-6">
          <h2>Análisis Léxico</h2>
          <pre className="bg-light p-3" style={{ height: '200px', overflowY: 'scroll' }}>
            {resultadoLexico.length > 0 ? resultadoLexico.map((res, idx) => <div key={idx}>{res}</div>) : 'No hay resultados'}
          </pre>
        </div>
        <div className="col-md-6">
          <h2>Análisis Sintáctico</h2>
          <pre className="bg-light p-3" style={{ height: '200px', overflowY: 'scroll' }}>
            {resultadoSintactico.length > 0 ? resultadoSintactico.map((res, idx) => <div key={idx}>{res}</div>) : 'No hay resultados'}
          </pre>
        </div>
      </div>
      <div className="row mt-4">
        <div className="col-12">
          <h2>Tabla de Resultados Léxicos</h2>
          <table className="table table-bordered">
            <thead>
              <tr>
                <th>Identificador</th>
                <th>Simbolo</th>
                <th>Token</th>
                <th>Número de línea</th>
                <th>Palabra reservada</th>
                <th>Número</th>
                <th>Llave izquierda</th>
                <th>Llave derecha</th>
                <th>Paréntesis izquierdo</th>
                <th>Paréntesis derecho</th>
                <th>Punto y coma</th>
              </tr>
            </thead>
            <tbody>
              {resultadoTabla.length > 0 ? resultadoTabla.map((res, idx) => (
                <tr key={idx}>
                  <td>{res.Identificador}</td>
                  <td>{res.Simbolo}</td>
                  <td>{res.Token}</td>
                  <td>{res["Número de línea"]}</td>
                  <td>{res["Palabra reservada"]}</td>
                  <td>{res["Número"]}</td>
                  <td>{res["Llave izquierda"]}</td>
                  <td>{res["Llave derecha"]}</td>
                  <td>{res["Paréntesis izquierdo"]}</td>
                  <td>{res["Paréntesis derecho"]}</td>
                  <td>{res["Punto y coma"]}</td>
                </tr>
              )) : (
                <tr>
                  <td colSpan="11">No hay resultados</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
      <div className="row mt-4">
        <div className="col-12">
          <h2>Conteo de Tokens</h2>
          <table className="table table-bordered">
            <thead>
              <tr>
                <th>Token</th>
                <th>Conteo</th>
              </tr>
            </thead>
            <tbody>
              {Object.keys(conteoTokens).length > 0 ? Object.entries(conteoTokens).map(([token, count], idx) => (
                <tr key={idx}>
                  <td>{token}</td>
                  <td>{count}</td>
                </tr>
              )) : (
                <tr>
                  <td colSpan="2">No hay resultados</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default App;
