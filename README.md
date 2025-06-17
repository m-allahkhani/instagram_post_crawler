# Instagram Crawler

## Overview
This project is a Python-based Instagram crawler that logs into a specified account, retrieves the links of all posts, and saves them in an organized JSON file. Additionally, it integrates with **QrGraphyCrawler** to generate QR codes for each link saved in the JSON file.

## Features
- Automates the login process to Instagram.
- Collects and saves links of all posts from a specified account.
- Generates QR codes for each post link using the QrGraphy service.

## Requirements
- Python 3.x
- Required libraries:
  - `requests`
  - `Selenium` (for web automation)
  - `json`
  - `qrcode` (for generating QR codes)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/instagram-crawler.git
   cd instagram-crawler
