
import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Lataa .env-tiedoston muuttujat
load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError(
        "TAVILY_API_KEY puuttuu .env-tiedostosta!"
    )

client = TavilyClient(api_key=api_key)


def search_sources(topic: str, max_results: int = 5):
    """Hakee aiheeseen liittyviä verkkolähteitä."""

    response = client.search(
        query=f"{topic} scientific research",
        search_depth="basic",
        max_results=max_results,
        topic="general",
    )

    sources = []

    for index, result in enumerate(
        response.get("results", []), start=1
    ):
        sources.append({
            "id": f"S{index}",
            "title": result.get("title", ""),
            "url": result.get("url", ""),
            "content": result.get("content", ""),
        })

    return sources


if __name__ == "__main__":
    topic = input("Enter your research topic: ").strip()

    if not topic:
        print("Please enter a topic.")
    else:
        try:
            sources = search_sources(topic)

            if not sources:
                print("No sources found.")
            else:
                for source in sources:
                    print("\n" + "=" * 60)
                    print(f"ID: {source['id']}")
                    print(f"Title: {source['title']}")
                    print(f"URL: {source['url']}")
                    print(f"Content: {source['content'][:400]}")

        except Exception as error:
            print(f"Search failed: {error}")
