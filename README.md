
# Product Management Web App

## Description

This **Product Management Web App** allows users to manage products in a web-based application. The app allows for CRUD operations (Create, Read, Update, Delete) on products, and supports filtering by category, availability, and searching by name. The app is built using **Flask** for the backend and **HTML, CSS, and JavaScript** for the frontend.

---

## Features

- **CRUD Operations**: Create, read, update, and delete products.
- **Filtering and Searching**: Search products by name, category, and availability.
- **Product Management**: Allows users to add, edit, and remove products from the database.
- **Responsive Design**: Works seamlessly on both desktop and mobile devices.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package installer)
- **Flask** (Web framework)

If you don't have **Python** and **pip** installed, download and install the latest version of Python from [python.org](https://www.python.org/).

---

## Setup Instructions

### 1. Clone the Repository

Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/yourusername/product-management-web-app.git
cd product-management-web-app
```

### 2. Create a Virtual Environment

A virtual environment ensures that your project's dependencies are isolated and do not affect your global Python environment.

- **Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scriptsctivate
  ```

Once activated, your terminal prompt should change to indicate that the virtual environment is active.

### 3. Install Dependencies

With the virtual environment active, install the project dependencies by running:

```bash
pip install -r requirements.txt
```

This will install the necessary Python libraries such as Flask and others.

### 4. Set Up the Database

Ensure you have the database set up. You can configure your database connection in the `config.py` file. For local development, SQLite can be used.

### 5. Run the Flask Application

Start the Flask application by running:

```bash
python app.py
```

The application will be hosted at `http://127.0.0.1:5000/`. Open this URL in your browser to see the app in action.

### 6. Run the Tests

You can run the automated tests to ensure everything is working correctly:

```bash
pytest
```

This will run all the test cases in the project.

---

## Folder Structure

```
/product-management-web-app
    /instance               # Automatically generated - Configuration data (ignored by Git)
    /static                 # Static files (CSS, JavaScript, images)
        /css                # Stylesheets (style.css)
        /js                 # JavaScript files (script.js)
    /templates              # HTML templates
        /index.html         # Main page
    /app.py                 # Main Flask app
    /requirements.txt       # Project dependencies
    /test_app.py            # Test cases for app functionality
    README.md               # Project documentation
```

---

## Usage

### Product Management Features

- **Create a Product**: Go to the product creation page (`/create-product`) and fill in the product details (name, category, availability, etc.). Submit the form to add the product.
- **Read a Product**: View a product by navigating to the product details page (`/product/<product_id>`).
- **Update a Product**: Edit the product details by visiting the product's edit page (`/edit-product/<product_id>`).
- **Delete a Product**: Delete a product from the database by navigating to the product detail page and clicking the delete button.
- **Search and Filter**: You can search for products by name, filter products by category, and check for availability.

---

## Running in Production

For production environments, ensure the following:

- Set `FLASK_ENV=production` to enable production mode.
- Use a production-ready server like **Gunicorn** to run the Flask app.
- Set up a robust database like PostgreSQL or MySQL.
- Ensure that you configure **security settings** (e.g., `SECRET_KEY`, CSRF protection) properly in `config.py`.

---

## Testing

This project includes tests for the application:

- **Unit Tests**: Located in the `test_app.py` file.
- **BDD Tests**: If you are using BDD, you may have `.feature` files and step definitions located in the `features/` folder.

To run the tests:

```bash
pytest
```

You can run tests for specific files by specifying the test file:

```bash
pytest test_app.py
```

---

## Example of API Endpoints

Here are some example routes that are used to interact with the product management system:

- `GET /products`: List all products.
- `GET /product/<product_id>`: Get a product by ID.
- `POST /create-product`: Create a new product.
- `PUT /edit-product/<product_id>`: Edit an existing product.
- `DELETE /delete-product/<product_id>`: Delete a product by ID.

---

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your changes (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
