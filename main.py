from flask import Flask, request
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Compound Interest Calculator - Grow Your Wealth</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; background-color: #f8f9fa; }
        .card { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-bottom: 30px; }
        h1, h2 { color: #2c3e50; text-align: center; }
        label { display: block; margin-top: 15px; font-weight: bold; }
        input { width: 100%; padding: 12px; margin-top: 5px; border: 1px solid #ddd; border-radius: 8px; box-sizing: border-box; font-size: 16px; }
        button { background: #28a745; color: white; border: none; padding: 15px; width: 100%; border-radius: 8px; cursor: pointer; font-size: 18px; margin-top: 20px; transition: background 0.3s; }
        button:hover { background: #218838; }
        .res { margin-top: 25px; padding: 20px; background: #e9f7ef; border-left: 5px solid #28a745; border-radius: 5px; font-size: 1.2em; text-align: center; }
        .content-section { background: white; padding: 25px; border-radius: 15px; margin-top: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
        .faq { margin-top: 20px; }
        .faq-item { margin-bottom: 15px; border-bottom: 1px solid #eee; padding-bottom: 10px; }
        .faq-question { font-weight: bold; color: #2c3e50; }
        footer { text-align: center; margin-top: 50px; color: #888; font-size: 0.9em; }
    </style>
</head>
<body>

    <div class="card">
        <h1>💰 Wealth Calculator</h1>
        <p style="text-align:center; color: #666;">Plan your financial future with compound interest.</p>
        <form method="POST">
            <label>Initial Investment ($)</label>
            <input type="number" name="inicial" value="1000" required title="Amount of money you start with">
            <label>Monthly Contribution ($)</label>
            <input type="number" name="mensual" value="100" required title="Amount you add every month">
            <label>Years of Growth</label>
            <input type="number" name="anios" value="10" required title="How long you will invest">
            <label>Annual Interest Rate (%)</label>
            <input type="number" step="0.1" name="tasa" value="8" required title="Expected annual return">
            <button type="submit">Calculate My Future</button>
        </form>
        
        {% RESULTADO_AQUI %}
    </div>

    <div class="content-section">
        <h2>What is Compound Interest?</h2>
        <p>Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods. It is essentially "interest on interest" and will make your money grow much faster than simple interest.</p>
        
        <div class="faq">
            <h2>Frequently Asked Questions</h2>
            <div class="faq-item">
                <p class="faq-question">Why is the monthly contribution important?</p>
                <p>Even small monthly additions can significantly increase your final balance over time due to compounding.</p>
            </div>
            <div class="faq-item">
                <p class="faq-question">Is an 8% return realistic?</p>
                <p>While markets fluctuate, historical long-term stock market averages are often cited around 7-10%.</p>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2026 Financial Tools Hub. All rights reserved.</p>
    </footer>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    anios = None
    if request.method == 'POST':
        try:
            inicial = float(request.form['inicial'])
            mensual = float(request.form['mensual'])
            anios = int(request.form['anios'])
            tasa = float(request.form['tasa'])
            
            total = inicial
            tasa_mensual = (tasa / 100) / 12
            for _ in range(anios * 12):
                total = (total + mensual) * (1 + tasa_mensual)
            
            resultado = "{:,.2f}".format(total)
        except:
            resultado = "Error in calculation"
    
    if resultado:
        bloque_res = f'<div class="res">In {anios} years, you would have: <strong>${resultado}</strong></div>'
        return HTML_TEMPLATE.replace('{% RESULTADO_AQUI %}', bloque_res)
    else:
        return HTML_TEMPLATE.replace('{% RESULTADO_AQUI %}', '')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
