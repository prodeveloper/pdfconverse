# SmartPDF

PDFConverse is a Python tool that allows you to interact with PDF documents using AI, leveraging the Gemini API to provide intelligent responses to queries about PDF content. It optimizes token usage and enables focused analysis of specific page ranges.

## Features

- Interact with individual pages or page ranges in your PDF
- Run AI-powered prompts on specific sections of your document
- Avoid the problem of passing too much information to the model
- Save tokens by targeting specific pages or ranges
- Built-in sanity checks for better performance and reliability

## Installation

You can install PDFConverse using pip:

```
pip install pdfconverse
```

## Usage

Here's a basic example of how to use PDFConverse:

```python
import os
from pdfconverse import PDFConverse

# Set up your PDF path and Gemini API key. Assuming you have a .env file with the Gemini API key
pdf_path = "./path/to/your/document.pdf"
gemini_key = os.getenv("GEMINI_API_KEY")

# Initialize PDFConverse
pdfconverse = PDFConverse(pdf_path=pdf_path, gemini_key=gemini_key)

# Get a summary of the first page
summary = pdfconverse.page(page_start=0, page_end=0).prompt("Give me a summary")
print(summary)
```

## Use Cases

1. **Reading Aid**: Use PDFConverse as a reading assistant, summarizing individual pages as you go through a document.
2. **Targeted Analysis**: Focus on specific sections of a large document without processing unnecessary content.
3. **Document Q&A**: Ask questions about particular pages or sections of your PDF.

## Caution

While PDFConverse can summarize or interact with entire books, please be aware that this may lead to expensive bills from the Gemini API. Always monitor your usage and costs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Gemini API for powering the AI interactions
- Inspired by the need for more granular control over AI-document interactions