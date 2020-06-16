from __future__ import unicode_literals

import requests

from newsapi import const
from newsapi.newsapi_auth import NewsApiAuth
from newsapi.newsapi_exception import NewsAPIException
from newsapi.utils import is_valid_string, stringify_date_param


class NewsApiClient(object):
      def __init__(self, api_key, session=None):
        self.auth = NewsApiAuth(api_key=api_key)
        if session is None:
            self.request_method = requests
        else:
            self.request_method = session

    def get_top_headlines(  # noqa: C901
        self, q=None, qintitle=None, sources=None, language="en", country=None, category=None, page_size=None, page=None
    ):
        payload = {}

        # Keyword/Phrase
        if q is not None:
            if is_valid_string(q):
                payload["q"] = q
            else:
                raise TypeError("keyword/phrase q param should be of type str")

        # Keyword/Phrase in Title
        if qintitle is not None:
            if is_valid_string(qintitle):
                payload["qintitle"] = qintitle
            else:
                raise TypeError("keyword/phrase qintitle param should be of type str")

        # Sources
        if (sources is not None) and ((country is not None) or (category is not None)):
            raise ValueError("cannot mix country/category param with sources param.")

        # Sources
        if sources is not None:
            if is_valid_string(sources):
                payload["sources"] = sources
            else:
                raise TypeError("sources param should be of type str")

        # Language
        if language is not None:
            if is_valid_string(language):
                if language in const.languages:
                    payload["language"] = language
                else:
                    raise ValueError("invalid language")
            else:
                raise TypeError("language param should be of type str")

        # Country
        if country is not None:
            if is_valid_string(country):
                if country in const.countries:
                    payload["country"] = country
                else:
                    raise ValueError("invalid country")
            else:
                raise TypeError("country param should be of type str")

        # Category
        if category is not None:
            if is_valid_string(category):
                if category in const.categories:
                    payload["category"] = category
                else:
                    raise ValueError("invalid category")
            else:
                raise TypeError("category param should be of type str")

        # Page Size
        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload["pageSize"] = page_size
                else:
                    raise ValueError("page_size param should be an int between 1 and 100")
            else:
                raise TypeError("page_size param should be an int")

        # Page
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload["page"] = page
                else:
                    raise ValueError("page param should be an int greater than 0")
            else:
                raise TypeError("page param should be an int")

        # Send Request
        r = self.request_method.get(const.TOP_HEADLINES_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()

    def get_everything(  # noqa: C901
        self,
        q=None,
        qintitle=None,
        sources=None,
        domains=None,
        exclude_domains=None,
        from_param=None,
        to=None,
        language=None,
        sort_by=None,
        page=None,
        page_size=None,
    ):
       

        payload = {}

        # Keyword/Phrase
        if q is not None:
            if is_valid_string(q):
                payload["q"] = q
            else:
                raise TypeError("keyword/phrase q param should be of type str")

        # Keyword/Phrase in Title
        if qintitle is not None:
            if is_valid_string(qintitle):
                payload["qintitle"] = qintitle
            else:
                raise TypeError("keyword/phrase qintitle param should be of type str")

        # Sources
        if sources is not None:
            if is_valid_string(sources):
                payload["sources"] = sources
            else:
                raise TypeError("sources param should be of type str")

        # Domains To Search
        if domains is not None:
            if is_valid_string(domains):
                payload["domains"] = domains
            else:
                raise TypeError("domains param should be of type str")

        if exclude_domains is not None:
            if isinstance(exclude_domains, str):
                payload["excludeDomains"] = exclude_domains
            else:
                raise TypeError("exclude_domains param should be of type str")

        # Search From This Date ...
        if from_param is not None:
            payload["from"] = stringify_date_param(from_param)

        # ... To This Date
        if to is not None:
            payload["to"] = stringify_date_param(to)

        # Language
        if language is not None:
            if is_valid_string(language):
                if language not in const.languages:
                    raise ValueError("invalid language")
                else:
                    payload["language"] = language
            else:
                raise TypeError("language param should be of type str")

        # Sort Method
        if sort_by is not None:
            if is_valid_string(sort_by):
                if sort_by in const.sort_method:
                    payload["sortBy"] = sort_by
                else:
                    raise ValueError("invalid sort")
            else:
                raise TypeError("sort_by param should be of type str")

        # Page Size
        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload["pageSize"] = page_size
                else:
                    raise ValueError("page_size param should be an int between 1 and 100")
            else:
                raise TypeError("page_size param should be an int")

        # Page
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload["page"] = page
                else:
                    raise ValueError("page param should be an int greater than 0")
            else:
                raise TypeError("page param should be an int")

        # Send Request
        r = self.request_method.get(const.EVERYTHING_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()

    def get_sources(self, category=None, language=None, country=None):  # noqa: C901
       

        payload = {}

        # Language
        if language is not None:
            if is_valid_string(language):
                if language in const.languages:
                    payload["language"] = language
                else:
                    raise ValueError("invalid language")
            else:
                raise TypeError("language param should be of type str")

        # Country
        if country is not None:
            if is_valid_string(country):
                if country in const.countries:
                    payload["country"] = country
                else:
                    raise ValueError("invalid country")
            else:
                raise TypeError("country param should be of type str")

        # Category
        if category is not None:
            if is_valid_string(category):
                if category in const.categories:
                    payload["category"] = category
                else:
                    raise ValueError("invalid category")
            else:
                raise TypeError("category param should be of type str")

        # Send Request
        r = self.request_method.get(const.SOURCES_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()
