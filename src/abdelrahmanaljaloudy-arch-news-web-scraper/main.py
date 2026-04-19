import urllib.request
import urllib.error
from html.parser import HTMLParser
import json
from datetime import datetime

class NewsParser(HTMLParser):
    """Simple HTML parser to extract news headlines."""
    
    def __init__(self):
        super().__init__()
        self.headlines = []
        self.in_title = False
        self.current_data = ""
    
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
            
    def handle_endtag(self, tag):
        if tag == 'title' and self.in_title:
            title = self.current_data.strip()
            if title and len(title) > 10:
                self.headlines.append(title)
            self.in_title = False
            self.current_data = ""
    
    def handle_data(self, data):
        if self.in_title:
            self.current_data += data


def fetch_news(url, source_name):
    """Fetch news headlines from a given RSS feed URL."""
    headlines = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(request, timeout=10) as response:
            content = response.read().decode('utf-8', errors='ignore')
        
        # Extract titles from RSS/XML
        titles = []
        start = 0
        while True:
            tag_start = content.find('<title>', start)
            if tag_start == -1:
                break
            tag_end = content.find('</title>', tag_start)
            if tag_end == -1:
                break
            title = content[tag_start + 7:tag_end].strip()
            # Clean CDATA
            title = title.replace('<![CDATA[', '').replace(']]>', '')
            if len(title) > 15:
                titles.append(title)
            start = tag_end + 8
        
        # Skip first title (usually site name)
        for title in titles[1:]:
            headlines.append({
                "source": source_name,
                "headline": title,
                "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
                
    except urllib.error.URLError as e:
        print(f"❌ Could not fetch from {source_name}: {e}")
    except Exception as e:
        print(f"❌ Error processing {source_name}: {e}")
    
    return headlines


def display_headlines(headlines, limit=10):
    """Display headlines in a formatted way."""
    if not headlines:
        print("No headlines found.")
        return
    
    print(f"\n{'='*60}")
    print(f"  📰 Latest News Headlines")
    print(f"{'='*60}")
    
    displayed = headlines[:limit]
    for i, item in enumerate(displayed, 1):
        print(f"\n{i}. [{item['source']}]")
        print(f"   {item['headline']}")
    
    print(f"\n{'='*60}")
    print(f"  Scraped at: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Total headlines fetched: {len(headlines)}")


def save_to_file(headlines, filename="news_headlines.json"):
    """Save headlines to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(headlines, f, indent=4, ensure_ascii=False)
    print(f"\n✅ Headlines saved to {filename}")


def main():
    # Free RSS feed sources
    sources = [
        {
            "name": "BBC News",
            "url": "http://feeds.bbci.co.uk/news/rss.xml"
        },
        {
            "name": "Reuters",
            "url": "https://feeds.reuters.com/reuters/topNews"
        },
        {
            "name": "Al Jazeera",
            "url": "https://www.aljazeera.com/xml/rss/all.xml"
        }
    ]

    print("=" * 60)
    print("       🌐 News Headlines Scraper")
    print("=" * 60)

    while True:
        print("\nOptions:")
        print("  1. Fetch Latest Headlines")
        print("  2. Fetch & Save to JSON File")
        print("  3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == '1':
            all_headlines = []
            print("\n⏳ Fetching headlines, please wait...")
            for source in sources:
                print(f"   Scraping {source['name']}...")
                headlines = fetch_news(source['url'], source['name'])
                all_headlines.extend(headlines)
            display_headlines(all_headlines)

        elif choice == '2':
            all_headlines = []
            print("\n⏳ Fetching headlines, please wait...")
            for source in sources:
                print(f"   Scraping {source['name']}...")
                headlines = fetch_news(source['url'], source['name'])
                all_headlines.extend(headlines)
            display_headlines(all_headlines)
            save_to_file(all_headlines)

        elif choice == '3':
            print("\nGoodbye! 👋")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()