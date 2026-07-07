# 📚 Bookswagon Web Scraping using Python & Selenium

## 📌 Project Overview

This project automates the process of collecting book information from the Bookswagon website using **Python** and **Selenium**. The scraper extracts book details from the search results page and stores the data in a structured CSV file for further analysis.

## 🚀 Features

- Opens the Bookswagon website automatically
- Searches for Python books
- Extracts:
  - 📖 Book Title
  - ✍️ Author
  - 💰 Price
  - ⭐ Rating
  - 🔗 Product Link
  - 🖼️ Image URL
- Saves the extracted data into a CSV file
- Handles dynamically loaded content using Selenium

## 🛠️ Technologies Used

- Python
- Selenium
- Pandas
- Chrome WebDriver
- VS Code

## 📂 Project Structure

```
Bookswagon-Web-Scraper
│
├── scraper.py
├── bookswagon_books.csv
├── requirements.txt
├── README.md
└── screenshots
    ├── scraper.png
    └── output.png
```
## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/bookswagon-web-scraper.git
```

Navigate into the project folder

```bash
cd bookswagon-web-scraper
```

Install the required libraries

```bash
pip install -r requirements.txt
```

or

```bash
pip install selenium pandas webdriver-manager
```

---

## ▶️ Run the Project

Execute the Python file

```bash
python scraper.py
```

The program will:

1. Launch Chrome
2. Open Bookswagon
3. Load the search results
4. Extract book information
5. Save the results as **bookswagon_books.csv**

---

## 📊 Sample Output

| Title | Author | Price | Rating |
|-------|--------|-------|--------|
| Computer Science with Python | Sumita Arora | ₹798 | 4.8 |
| Python Crash Course | Eric Matthes | ₹1299 | 4.7 |

---

## 💡 What I Learned

Through this project, I learned:

- Web Scraping using Selenium
- Browser Automation
- HTML Inspection
- CSS Selectors
- Handling Dynamic Websites
- Data Extraction
- Working with Pandas
- Exporting Data to CSV

