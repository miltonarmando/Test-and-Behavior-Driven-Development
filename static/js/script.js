// Function to fetch all products from the server
async function fetchProducts() {
    const response = await fetch("/products");
    const products = await response.json();
    renderProducts(products);
}

// Function to search for products based on user input
async function searchProducts() {
    const name = document.getElementById("search-name").value;
    const category = document.getElementById("search-category").value;
    const availability = document.getElementById("search-availability").checked;

    const params = new URLSearchParams();
    if (name) params.append("name", name);
    if (category) params.append("category", category);
    params.append("availability", availability);

    const response = await fetch(`/products/search?${params.toString()}`);
    
    if (response.ok) {
        const products = await response.json();
        renderProducts(products);
        alert("Search completed successfully!");
    } else {
        alert("Failed to search products.");
    }
}

// Function to add a new product to the database
async function addProduct() {
    const name = document.getElementById("name").value;
    const category = document.getElementById("category").value;
    const price = parseFloat(document.getElementById("price").value);
    const availability = document.getElementById("availability").checked;

    const response = await fetch("/products", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, category, price, availability }),
    });

    if (response.ok) {
        fetchProducts();
        clearForm();
        alert("Product added successfully!");
    } else {
        alert("Failed to add product.");
    }
}

// Function to update an existing product
async function updateProduct(id) {
    const name = prompt("Enter new name:");
    const category = prompt("Enter new category:");
    const price = parseFloat(prompt("Enter new price:"));
    const availability = confirm("Is it available?");

    const response = await fetch(`/products/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, category, price, availability }),
    });

    if (response.ok) {
        fetchProducts();
        alert("Product updated successfully!");
    } else {
        alert("Failed to update product.");
    }
}

// Function to delete a product by its ID
async function deleteProduct(id) {
    const response = await fetch(`/products/${id}`, { method: "DELETE" });

    if (response.ok) {
        fetchProducts();
        alert("Product deleted successfully!");
    } else {
        alert("Failed to delete product.");
    }
}

// Function to render the product list in the table
function renderProducts(products) {
    const tableBody = document.getElementById("product-table-body");
    tableBody.innerHTML = "";

    products.forEach(product => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${product.id}</td>
            <td>${product.name}</td>
            <td>${product.category}</td>
            <td>${product.price}</td>
            <td>${product.availability ? "Available" : "Unavailable"}</td>
            <td class="actions">
                <button class="update" onclick="updateProduct(${product.id})">Update</button>
                <button class="delete" onclick="deleteProduct(${product.id})">Delete</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

// Function to clear the form inputs
function clearForm() {
    document.getElementById("name").value = "";
    document.getElementById("category").value = "";
    document.getElementById("price").value = "";
    document.getElementById("availability").checked = false;
}

// Fetch the list of products when the page loads
window.onload = fetchProducts;
