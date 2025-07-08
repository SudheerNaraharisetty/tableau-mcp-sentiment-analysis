# Tableau MCP Sentiment Analysis Server

This project contains a simple Python-based MCP (Analytics Extension) server for performing sentiment analysis in Tableau.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd tableau-mcp-sentiment-analysis
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download TextBlob corpora:**
    ```bash
    python -m textblob.download_corpora
    ```

## Running the Server

To start the server, run the following command:

```bash
python app.py
```

The server will start on `http://127.0.0.1:5001`.

## Using in Tableau

1.  Open Tableau Desktop.
2.  Go to **Help > Settings and Performance > Manage Analytics Extension Connection**.
3.  Select **TabPy/External API**.
4.  Enter the server details:
    *   **Server:** `localhost`
    *   **Port:** `5001`
5.  Create a new calculated field in your workbook with the following formula:
    ```
    SCRIPT_STR("/sentiment", ATTR([Your TextField]))
    ```
    Replace `[Your TextField]` with the field in your data that contains the text you want to analyze.