import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.response = self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def get_business_name(self):
        if self.response:
            soup = BeautifulSoup(self.response.text, 'html.parser')
            title_tag = soup.find("title")
            return title_tag.text if title_tag else "Business name not found"
        else:
            return "Data not available"

    # Gets all the phone numbers on the webpage
    def get_phone_number(self):
        if self.response:
            soup = BeautifulSoup(self.response.text, 'html.parser')
            phone_span = soup.find("span", class_="phone")
            return phone_span.text if phone_span else "Phone number not found"
        else:
            return "Data not available"

    # Gets all the featured testimonials
    def get_featured_testimonials(self):
        if self.response:
            soup = BeautifulSoup(self.response.text, 'html.parser')
            featured_testimonials = soup.find_all("div", class_="quote")
            return [testimonial.text for testimonial in featured_testimonials]
        else:
            return []
    
    # Gets all the links from the Webpage
    def get_staff_members(self):
        if self.response:
            soup = BeautifulSoup(self.response.text, 'html.parser')
            staff_elements = soup.find_all("div", class_="info")
            return [staff.text for staff in staff_elements]
        else:
            return []

    # Gets all the links from the Webpage
    def get_all_links(self):
        if self.response:
            soup = BeautifulSoup(self.response.text, 'html.parser')
            links = soup.find_all('a')
            return [(link.text, link.get('href')) for link in links]
        else:
            return []
    
    # Gets all the articles on the Webpage
    def get_all_articles(self):
        if self.response:
            soup = BeautifulSoup(self.response.text, 'html.parser')
            articles = soup.find_all('article')
            return [article.text for article in articles] if articles else ["No articles were found"]
        else:
            return ["Data not available"]

if __name__ == "__main__":
    scraper = WebScraper('http://www.wisdompetmed.com/')
    
    print("Business Name:", scraper.get_business_name())
    print("Phone Number:", scraper.get_phone_number())
    print("Featured Testimonials:", scraper.get_featured_testimonials())
    print("Staff Members:", scraper.get_staff_members())
    
    # Prints all the links
    print("\nAll Links:")
    for text, href in scraper.get_all_links():
        print(text, href)
    
    # Prints the featured articles
    print("\nAll Featured Articles:")
    for article in scraper.get_all_articles():
        print(article)
    
    # Write HTML code to a text file
    with open('scraped_html.txt', 'w', encoding="utf8") as f:
        f.write(scraper.response.text)