function enterSpace() {
    alert("Welcome to TCW SPACE 🚀");
}

fetch("http://127.0.0.1:5000/api/products")
.then(res => res.json())
.then(data => {
    let container = document.getElementById("products");

    data.forEach(p => {
        let div = document.createElement("div");
        div.innerHTML = `
            <div style="border:1px solid #b300ff;padding:20px">
                <h3>${p.name}</h3>
                <p>$${p.price}</p>
            </div>
        `;
        container.appendChild(div);
    });
});
