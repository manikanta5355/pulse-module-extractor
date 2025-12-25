\# Pulse – Module Extraction AI Agent



\## Overview

This project extracts structured modules and submodules from documentation-based

help websites. The goal is to identify key product modules and their submodules and

generate accurate, structured descriptions based entirely on documentation content.



\## Core Features

\- Accepts documentation URLs via command-line input

\- Extracts modules and submodules using document hierarchy

\- Generates structured JSON output

\- Supports multiple documentation sources



\## Architecture Overview

The system follows a modular pipeline:

1\. URL input via command-line

2\. HTML content retrieval using HTTP requests

3\. Structural parsing using BeautifulSoup

4\. Module and submodule inference using heading hierarchy

5\. Structured JSON generation



\## Technical Approach

\- h2 tags are treated as top-level modules

\- h3 tags are treated as submodules

\- Descriptions are generated based on extracted content context

\- Output is normalized into a consistent JSON schema



\## AI Perspective

While the current implementation relies on structural cues for high precision,

the same pipeline can be enhanced using AI-based semantic inference techniques

such as embeddings or LLMs to improve topic grouping and description quality.


## 📹 Video Explanation
A short video explaining the approach, design, and working of this project.

▶️ **Google Drive Link:**  
https://drive.google.com/drive/folders/1h_uufkw1vIH0A5uM7Iv57fW9m2ryjY2o?usp=drive_link


\## How to Run

```bash

pip install -r requirements.txt

python module_extractor.py https://wordpress.org/documentation/





