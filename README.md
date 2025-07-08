# Tableau MCP Sentiment Analysis Server

This project provides a simple, yet powerful, Python-based Analytics Extension (often referred to as an MCP server) that integrates directly with Tableau Desktop. Its primary function is to perform **sentiment analysis** on text data, allowing you to unlock deeper insights from your qualitative data directly within your Tableau dashboards.

## Why Use This?

Tableau is excellent for visualizing structured data, but it has limitations when it comes to advanced text analysis. Imagine you have a dataset filled with customer comments, survey responses, or social media posts. How do you quickly understand the overall sentiment – are your customers happy or unhappy?

This Analytics Extension bridges that gap. It allows you to:

*   **Transform Unstructured Text into Actionable Data:** Convert raw text into quantifiable sentiment categories (Positive, Negative, Neutral).
*   **Enhance Your Tableau Dashboards:** Integrate sentiment scores as a new dimension or measure, enabling powerful visualizations and filtering based on customer emotion.
*   **Gain Deeper Insights:** Understand the emotional tone behind feedback, identify trends, and pinpoint areas for improvement or success.
*   **No Coding Required in Tableau:** Once the server is set up, you interact with it using a simple calculated field, just like any other Tableau function.

## What It Does

This server exposes a simple API endpoint that takes text as input and returns its sentiment:

*   **Sentiment Classification:** Analyzes input text and categorizes it as "Positive," "Negative," or "Neutral."
*   **Tableau Integration:** Designed specifically to work seamlessly as an Analytics Extension (formerly known as an External Service or TabPy connection) in Tableau Desktop.
*   **Lightweight & Local:** Runs locally on your machine, making it easy to set up and use without external cloud dependencies.

## Use Cases

*   **Customer Feedback Analysis:** Analyze product reviews, support tickets, or survey comments to gauge customer satisfaction and identify common pain points or delights.
*   **Social Media Monitoring:** Track brand perception by analyzing mentions and comments on social platforms.
*   **Employee Engagement:** Understand the sentiment in internal survey responses or feedback channels.
*   **Market Research:** Analyze open-ended responses from focus groups or market surveys to uncover underlying attitudes.
*   **News & Media Analysis:** Determine the sentiment of news articles or reports related to specific topics or companies.

## Getting Started

Follow these steps to set up and run your Sentiment Analysis server.

### Prerequisites

*   **Python 3.x:** Ensure Python is installed on your system.
*   **Git:** For cloning the repository.

### 1. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/SudheerNaraharisetty/tableau-mcp-sentiment-analysis.git
cd tableau-mcp-sentiment-analysis
```

### 2. Install Dependencies

Navigate into the cloned directory and install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 3. Download TextBlob Corpora

TextBlob requires some linguistic data to perform sentiment analysis. Download it using:

```bash
python -m textblob.download_corpora
```

## Running the Server

To start the sentiment analysis server, execute the following command from the `tableau-mcp-sentiment-analysis` directory:

```bash
python app.py
```

The server will start and listen for requests on `http://127.0.0.1:5001`. You will see output in your terminal indicating that the Flask development server is running. Keep this terminal window open while you are using Tableau.

## Integrating with Tableau Desktop

Once the server is running, you can connect Tableau Desktop to it.

### 1. Configure Analytics Extension Connection

1.  Open **Tableau Desktop**.
2.  Go to **Help > Settings and Performance > Manage Analytics Extension Connection...**
3.  In the dialog box, select **TabPy/External API**.
4.  Enter the following details:
    *   **Server:** `localhost`
    *   **Port:** `5001`
5.  Click **Test Connection**. You should see a "Successfully connected to the Analytics Extension" message.
6.  Click **OK**.

### 2. Create a Calculated Field in Tableau

Now you can use the sentiment analysis server in your Tableau worksheets.

1.  In your Tableau workbook, go to **Analysis > Create Calculated Field...**
2.  Name your calculated field (e.g., `Sentiment Score`).
3.  Enter the following formula:

    ```tableau
    SCRIPT_STR(
        "/evaluate",
        ATTR([Your TextField])
    )
    ```
    *   Replace `[Your TextField]` with the actual name of the field in your data source that contains the text you want to analyze (e.g., `[Customer Comments]`, `[Review Text]`).
    *   The `/evaluate` path corresponds to the endpoint on our Python server.

4.  Click **OK**.

Tableau will now send the text from `[Your TextField]` to your running Python server, and the server will return "Positive," "Negative," or "Neutral" for each row. This new `Sentiment Score` calculated field can then be used in your visualizations, filters, and aggregations just like any other field!

## How It Works (Brief Technical Overview)

*   **Flask (`app.py`):** A lightweight Python web framework that creates the server. It listens for incoming requests from Tableau.
*   **TextBlob:** A Python library for processing textual data. It provides a simple API for common natural language processing (NLP) tasks, including sentiment analysis.
*   **Tableau Analytics Extension Protocol:** Tableau communicates with the server using a specific JSON-based protocol. The server is designed to understand Tableau's requests (sent to the `/evaluate` endpoint) and return responses in the expected format (a list of results).

## Troubleshooting

*   **"Error: An error occurred on the server" in Tableau:** Check the terminal where your `app.py` server is running for any Python error messages.
*   **"Connection Failed" in Tableau:**
    *   Ensure the Python server (`app.py`) is running.
    *   Verify the port (`5001`) is correct and not blocked by a firewall.
    *   Make sure you typed `localhost` correctly.
*   **`ImportError` during `pip install` or `python app.py`:** Ensure all dependencies are correctly installed and that you are using a compatible Python version. If you encounter `Werkzeug` related errors, ensure `Werkzeug==2.2.2` is specified in `requirements.txt`.

---
