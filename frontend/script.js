async function calculate() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const operation = document.getElementById('operation').value;

    const response = await fetch('http://localhost:8000/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ num1: parseFloat(num1), num2: parseFloat(num2), operation })
    });

    const data = await response.json();
    const result = document.getElementById('result');
    result.textContent = data.result !== undefined ? `Result: ${data.result}` : `Error: ${data.error}`;
}
