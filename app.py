import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.homepage import page_homepage
from app_pages.project_summary import page_project_summary
from app_pages.hypothesis_and_validation import page_hypothesis_and_validation
from app_pages.property_sale_price_study import page_sale_price_study
from app_pages.sales_predictor import page_sales_predictor
from app_pages.ml_model import page_ml_model

app = MultiPage(app_name="🏘️ Property Price Predictor")

# Add app pages here using .add_page()

app.add_page("🏘️ Homepage", page_homepage)
app.add_page("📝 Project Summary", page_project_summary)
app.add_page("👓 Hypothesis & Validation", page_hypothesis_and_validation)
app.add_page("🏡 Propery Sale Price Study", page_sale_price_study)
app.add_page("💰 Sales Predictor", page_sales_predictor)
app.add_page("🤖 ML Model", page_ml_model)

app.run()  # Run the app
