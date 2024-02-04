# NewsSender

## Description

The Email News App is a Python application designed to automatically send news updates to users via email based on their specified interests. The application fetches news from various sources using the NewsAPI, formats it, and sends it out as personalized email digests.

## Key Features and Improvements

Originally this app was created following the guide from pythonprocourse [Intermediate to Advanced Python with 10 OOP Projects](https://www.udemy.com/course/the-python-pro-course/). Later the following improvements were implemented independently.
- Sensitive information like API keys and email credentials are stored externally in a .txt file.
- Error Handling: Improved error handling for more robust news fetching and email sending.
- Unit Tests were added.
- Logging: Integrated logging for tracking application operations, successes, and failures.

## Further Improvements Scope

- Web Interface: A user-friendly interface for managing preferences.
- Asynchronous Operations: Implementing async for improved efficiency.
- Database Integration: Moving from Excel to a more scalable database solution.
- HTML Email Templates: Enhancing email aesthetics with HTML formatting.
- News Summarization: Add an opportunity to get not the titles and links, but the summary of the latest news, created by LLM.
- Caching: Implement caching for news articles to reduce the number of API requests

## Setup and Implementation

1. Clone the Repository
`git clone <https://github.com/AlexeyKarz/NewsSender.git>`
2. Install Dependencies. Ensure you have Python installed and run:
`pip install -r requirements.txt`
3. API Key and Email Credentials. Obtain an API key from [NewsAPI](https://newsapi.org).
Create a apigmailpass.txt file in the root directory with your NewsAPI key, email, and password separated by commas (e.g., api_key,email@example.com,password).
4. Change people.xlsx
Add working emails to run the app. For testing I used the disposable email addreses using [DropMail](https://dropmail.me/en/)
5. Change the time for getting emails.
Set the time (hour, minute) when you want to recieve the emails (for testing set the time on 1 minute than the current time) in *main.py::49*
6. Running the Application
Execute the main.py script to start sending news emails:
`python main.py`

## Contribution

Feedback and contributions are welcomed!

## License

This project is open-sourced under the MIT license.

