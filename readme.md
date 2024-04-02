# AmbitionBox Jobs Scraper

## Only for educational purpose


This is a web scraping tool built using Python and Streamlit to scrape job listings from AmbitionBox and display them in a tabular format. It allows users to search for jobs based on a keyword and download the scraped data as a CSV file.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Features

- **Search:** Users can search for jobs by entering a keyword.
- **Scraping:** The tool scrapes job listings from AmbitionBox based on the search query.
- **Display:** The scraped data is displayed in a tabular format with details such as company name, job title, rating, experience required, location, and skills.
- **Download:** Users can download the scraped data as a CSV file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Gorachand22/ambitionbox-jobs-scraper.git

   ```

2. Navigate to the project directory:

   ```bash
   cd ambitionbox-jobs-scraper
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Enter a keyword in the search box and click on the "Scrap" button to scrape job listings.
3. Wait for the scraping process to complete.
4. View the scraped data in the table.
5. Optionally, download the data as a CSV file using the download button.

## Dependencies

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/en/master/)
- [Streamlit](https://streamlit.io/)

## License

This project is licensed under the [MIT License](LICENSE).