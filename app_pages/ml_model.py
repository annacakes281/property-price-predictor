import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import (
    load_property_data,
    load_pkl_file)
from src.evaluate import (
    regression_performance,
    regression_evaluation)

def page_ml_model():
    
    st.write("#### 🤖 ML Model")

    #load files
    version = "v1"
    pipeline = load_pkl_file(
        f"outputs/ml_pipeline/sale_price_prediction/{version}/regression_pipeline.pkl"
    )
    feature_importance = plt.imread(
        f"outputs/ml_pipeline/sale_price_prediction/{version}/feature_importance.png"
    )
    X_train = pd.read_csv(f"outputs/ml_pipeline/sale_price_prediction/{version}/X_train.csv")
    x_test = pd.read_csv(f"outputs/ml_pipeline/sale_price_prediction/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/sale_price_prediction/{version}/y_train.csv"
    )
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/sale_price_prediction/{version}/y_test.csv"
    )

    st.info(
        f"#### ML Pipeline Requirements:\n"
        f"* It was agreed upon with the client that an *R2* score\n"
        f"of at least 0.75 was to be achieved on both the train\n"
        f"and test set.\n"
        f"* The pipeline achieved an *R2* score of: 1.0 on\n"
        f"the train set.\n"
        f"* The pipeline achieved an *R2* scor of: 0.86 on\n"
        "the train set.\n\n"
        f"**The *R2* target has been reached.**"
    )
    # show pipeline steps, had to write manually as it would not load otherwise
    st.write("---")
    st.write("#### ML Pipeline Steps:")
    # st.write(pipeline)
    st.success(
        f"Pipeline(steps=[('NumericLogTransform',\n"
        f"LogTransformer(variables=['1stFlrSF', 'GrLivArea'])),\n"
        f"('WinsorizerIQR', Winsorizer(capping_method='iqr',\n"
        f"fold=1.5, tail='both', variables=['1stFlrSF', 'GrLivArea',\n"
        f"'GarageArea'])), ('feat_scaling', StandardScaler()),\n"
        f"('model', ExtraTreesRegressor(random_state=0))])"
    )
    st.write("---")

    # show best features
    st.write("#### Best Features:")
    st.write(X_train.columns.to_list())
    st.image(feature_importance)
    st.write("---")

    # evaluate performance on train and test sets
    regression_performance(X_train=X_train, y_train=y_train,
                           x_test=x_test, y_test=y_test, pipeline=pipeline)

    st.write("---")
