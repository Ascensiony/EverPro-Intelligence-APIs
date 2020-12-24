from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .engine import search

import json
from difflib import SequenceMatcher
from django.utils.html import escape


def select_best(query: str, amazon_results: list, flipikart_results: list):
    if amazon_results is None and flipikart_results is None:
        return []

    amazon_results = amazon_results[:5] if len(
        amazon_results) > 5 else amazon_results
    flipikart_results = (
        flipikart_results[:5] if len(
            flipikart_results) > 5 else flipikart_results
    )

    # amazon_results = [data+data["engine"]="Amazon" for data in amazon_results]
    # flipikart_results = [data+data["engine"]="Flipkart" for data in flipikart_results]

    for index, _ in enumerate(amazon_results):
        amazon_results[index]["engine"] = "Amazon"
    for index, _ in enumerate(flipikart_results):
        flipikart_results[index]["engine"] = "Flipikart"

    results = amazon_results + flipikart_results
    for index, _ in enumerate(results):
        try:
            results[index]["closeness"] = SequenceMatcher(
                None, query, results[index]["product_name"]
            ).ratio()

        except Exception as e:
            del results[index]
            continue

    results = sorted(results, key=lambda k: k["closeness"])

    return results


def search_product(request):

    if request.method == "POST":
        try:
            query = str(request.POST["query"]).strip().lower()

            search(query)

            with open("search/engines/amazon.json", "r", encoding="utf-8") as f:
                amazon_results = json.load(f)
            with open("search/engines/flipkart.json", "r", encoding="utf-8") as f:
                flipikart_results = json.load(f)

            results = select_best(query, amazon_results, flipikart_results)

            if results is None:
                return render(
                    request,
                    "index.html",  # needs to be edited
                    {
                        "error": "Sorry, no results found for your passed query",
                        "code": 204,
                    },
                )
            return render(
                request,
                "index.html",  # needs to be edited
                {"search_results": json.dumps(results), "code": 200},
            )

        except Exception as e:
            print("Exception in Engine")
            print(e)

            return render(
                request,
                "index.html",  # needs to be edited
                {
                    "error": "Sorry, Some internal error occurred, please report this to us!",
                    "code": 500,
                },
            )
