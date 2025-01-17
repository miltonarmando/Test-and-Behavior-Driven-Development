// Function to fetch all products from the server
async function fetchProducts() {
    const response = await fetch("/products");  // Fetch products from the "/products" endpoint
    const products = await response.json();  // Parse the response as JSON
    renderProducts(products);  // Pass the products data to renderProducts function to display in the table
}

// Function to search for products based on user input
async function searchProducts() {
    // Get search criteria from the input fields
    const name = document.getElementById("search-name").value;
    const category = document.getElementById("search-category").value;
    const availability = document.getElementById("search-availability").checked;

    // Prepare URL parameters for the search query
    const params = new URLSearchParams();
    if (name) params.append("name", name);
    if (category) params.append("category", category);
    params.append("availability", availability);  // Convert checkbox state (checked/unchecked) to query param

    // Fetch search results from the server with the specified parameters
    const response = await fetch(`/products/search?${params.toString()}`);
    const products = await response.json();  // Parse the response as JSON
    renderProducts(products);  // Pass the search results to renderProducts function
}

// Function to add a new product to the database
async function addProduct() {
    // Get form values to create a new product
    const name = document.getElementById("name").value;
    const category = document.getElementById("category").value;
    const price = parseFloat(document.getElementById("price").value);  // Ensure price is a float
    const availability = document.getElementById("availability").checked;

    // Send a POST request to create the new product
    const response = await fetch("/products", {
        method: "POST",
        headers: { "Content-Type": "application/json" },  // Set content type to JSON
        body: JSON.stringify({ name, category, price, availability }),  // Send product data in the request body
    });

    if (response.ok) {
        fetchProducts();  // If the product is successfully created, fetch the updated product list
        clearForm();  // Clear the form inputs after submission
    }
}

// Function to update an existing product
async function updateProduct(id) {
    // Prompt user for new product details
    const name = prompt("Enter new name:");
    const category = prompt("Enter new category:");
    const price = parseFloat(prompt("Enter new price:"));
    const availability = confirm("Is it available?");  // Confirm if the product is available

    // Send a PUT request to update the product details
    const response = await fetch(`/products/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, category, price, availability }),
    });

    if (response.ok) fetchProducts();  // If update is successful, fetch the updated product list
}

// Function to delete a product by its ID
async function deleteProduct(id) {
    // Send a DELETE request to remove the product
    const response = await fetch(`/products/${id}`, { method: "DELETE" });
    if (response.ok) fetchProducts();  // If deletion is successful, fetch the updated product list
}

// Function to render the product list in the table
function renderProducts(products) {
    const tableBody = document.getElementById("product-table-body");  // Get the table body element
    tableBody.innerHTML = "";  // Clear any existing content in the table body
    
    // Iterate over each product and create a new table row
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
        tableBody.appendChild(row);  // Append the newly created row to the table body
    });
}

// Function to clear the form inputs
function clearForm() {
    document.getElementById("name").value = "";
    document.getElementById("category").value = "";
    document.getElementById("price").value = "";
    document.getElementById("availability").checked = false;  // Reset checkbox state
}

// Fetch the list of products when the page loads
window.onload = fetchProducts;
