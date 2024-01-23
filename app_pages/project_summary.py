import streamlit as st
import pandas as pd

def page_project_summary():
    
    st.write("#### 📝 Project Summary")

    # background information taken from readme
    st.info(
        f"**Background information:**\n\n"
        f"As a good friend, you are requested by your friend, who has received\n"
        f"an inheritance from a deceased great-grandfather located in\n"
        f"Ames,Iowa, to help in maximising the sales price for\n"
        f"the inherited properties.\n\n"
        f"Although your friend has an excellent understanding of property prices\n"
        f"in her own state and residential area, she fears that basing her\n"
        f"estimates for property worth on her current knowledge might lead to\n"
        f"inaccurate appraisals.\n"
        f"What makes a house desirable and valuable where she comes from might\n"
        f"not be the same in Ames, Iowa.\n"
        f"She found a public dataset with house prices for Ames, Iowa,\n"
        f"and will provide you with that.\n\n"
        f"**Quick Summary**:\n\n"
        f"*This is a sales prediction app that will predict property prices in\n"
        f"Ames, Iowa, based on certain features, as well as predict the\n"
        f"inherited house prices.*\n\n"
        f"**About the Dataset:**\n\n"
        f"The dataset has almost 1.5 thousand rows and represents housing\n"
        f"records from Ames, Iowa, indicating house profile (Floor Area,\n"
        f"Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built)\n"
        f"and its respective sale price for houses built\n"
        f"between 1872 and 2010.\n\n"
        f"Press the button below to view the dataset content or to\n"
        f"view the dataset:\n"
        f"[Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)")

    # checkbox to view dataset
    if st.checkbox("View Dataset"):
        df = pd.DataFrame(
        [
        {"Variable": "1stFlrSF", 
        "Meaning": "First Floor square feet", 
        "Units": "334-4692"},
        
        {"Variable": "2ndFlrSF", 
        "Meaning": "Second-Floor square feet", 
        "Units": "0-2065"},

        {"Variable": "BedroomAbvGr", 
        "Meaning": "Bedrooms above grade (does NOT include basement bedrooms)", 
        "Units": "0-8"},

        {"Variable": "BsmtExplosure", 
        "Meaning": "Refers to walkout or garden level walls", 
        "Units": "Gd; Av; Mn; No; None"},

        {"Variable": "BasmtFinType1", 
        "Meaning": "Rating of basement finished area", 
        "Units": "GLQ; ALQ; BLQ; Rec; LwQ; Unf"},

        {"Variable": "BsmFinSF1", 
        "Meaning": "Type 1 finished sqaure feet", 
        "Units": "0-5644"},

        {"Variable": "BsmtFinSF", 
        "Meaning": "Unfinished square feet of basement area", 
        "Units": "0-2336"},

        {"Variable": "TotalBsmtSF", 
        "Meaning": "UTotal square feet of basement area", 
        "Units": "0-6110"},

        {"Variable": "GarageArea", 
        "Meaning": "Size of garage in sqaure feet", 
        "Units": "0-1418"},

        {"Variable": "GarageFinish", 
        "Meaning": "Interior finish of the garage", 
        "Units": "Fin; RFn; Unf; None"},

        {"Variable": "GarageYrBlt", 
        "Meaning": "Year garage was built", 
        "Units": "1900-2010"},

        {"Variable": "GrLivArea", 
        "Meaning": "Above grade (ground) living area squre feet", 
        "Units": "334-5642"},

        {"Variable": "KitchenQual", 
        "Meaning": "Kitchen quality", 
        "Units": "Ex; Gd; TA; Fa; Po"},

        {"Variable": "LotArea", 
        "Meaning": "Lot size in square feet", 
        "Units": "1300-215245"},

        {"Variable": "LotFrontage", 
        "Meaning": "Linear feet of street connected to property", 
        "Units": "21-313"},

        {"Variable": "MasVnrArea", 
        "Meaning": "Masonry veneer area in sqaure feet", 
        "Units": "0-1600"},

        {"Variable": "EnclosedPorch", 
        "Meaning": "Enclosed porch area in square feet", 
        "Units": "0-286"},

        {"Variable": "OpenPorchSF", 
        "Meaning": "Open porch area in sqaure feet", 
        "Units": "0-547"},

        {"Variable": "OverallCond", 
        "Meaning": "Rates the overall condition of the house", 
        "Units": "10-1"},

        {"Variable": "OverQual", 
        "Meaning": "Rates the overall material and finish of the house", 
        "Units": "10-1"},

        {"Variable": "WoodDeckSF", 
        "Meaning": "Wood deck in sqaure feet", 
        "Units": "0-736"},

        {"Variable": "YearBuilt", 
        "Meaning": "Original construction date", 
        "Units": "1872-2010"},

        {"Variable": "YearRemodAdd", 
        "Meaning": "Remodal date (same as construction date if no remodelling or additions)", 
        "Units": "1950-2010"},

        {"Variable": "SalePrice", 
        "Meaning": "Sale Price", 
        "Units": "34900-755000"},
    ])

        # this hides the indes and allows the table column width to be expanded and decreased
        df = st.data_editor(df, hide_index=True, use_container_width=True)

    # link to readme
    st.write(
        f"For any additional information, please visit and\n"
        f"**read**:\n"
        f"[Project README](https://github.com/annacakes281/heritage-housing-issues/tree/main?tab=readme-ov-file)"
    )

    # business requirements taken from readme
    st.success(
        f"The project contains 2 **Business Requirements**:\n"
        f"* 1 - The client is interested in discovering how the house attributes\n"
        f"correlate with the sale price.\n"
        f"Therefore, the client expects data visualisations of\n"
        f"the correlated variables against the sale price to show that.\n\n"
        f"* 2 - The client is interested in predicting the house sale price\n"
        f"from her four inherited houses and any other house in Ames, Iowa."
    )
