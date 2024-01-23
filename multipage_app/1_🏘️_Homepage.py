import streamlit as st

st.set_page_config(
            page_title="Property Price Predictor",
            page_icon="🏘️"
        )

st.title("Homepage")

st.info(
    f"Welcome to the Property Price Predictor!\n"
    f"\nThe purpose of this app is to Predict Property Prices (currently only\n"
    f"avaliable in the Ames area).\n\n"
    f"The following pages can be found here:\n\n"
    f"* Project Summary\n\n"
    f"* Hypothesis and Validation\n\n"
    f"* Propery Sale Price Study\n\n"
    f"* Sales Predictor\n\n"
    f"* ML Model\n\n"
    f"Use the sidebar to navivate to the different pages.")

st.sidebar.write("Select page above to view")