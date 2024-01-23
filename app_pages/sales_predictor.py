import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from src.data_management import (
    load_property_data,
    load_pkl_file,
    load_inherited_data)
from src.evaluate import (
    regression_performance,
    regression_evaluation,
    regression_evaluation_plots)
from src.predict_sales import predict_price


def page_sales_predictor():
    st.write("#### 💰 Sales Predictor")

    # load the price predictor files
    
    version = "v1"
    sale_price_prediction = load_pkl_file(
        f"outputs/ml_pipeline/sale_price_prediction/{version}/regression_pipeline.pkl"
    )
    sale_price_vars =(
        pd.read_csv(f"outputs/ml_pipeline/sale_price_prediction/{version}/X_train.csv")
        .columns
        .to_list()
    )

    st.write("### Property Price Predictor")
    st.success(
        f"*Business Requirement 2:*\n"
        f"* 2 - The client is interested in predicting the house sale price\n"
        f"from her four inherited houses and any other house in Ames, Iowa.\n"
        f"* The client is also interested in prices of properties\n"
        f"around the Ames area."
    )
    st.info(
        f"ABOUT THE PREDICTION, WHAT FEATURES, HOW IT WORKS"
    )

    st.write("---")

    # generate the live data
    X_live = DrawInputsWidgets()

    if st.button("Predict Property Price"):
        sale_price_prediction(X_live, sale_price_vars, sale_price_prediction)

        if price_prediction == 1:
            predict_price(X_live, sale_price_vars, sale_price_prediction)

def DrawInputsWidgets():

    # load dataset
    df = load_property_data()
    percentageMin, percentageMax = 0.4, 2.0

    # we create input widgets only for 6 features	
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)

	# create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])
	
	# from here on we draw the widget based on the variable type (numerical or categorical)
	# and set initial values

    with col1:
        feature = "OverallQual"
        st_widget = st.selectbox(
			label= "Overall Quality",
			options=df[feature].sort_values(ascending=True).unique()
			)
    X_live[feature] = st_widget

    with col2:
        feature = "GrLivArea"
        st_widget = st.number_input(
			label= "Above Ground Area(sq. ft)",
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 5
			)
    X_live[feature] = st_widget

    with col3:
        feature = "GarageArea"
        st_widget = st.number_input(
			label= "Garage Area(sq. ft)",
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 5
			)
    X_live[feature] = st_widget

    with col4:
        feature = "YearBuilt"
        st_widget = st.number_input(
			label= "Year Built",
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 1
			)
    X_live[feature] = st_widget

    with col5:
        feature = "1stFlrSF"
        st_widget = st.number_input(
			label= "First Floor(sq. ft)",
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 5
			)
    X_live[feature] = st_widget

    return X_live