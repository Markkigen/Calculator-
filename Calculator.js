function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculate() {
    try {
        document.getElementById('display').value = eval(document.getElementById('display').value);
    } catch (e) {
        document.getElementById('display').value = 'Error';
    }
}

function deleteLast() {
    const display = document.getElementById("display");
    display.value = display.value.slice(0, -1);
}

function clearentry() {
    const display = document.getElementById('display');
    display.value = '';
}


