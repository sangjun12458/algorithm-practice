import trafilatura

def extract_article(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_tables=False
    )
    return text or ""
