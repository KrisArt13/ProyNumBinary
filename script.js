let pantalla = document.getElementById('pantalla');
let numeroIngresado = "";

function agregarValor(valor) {
    if (valor === '-' && numeroIngresado === "") {
        numeroIngresado = "-";  
    } else if (valor !== '-') {
        numeroIngresado += valor;
    }
    pantalla.value = numeroIngresado;
}

function limpiar() {
    numeroIngresado = "";
    pantalla.value = "";
}

function convertir() {
    if (numeroIngresado !== "") {
        fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `numero=${numeroIngresado}`
        })
        .then(response => response.text())  
        .then(data => {
            document.getElementById('resultado').innerText = data;
        })
        .catch(error => {
            document.getElementById('resultado').innerText = 'Error';
        });
    }
}
