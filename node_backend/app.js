document.getElementById('bmi-form').addEventListener('submit', function (event) {
    event.preventDefault();

    // Get weight and height input
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);

    // Calculate BMI
    const bmi = weight / (height * height);
    const category = getBMICategory(bmi);

    // Update UI with the calculated BMI
    document.getElementById('bmi-result').textContent = bmi.toFixed(2);
    document.getElementById('bmi-category').textContent = category;

    // Fetch health tips based on the category
    fetchHealthTips(category);
});

function getBMICategory(bmi) {
    if (bmi < 18.5) return 'Underweight';
    if (bmi >= 18.5 && bmi < 24.9) return 'Normal weight';
    if (bmi >= 25 && bmi < 29.9) return 'Overweight';
    return 'Obese';
}

function fetchHealthTips(bmiCategory) {
    fetch(`https://api.example.com/fitness/tips?category=${bmiCategory}`, {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer YOUR_API_KEY'
        }
    })
    .then(response => response.json())
    .then(data => {
        const tipsDiv = document.getElementById('health-tips');
        tipsDiv.innerHTML = "<h3>Health Tips:</h3>";
        data.tips.forEach(tip => {
            const p = document.createElement('p');
            p.textContent = tip;
            tipsDiv.appendChild(p);
        });
    })
    .catch(error => console.error("Error fetching health tips:", error));
}
