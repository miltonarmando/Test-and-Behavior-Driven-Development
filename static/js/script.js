// Function to fetch all products from the server
async function fetchProducts() {
    const response = await fetch("/products");  // Sending a GET request to fetch all products
    const products = await response.json();  // Parsing the response as JSON
    renderProducts(products);  // Rendering the products in the table
}

// Function to search for products based on user input
async function searchProducts() {
    // Retrieving search criteria from input fields
    const name = document.getElementById("search-name").value;
    const category = document.getElementById("search-category").value;
    const availability = document.getElementById("search-availability").checked;

    // Building URL search parameters
    const params = new URLSearchParams();
    if (name) params.append("name", name);
    if (category) params.append("category", category);
    params.append("availability", availability);

    const response = await fetch(`/products/search?${params.toString()}`);  // Sending a GET request to search products
    
    if (response.ok) {
        const products = await response.json();  // Parsing the response as JSON
        renderProducts(products);  // Rendering the filtered products
        alert("Search completed successfully!");  // Alerting the user of the successful search
    } else {
        alert("Failed to search products.");  // Alerting the user if the search fails
    }
}

// Function to add a new product to the database
async function addProduct() {
    // Retrieving the new product details from the form
    const name = document.getElementById("name").value;
    const category = document.getElementById("category").value;
    const price = parseFloat(document.getElementById("price").value);
    const availability = document.getElementById("availability").checked;

    const response = await fetch("/products", {
        method: "POST",  // Sending a POST request to add a new product
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, category, price, availability }),  // Sending the product details in the request body
    });

    if (response.ok) {
        fetchProducts();  // Refreshing the product list
        clearForm();  // Clearing the form fields
        alert("Product added successfully!");  // Alerting the user of the successful addition
    } else {
        alert("Failed to add product.");  // Alerting the user if the addition fails
    }
}

// Function to update an existing product
async function updateProduct(id) {
    // Prompting the user to enter new product details
    const name = prompt("Enter new name:");
    const category = prompt("Enter new category:");
    const price = parseFloat(prompt("Enter new price:"));
    const availability = confirm("Is it available?");  // Asking if the product is available

    const response = await fetch(`/products/${id}`, {
        method: "PUT",  // Sending a PUT request to update the product
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, category, price, availability }),  // Sending the updated product details in the request body
    });

    if (response.ok) {
        fetchProducts();  // Refreshing the product list
        alert("Product updated successfully!");  // Alerting the user of the successful update
    } else {
        alert("Failed to update product.");  // Alerting the user if the update fails
    }
}

// Function to delete a product by its ID
async function deleteProduct(id) {
    const response = await fetch(`/products/${id}`, { method: "DELETE" });  // Sending a DELETE request to remove the product

    if (response.ok) {
        fetchProducts();  // Refreshing the product list
        alert("Product deleted successfully!");  // Alerting the user of the successful deletion
    } else {
        alert("Failed to delete product.");  // Alerting the user if the deletion fails
    }
}

// Function to render the product list in the table
function renderProducts(products) {
    const tableBody = document.getElementById("product-table-body");
    tableBody.innerHTML = "";  // Clearing the table before rendering new data

    products.forEach(product => {
        const row = document.createElement("tr");  // Creating a new table row for each product
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
        tableBody.appendChild(row);  // Appending the row to the table body
    });
}

// Function to clear the form inputs
function clearForm() {
    document.getElementById("name").value = "";
    document.getElementById("category").value = "";
    document.getElementById("price").value = "";
    document.getElementById("availability").checked = false;  // Resetting the form fields
}

// Fetch the list of products when the page loads
window.onload = fetchProducts;  // Calling fetchProducts when the page is loaded to display the products
