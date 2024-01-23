import streamlit as st

st.write("## Hypothesis and Validation")

st.success(
    f"**Hypothesis One:**\n\n"
    f"* It is suspected that the *size* of a property will have an impact on\n"
    f"*sale price*, meaning that the larger a propery is overall,\n"
    f"the more it will sell for:\n"
    f"  * To validate this, we will do an correlation study,\n"
    f"as well assess the best features against sales price.\n\n"
    f"**Hypothesis Two:**\n\n"
    f"* It is suspected that the higher the quality/finish of a property\n"
    f"will have an impact on sale price, meaning that the\n"
    f"higher quality homes will overall sell for higher:\n"
    f"  * To validate this, we will do an correlation study,\n"
    f"as well assess the best features against sales price.\n\n"
    f"**Hypothesis Three:**\n\n"
    f"* It is suspected that the year of a property will have an impact on\n"
    f"sale price, meaning that the newly built properties are\n"
    f"more likely to sell for more:\n"
    f"  * To validate this, we will do an correlation study,\n"
    f"as well assess the best features against sales price.\n\n"
    f"**Conclusions:**\n\n"
    f"From the correlation studies and assessing to find the\n"
    f"best features, it was confirmed that *size, quality,*\n"
    f"and *year* all have a positive impact on sale price."
)

st.sidebar.write("Select page above to view")