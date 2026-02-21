import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Web Scraper Tool", page_icon="🌐")

st.title("🌐 Simple Web Scraper")
st.write("Enter a URL below to extract titles, paragraphs, and links.")

# Input URL
url = st.text_input("Enter URL (include https://)", placeholder="https://example.com")

if st.button("Scrape Page"):
    if url:
        try:
            with st.spinner("Fetching data..."):
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract Data
                title = soup.find('title').get_text() if soup.find('title') else 'No title found'
                paragraphs = [p.get_text() for p in soup.find_all('p')]
                links = [a['href'] for a in soup.find_all('a', href=True)]

                # Display Results in Tabs
                st.success(f"Successfully scraped: {title}")
                
                tab1, tab2, tab3 = st.tabs(["📝 Paragraphs", "🔗 Links", "📄 Raw HTML"])
                
                with tab1:
                    st.header("Paragraphs Found")
                    if paragraphs:
                        for i, para in enumerate(paragraphs, 1):
                            st.write(f"**{i}.** {para}")
                    else:
                        st.info("No paragraphs found.")

                with tab2:
                    st.header("Links Found")
                    if links:
                        for i, link in enumerate(links, 1):
                            st.write(f"{i}. {link}")
                    else:
                        st.info("No links found.")
                        
                with tab3:
                    st.header("Source Code")
                    st.code(response.text[:5000], language='html') # Show first 5k chars

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL.")