import requests
import xml.etree.ElementTree as ET

def fetch_rss_feed(url):
    """Fetch the RSS feed from the given URL."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Error fetching RSS feed: {e}")
        return None

def parse_rss_feed(xml_data):
    """Parse the RSS feed and display title, description, and link."""
    try:
        root = ET.fromstring(xml_data)
        channel = root.find('channel')

        if channel is None:
            print("Invalid RSS feed format.")
            return

        items = channel.findall('item')

        if not items:
            print("No items found in the RSS feed.")
            return

        print("\n📰 RSS Feed Items:\n" + "="*60)
        for item in items:
            title = item.findtext('title', default="No Title")
            description = item.findtext('description', default="No Description")
            link = item.findtext('link', default="No Link")

            print(f"\n🔵 Title: {title}")
            print(f"📄 Description: {description}")
            print(f"🔗 Link: {link}")
            print("-" * 60)

    except Exception as e:
        print(f"Error parsing RSS feed: {e}")

def main():
    url = input("Enter the RSS feed URL: ").strip()
    xml_data = fetch_rss_feed(url)
    if xml_data:
        parse_rss_feed(xml_data)

if __name__ == "__main__":
    main()
