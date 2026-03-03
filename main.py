from flask import Flask, request
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora de Dinero</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; padding: 20px; background-color: #f4f4f9; }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 400px; margin: auto; }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; }
        button { background: #28a745; color: white; border: none; padding: 10px; width: 100%; border-radius: 5px; cursor: pointer; font-size: 16px; }
        .res { margin-top: 20px; padding: 15px; background: #d4edda; color: #155724; border-radius: 5px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h2>💰 Calculadora de Riqueza</h2>
        <form method="POST">
            Inversión Inicial ($): <input type="number" name="inicial" value="1000" required>
            Aporte Mensual ($): <input type="number" name="mensual" value="100" required>
            Años: <input type="number" name="anios" value="10" required>
            Interés Anual (%): <input type="number" step="0.1" name="tasa" value="8" required>
            <button type="submit">Calcular Futuro</button>
        </form>
        {% RESULTADO_AQUI %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    anios = None
    if request.method == 'POST':
        inicial = float(request.form['inicial'])
        mensual = float(request.form['mensual'])
        anios = int(request.form['anios'])
        tasa = float(request.form['tasa'])
        
        total = inicial
        tasa_mensual = (tasa / 100) / 12
        for _ in range(anios * 12):
            total = (total + mensual) * (1 + tasa_mensual)
        
        resultado = "{:,.2f}".format(total)
    
    if resultado:
        bloque_res = f'<div class="res">En {anios} años tendrás: ${resultado}</div>'
        return HTML_TEMPLATE.replace('{% RESULTADO_AQUI %}', bloque_res)
    else:
        return HTML_TEMPLATE.replace('{% RESULTADO_AQUI %}', '')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
