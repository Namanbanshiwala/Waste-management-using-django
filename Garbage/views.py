from django import forms
import requests
from django.shortcuts import redirect, render


NEWS_API_KEY = "4f9786b2fa9349bf9276177db196d22e"

class NewsSearchForm(forms.Form):
    country = forms.ChoiceField(
        choices=[
            ("us", "USA"),
            ("gb", "UK"),
            ("in", "India"),
            ("ca", "Canada"),
            ("au", "Australia"),
        ],
        label="Select Country",
    )
    keyword = forms.CharField(required=False, label="Search Keyword", initial="IPL")
    
def home_fetch_news():
    url = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={NEWS_API_KEY}"
    url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={NEWS_API_KEY}"
    url = f"https://newsapi.org/v2/everything?q=apple&from=2025-01-31&to=2025-01-31&sortBy=popularity&apiKey={NEWS_API_KEY}"
    # url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    # return data.get("articles", [])
    articles = [article for article in data.get("articles", []) if article.get("urlToImage")]
    return articles
def IPL_fetch_newss(country="in", keyword="Waste"):
    """Fetch news from NewsAPI for the given country and keyword"""
    url = f"https://newsapi.org/v2/everything?q={keyword}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = [article for article in data.get("articles", []) if article.get("urlToImage")]
    return articles

def News(request):
    country = "in"  # Default to India
    keyword = "Waste"  # Default to Waste news

    if request.method == "POST":
        form = NewsSearchForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data["country"]
            keyword = form.cleaned_data["keyword"]
    else:
        form = NewsSearchForm(initial={"country": country, "keyword": keyword})

    articles = IPL_fetch_newss(country, keyword)
    return render(request, "News.html", {"form": form, "articles": articles})