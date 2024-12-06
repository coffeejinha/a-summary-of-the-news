# A Summary of the News

## Introduction
This project, "A Summary of the News," is designed to provide concise summaries of lengthy news articles. Using Hugging Face's KoBART model, it offers a streamlined and user-friendly interface for extracting key information from Korean news articles.

## Features
- Scrapes the full text of news articles from specified URLs.
- Summarizes lengthy articles into digestible text using the KoBART summarization model.
- Handles articles that exceed the model's input size by splitting and processing them in chunks.

## How It Works
1. **Scraping News Articles**:
   - The application extracts the full text of a news article from a provided URL. (Currently optimized for Naver News articles.)
   
2. **Text Summarization**:
   - The extracted text is summarized using Hugging Face's KoBART model.
   - If the article is too long, it is split into smaller chunks for processing.

3. **Output**:
   - The summarized text is displayed to the user.

## Setup
1. Clone the repository.
2. Install the required Python packages:
   ```bash
   pip install transformers torch requests beautifulsoup4
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Known Issues
### Device Configuration Error
In the function `load_kobart_summarizer`, the following line may cause an error:
```python
return pipeline("summarization", model=model, tokenizer=tokenizer, device=0)
```
**Issue**: This line configures the application to use GPU (`device=0`). If your system does not have a GPU or it is not properly configured, you will encounter a `ValueError: 0 unrecognized or not available.` error.

**Solution**: Modify `device=0` to `device=-1` to use CPU instead of GPU:
```python
return pipeline("summarization", model=model, tokenizer=tokenizer, device=-1)
```

## Additional Notes
- Ensure that your environment supports the Hugging Face models and dependencies.
- If the news scraping fails, verify the structure of the website or provide an alternative URL.

## Future Enhancements
- Extend support for other news websites by customizing the scraping function.
- Introduce additional models for multilingual summarization.
- Create a GUI for easier access and usability.

---

For more details and updates, refer to the project repository.


