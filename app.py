import streamlit as st
import requests

# Configuration
GOOGLE_SEARCH_API_URL = "https://www.googleapis.com/customsearch/v1"
API_KEY = ""  # Replace with your Google Custom Search API Key
SEARCH_ENGINE_ID = ""  # Replace with your Google Custom Search Engine ID

# Function to search Google and return results
def search_product_on_google(product_name):
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': product_name + " site:flipkart.com OR site:amazon.in OR site:paytmmall.com OR site:shopclues.com OR site:tatacliq.com OR site:reliancedigital.in OR site:mi.com OR site:snapdeal.com OR site:ajio.com OR site:croma.com",  # Targeting top 10 Indian e-commerce websites
        'num': 10  # Number of search results to return
    }
    
    response = requests.get(GOOGLE_SEARCH_API_URL, params=params)
    
    if response.status_code == 200:
        results = response.json()
        return results.get('items', [])
    else:
        st.error(f"Error from Google Search API: {response.status_code}")
        return []

# Function to get the best e-commerce link and site name for the product
def get_best_ecommerce_link(search_results):
    best_link = None
    best_site_name = None
    
    for result in search_results:
        link = result.get('link', '')
        title = result.get('title', '')

        # Identify the website name from the link
        if 'amazon.in' in link:
            best_link = link
            best_site_name = 'Amazon India'
            break
        elif 'flipkart.com' in link:
            best_link = link
            best_site_name = 'Flipkart'
            break
        elif 'paytmmall.com' in link:
            best_link = link
            best_site_name = 'Paytm Mall'
            break
        elif 'shopclues.com' in link:
            best_link = link
            best_site_name = 'ShopClues'
            break
        elif 'tatacliq.com' in link:
            best_link = link
            best_site_name = 'TataCliq'
            break
        elif 'reliancedigital.in' in link:
            best_link = link
            best_site_name = 'Reliance Digital'
            break
        elif 'mi.com' in link:
            best_link = link
            best_site_name = 'Xiaomi (mi.com)'
            break
        elif 'snapdeal.com' in link:
            best_link = link
            best_site_name = 'Snapdeal'
            break
        elif 'ajio.com' in link:
            best_link = link
            best_site_name = 'Ajio'
            break
        elif 'croma.com' in link:
            best_link = link
            best_site_name = 'Croma'
            break

    return best_link, best_site_name

# Streamlit UI
def main():
    st.title("🛒 Cheapest Product Finder Across Indian E-commerce Websites")
    
    # Input: User enters the product name
    product_name = st.text_input("Enter the product name:", "")
    
    if st.button("Find Best Buy Link"):
        if product_name:
            st.write(f"Searching for the best buy link for '{product_name}'...")

            # Step 1: Search product on Google using Google Custom Search API
            search_results = search_product_on_google(product_name)
            if search_results:
                # Step 2: Get the best e-commerce link and website name from the search results
                best_link, best_site_name = get_best_ecommerce_link(search_results)
                
                if best_link:
                    st.write(f"**Buy Here on {best_site_name}:** [Link]({best_link})")
                else:
                    st.warning("Could not find a suitable link for purchasing the product.")
            else:
                st.warning("No search results found.")
        else:
            st.error("Please enter a product name.")

if __name__ == "__main__":
    main()
