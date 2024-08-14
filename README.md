
# Blog Scraper and Question Generator

This project is a Python-based web scraping tool that extracts blog posts from the [Investing in AI](https://investinginai.substack.com) newsletter. The extracted blog content is then processed using OpenAI's GPT models to generate insightful questions for podcast interviews. The scraped content and generated questions are saved in CSV files for further use.

## Features

- **Web Scraping with Selenium**: Automatically scrolls through the newsletter's archive page and extracts links to individual blog posts.
- **Content Extraction**: Extracts the full text of each blog post.
- **Question Generation with OpenAI GPT**: Generates thoughtful questions based on the blog content for podcast interviews.
- **CSV Export**: Saves blog content and generated questions to CSV files.

## Prerequisites

Before running the scripts, make sure you have the following installed:

- Python 3.x
- [Selenium](https://www.selenium.dev/documentation/) library
- Chrome WebDriver (Make sure it's compatible with your installed Chrome version)
- [OpenAI Python client library](https://github.com/openai/openai-python)