import os
import json
import requests

from typing import Type, Any
from pydantic.v1 import BaseModel, Field
from praisonai_tools.tools.base_tool import BaseTool

class SpiderCrawlToolSchema(BaseModel):
	"""Input for SpiderCrawlTool."""
	query: str = Field(..., description="Mandatory search query you want to use to search the internet"),
	limit: int = Field(10, description="Number of results you want to get back from the search engine"),

class SpiderCrawlTool(BaseTool):
	name: str = "Crawl the web"
	description: str = "Tool to crawl the web with a query"
	args_schema: Type[BaseModel] = SpiderCrawlToolSchema

	def _run(
		self,
		**kwargs: Any,
	) -> Any:
		"""Run the tool."""
		try:
			from spider import Spider
		except ImportError:
			raise ImportError("run `pip install spider-client` to run this tool")
		
		query = kwargs.get("query")
		limit = kwargs.get("limit") or 10

		if not query:
			raise ValueError("You must provide a query to search the web")

		params = {
			"fetch_page_conten": False,
			"limit": limit,
		}

		spider = Spider()
		results = spider.search(query, **params)
		return results
		
