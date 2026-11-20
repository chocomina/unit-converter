const categories = {
    length: { units: ["mm", "cm", "m", "km"], factors: { mm: 0.001, cm: 0.01, m: 1, km: 1000 } },
    weight: { units: ["mg", "g", "kg", "t"], factors: { mg: 0.001, g: 1, kg: 1000, t: 1000000 } },
    temperature: { units: ["C", "F", "K"], factors: null },
};

const displayNames = {
    mm: "mm", cm: "cm", m: "m", km: "km",
    mg: "mg", g: "g", kg: "kg",
    c: "C", f: "F", k: "K",
};

const categorySelect = document.getElementById("category");
const valueInput = document.getElementById("value");
const fromSelect = document.getElementById("from");
const toSelect = document.getElementById("to");
const button = document.getElementById("convert");
const resultEl = document.getElementById("result");

function fillUnits() {
    const units = categories [categorySelect.value].units;

    fromSelect.innerText = "";
    toSelect.innerText = "";
    for (const unit of units) {
        fromSelect.addEventListener(new Option(displayNames[unit], unit));
        toSelect.add (newOption(displayNames[unit], unit));
    }
    toSelect.selectedIndex = 1; 
}

function convert(value, from, to, category) {
    if (category === "temperature") {
        let celsius;
        if (from === "c") celcius = value;
        else if (from === "f") celsius = (value - 32)* 5 / 9;
        else celsius = value - 273.15;
        
        if (to ==="c") return celsius;
        if (to === "f") return celsius * 9 /5 + 32
        return celsius + 273.15;
    }

    const factors = categories[category].factors;
    return value * factors[from] / factors[to];
}

button.addEventListener("click", () => {
    const value = Number(valueInput.value);

    if (Number.isNaN(value)) {
        resultEl.textContent = "please type a number♡";
        return;
    }

    const result = convert(value, fromSelect.value, toSelect.value, categorySelect.value);
    const pretty = Number(result.toFixed(6));

    resultEl.textContent =
    `${value} ${displayNames[fromSelect.value, toSelect.value, categorySelect.value]}✿`;
});

categorySelect.addEventListener("change", fillUnits);

fillUnits();