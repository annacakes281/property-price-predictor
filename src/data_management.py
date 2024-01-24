import streamlit as st
import pandas as pd
import numpy as np
import joblib

# this file is based on code found in the CI walkthrough projects


def load_property_data():
    # we want the cleaned data without the NAN values
    df = pd.read_csv("outputs/datasets/cleaned/HousePriceRecordsCleaned.csv")
    return df


def load_inherited_data():
    df = pd.read_csv("outputs/datasets/collection/InheritedHouses.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)