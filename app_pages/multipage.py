import streamlit as st

class MultiPage:  # Class to generate multiple Streamlit pages
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title="Property Price Predictor",
            page_icon="🏘️"
        )

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio(
            'Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()
        
        st.sidebar.write("Select page above to view")