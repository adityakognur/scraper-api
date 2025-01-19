
# Scraper API

## Overview
A FastAPI-based project for extracting product reviews from e-commerce sites like Amazon and Shopify. 
The API dynamically identifies review elements, handles pagination, and integrates OpenAI's API for review analysis.

---

## Features
- Extract product reviews dynamically.  # Dynamically locate and scrape review elements from product pages.
- Handle pagination seamlessly.        # Automatically navigate through paginated review sections.
- Analyze text using OpenAI API.       # Perform text analysis such as summarization or sentiment analysis.

---

## Requirements
- Python 3.8+                         # Ensure Python version is 3.8 or higher.
- Libraries: FastAPI, BeautifulSoup, Requests, OpenAI, etc.  # Required Python libraries.

---

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>          # Replace with your GitHub repository URL.
   cd scraper-api                      # Navigate to the project directory.
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv                 # Create a virtual environment.
   venv\Scripts\activate             # On Windows: Activate the virtual environment.
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt     # Install all required Python libraries.
   ```
4. Add your OpenAI API key in a `.env` file:  # Ensure the API key is correctly added to the environment file.
   ```env
   OPENAI_API_KEY=your_openai_api_key_here  # Replace with your actual OpenAI API key.
   ```
5. Start the server:
   ```bash
   uvicorn app.main:app --reload       # Start the FastAPI server in development mode.
   ```

---

## Endpoints
- `GET /`: Welcome route.              # A simple route to test if the server is running.
- `POST /scrape`: Scrapes product reviews.  # The main endpoint for scraping reviews.

---

## Usage
Use a tool like Postman or cURL to test the API. 
Provide the URL of the product page in the request body when accessing the `/scrape` endpoint.

---
