from flask import Flask, render_template, request

app=Flask(__name__)

def numBinary(numero):
    
    binario=''
    try:
        numero = int(numero) 
    except ValueError:
        return 'No disponible' 
    if numero>=0:
        while numero>0:
            binario=f'{numero % 2}{binario}'
            numero //=2
    else:
        numero = abs(numero)
        while numero > 0:
            binario = f'{numero % 2}{binario}'
            numero //= 2
        
        binario = binario.zfill(32)
        binario = ''.join('1' if x == '0' else '0' for x in binario)  
        binario = bin(int(binario, 2) + 1)[30:].zfill(4)
  
    return  '0' if binario=='' else binario

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numero = request.form.get("numero")
        if numero:
            resultado = numBinary(numero)
            return resultado
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)