from flask import Flask, request

app = Flask(__name__)

# Diseño visual simple (HTML)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora de Dinero</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; padding: 20px; background: #f0f2f5; }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }
        button { background: #28a745; color: white; border: none; padding: 15px; width: 100%; border-radius: 5px; font-size: 16px; }
        .res { margin-top: 20px; font-weight: bold; color: #155724; background: #d4edda; padding: 15px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>💰 Calculadora de Riqueza</h2>
        <form method="POST">
            Inversión Inicial ($): <input type="number" name="inicial" value="1000">
            Aporte Mensual ($): <input type="number" name="mensual" value="100">
            Años: <input type="number" name="anios" value="10">
            Interés Anual (%): <input type="number" step="0.1" name="tasa" value="8">
            <button type="submit">Calcular Futuro</button>
        </form>
        {% if resultado %}
        <div class="res">En {{ anios }} años tendrás: ${{ resultado }}</div>
        {% endif %}
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
        
        # Lógica del interés compuesto
        total = inicial
        tasa_mensual = (tasa / 100) / 12
        for _ in range(anios * 12):
            total = (total + mensual) * (1 + tasa_mensual)
        resultado = "{:,.2f}".format(total)

return HTML_TEMPLATE.replace('{% if resultado %}', '').replace('{% endif %}', '').replace('{{ resultado }}', str(resultado) if resultado else '').replace('{{ anios }}', str(anios) if anios else '')

    
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

