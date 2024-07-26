# SpiderSearchTool Documentation

## Description
This tools enables you to retrieve search results from the internet using the [Spider.cloud](https://spider.cloud/) API.

## Installation
To incorporate this tool into your project, follow the installation instructions below:
```shell
pip install 'praisonai[tools]'
```

## Example
The following example demonstrates how to initialize the tool and execute a search with a given query:

```python
from praisonai_tools import SpiderSearchTool

# Initialize the tool for internet searching capabilities
tool = SpiderSearchTool()
```

## Steps to Get Started
To effectively use the `SpiderSearchTool`, follow these steps:

1. **Package Installation**: Confirm that the `praisonai[tools]` package is installed in your Python environment and that you have installed the Spider sdk by doing `pip install spider-client`.
2. **Get your API Key**: Find your Spider API key [here](https://spider.cloud/?utm_source=praisonai).
3. **Environment Configuration**: Store your obtained API key in an environment variable named `SPIDER_API_KEY` to facilitate its use by the tool.

## Conclusion
By following these steps, you will be able to effectively use the `SpiderSearchTool` to retrieve search results from the internet.
