# PPP: Property Price Predictor

### About
[Propery Price Predictor](https://property-price-predictor-am-c6b2e55483b8.herokuapp.com/) (PPP) is a Machine Learning tool that can help users to predict the sale prices of properties by taking the properties features as inputs. Currently this tool will only predict prices on properties within *Ames, Iowa*.

The app was created to help the client:
* View how the attributes of a property correlate to the sale price.
* Have the ability to predict sale prices for specific houses, and other properties across Ames.

# Table of Contents
<ul>
<li><a href="#dataset-content">Dataset Content</a></li>
     <ul>
        <li><a href="#initial-observations">Initial Observations</a></li>
        <li><a href="#possible-limitations">Possible Limitations</a></li>
    </ul>
<li><a href="#business-requirements">Business Requirements</a></li>
<li><a href="#hypothesis-and-validation">Hypothesis and Validation</a></li>
    <ul>
        <li><a href="#hypothesis-one">Hypothesis One</a></li>
        <li><a href="#hypothesis-two">Hypothesis Two</a></li>
        <li><a href="#hypothesis-three">Hypothesis Three</a></li>
    </ul>
<li><a href="#rationale-map">Rationale Business Requirement Map</a></li>
<li><a href="#ml-business-case">ML Business Case</a></li>
    <ul>
        <li><a href="#milestones">Milestones</a></li>
        <li><a href="#user-story-and-epics">User Story and Epics</a></li>
        <li><a href="#moscow-prioritisation">MoSCoW Prioritisation</a></li>
    </ul>
<li><a href="#dashboard-design">Dashboard Design</a></li>
    <ul>
        <li><a href="#project-summary">Project Summary</a></li>
        <li><a href="#hypothesis-and-validation">Hypothesis and Validation</a></li>
        <li><a href="#property-sale-price-study">Property Sale Price Study</a></li>
        <li><a href="#predict-sales">Predict Sales</a></li>
        <li><a href="#ml-model">ML Model</a></li>
    </ul>
<li><a href="#unfixed-bugs">Unfixed Bugs</a></li>
<li><a href="#deployment">Deployment</a></li>
    <ul>
        <li><a href="#heroku">Heroku</a></li>
        <li><a href="#main-data-analysis-and-ml-libs">Main Data Analysis and Machine Learning Libraries</a></li>
    </ul>
<li><a href="#credits">Credits</a></li>
    <ul>
        <li><a href="#content">Content</a></li>
        <li><a href="#acknowledgments">Ackowledgments</a></li>
    </ul>
</ul>


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data), provided by the client. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

### Initial Observations
* There is a lot of attributes that may have a large degree of inter-correlation. The best variables will need to be determined in order to properly proceed with the dataset, and use transformers where necessary.

### Possible Limitations
* The data lacks features that represent the location of the property, e.g. close to a school, which could have an imopact on sale price.

Although a ML model can be created, it may not be adequate at predicting propery prices within *Ames* without these extra variables that can influence sale price; with these features the performance would, in theory be higher.


## Business Requirements
You have been requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.


## Hypothesis and Validation
### Hypothesis One

* It is suspected that the *size* of a property will have an impact on *sale price*, meaning that the larger a propery is overall, the more it will sell for:
    * To validate this, we will do an correlation study, as well assess the best features against sales price.
        * **This hypothesis was confirmed during the correlation study, as well as during assessing the best features**

### Hypothesis Two

* It is suspected that the higher the *quality/finish* of a property will have an impact on *sale price*, meaning that the higher quality homes will overall sell for higher:
    * To validate this, we will do an correlation study, as well assess the best features against sales price.
        * **This hypothesis was confirmed during the correlation study, as well as during assessing the best features**

### Hypothesis Three

* It is suspected that the *year* of a property will have an impact on *sale price*, meaning that the newly built properties are more likely to sell for more:
    * To validate this, we will do an correlation study, as well assess the best features against sales price.
        * **This hypothesis was confirmed during the correlation study, as well as during assessing the best features**


## Rationale Business Requirement Map
* Business Requirement 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
    * We will perform data visualisation and a correlation study to answer this.
    * The correlation study (using pearson and spearman) will help us better understand how the variables are correlated to Sale price.
    * We will also plot the main variables against Sale price to visualise the insights.

* Business Requirement 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.
    * We want to predict whether sale price will increase based on correlated or best variables.
    * For this we will build a regressor model and analyse the best variables to use.

## ML Business Case
### Predict Sales
* **What are the business requirements?**
    * The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
    * The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.

* **Is there any business requirement that can be answered with conventional data analysis?**
    * Business requirement 1 can be answered with conventional data analysis to find correlated attributes to sale prices.

* **Does the client need a dashboard or an API endpoint?**
    * The client has requested a Streamlit dashboard

* **What does the client consider as a successful project outcome?**
    * A study that shows the most relevant variables that are correlated to sale price.
    * A capability to predict the sale price of the 4 inherited properties, as well as other properties within *Ames, Iowa*.

* **Can you break down the project into Epics and User Stories?**
    * Information gathering and data collection.
    * Data visualization, cleaning, and preparation.
    * Model training, optimization and validation.
    * Dashboard planning, designing, and development.
    * Dashboard deployment and release.*

* **Ethical or Privacy concerns?**
    * No, as the client has found a public dataset.

* Does the data suggest a particular model?
    * From the PPS study, the data suggested using a regressor model where the target is sale price.

* **What are the model's inputs and intended outputs?**
    * Input: property attribute information.
    * Output: predicted sale price.

* **What are the criteria for the performance goal of the predictions?**
    * It was agreed upon with the client that an R2 score of at least 0.75 will be required on both train and test sets.

* **How will the client benefit?**
    * The client will be able to maximise the sales price for the inherited properties.
    * The client will be able to view the sales price for other properties within the area by inputting the variables.

### Milestones
8 milestones were created for this project:

* Epic 1: Information Gathering & Data Collection - *closed*
* Epic 2: Data Visualisation, Cleaning, & Preparation - *closed*
* Epic 3: Model Training, Optimisation, & Validation - *closed
* Epic 4: Dashboard Planning, Designing, & Development - *closed*
* Epic 5: Dashboard Deployment & Release - *closed*
* User Stories - *closed*
* Admin - *closed*
* Should Have & Could Have Features - *open* (this is not important for the project)

**View [Milestones](https://github.com/annacakes281/heritage-housing-issues/milestones?state=closed)**

### User Stories and Epics

* The user stories and epics have been compied into a project board to make it easier to see what needs to be done, this can be viewed here : [User Stories and Epics](https://github.com/users/annacakes281/projects/5/views/1)

### MoSCoW Prioritisation

* The project tasks have been broken down into MoSCoW Prioritisation tasks, this can be found here: [MoSCoW Prioritisation](https://github.com/users/annacakes281/projects/6/views/1)
* Should and Cold have features were not implemented at this time due to time contraints.

## Dashboard Design
The dashboard will consist of six pages:
1. Homepage:
    * Section - welcome message and what can be found 
    * Sidebar - access to other pages, avaliable on all pages

2. Project Summary:
    * Section - background information
    * Section - quick summary
    * Section - about dataset
    * Widget checkbox - to view the dataset table, the column sizes can be changed
    * Link to README
    * Section - business Requirements

3. Hypothesis and Validation
    * Section - the hypothesis and validation

4. Propery Sale Price Study:
    * Section - sale price study and business requirement 1
    * Widget checkbox - view dataset
    * Section - correlation study variables and findings
    * Widget checkbox - graphs from correlation study

5. Sales Predictor:
    * Section - business requirement 2
    * Section - inherited property price
    * Widget checkbox - inherited properties
    * Widget checkbox - inherited property predicted prices
    * Section - predict property price
    * Widgets - allows users to input selected variables to predict price and output

6. ML Model:
    * Section - about the regressor model and R2 score
    * Section - pipeline steps
    * Section - best features and importance
    * Section - model evaluation


## Unfixed Bugs
* One unfixed bug is the *streamlit* warning regarding <code>st.cache is deprecated. Please use one of Streamlit's new caching commands, st.cache_data or st.cache_resource.</code> despite the commands being used, the warning does not disappear.
* Another bug noticed after deployment and not fixed due to time constraints and a struggle with getting project deployed with under 500mb slug is that any *years* show up with a comma.


## Deployment
### Heroku

* The App live link is: [Property Price Predictor](https://property-price-predictor-am-c6b2e55483b8.herokuapp.com/)
* Ensure: Procfile says <code>web: sh setup.sh && streamlit run app.py</code>
* Runtime: python-3.8.17

* The project was deployed to Heroku using the following steps:

1. Log in to Heroku with the CLI
2. Create the app with <code> heroku create --region eu</code>
3. set: <code>heroku stack:set heroku-20</code>
4. Using the Heroku website, go to the deploy tab and connect the repo
5. Deploy from main branch, it will build the app, if all if successful click the button to Open App.


## Main Data Analysis and Machine Learning Libraries
Below are the libraries that I used for the project, taken from *requirements.txt*

* numpy==1.23.5
* pandas==1.5.3
* matplotlib==3.7.2
* seaborn==0.12.2
* ydata-profiling==4.5.1
* plotly== 5.11.0
* ppscore==1.3.0

* feature-engine==1.6.1
* imbalanced-learn==0.10.0
* scikit-learn==1.3.0
* xgboost==1.7.6
* Jinja2==3.1.2
* MarkupSafe==2.1.3

* ipywidgets==8.0.6
* altair==5.0.1

To create the dashboard:
* protobuf==4.24.1
* streamlit==1.25.0

## Credits 

### Content 

- The projects steps were dependant on following the Code Institue [Churnometer](https://github.com/Code-Institute-Solutions/churnometer) practice project
- I relied on the following Code Institue lessons for code as well:
    * [Feature Engineering: Handle Missing Data](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/1f851533cd6a4dcd8a280fd9f37ef4e2/bb0bf41fb8744b46813c0f52a74b9b11/)
    * [Feature Engineering: Categorical Encoding](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/1f851533cd6a4dcd8a280fd9f37ef4e2/bb0bf41fb8744b46813c0f52a74b9b11/)
    * [Feature Engineering: Numerical Transformation](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/1f851533cd6a4dcd8a280fd9f37ef4e2/bb0bf41fb8744b46813c0f52a74b9b11/)
    * [Feature Engineering: Variable Discritisation](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/1f851533cd6a4dcd8a280fd9f37ef4e2/bb0bf41fb8744b46813c0f52a74b9b11/)
    * [Feature Engineering: Handle Outlier](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/1f851533cd6a4dcd8a280fd9f37ef4e2/bb0bf41fb8744b46813c0f52a74b9b11/)
    * [Feature Engineering: Drop Features](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/1f851533cd6a4dcd8a280fd9f37ef4e2/bb0bf41fb8744b46813c0f52a74b9b11/)
    * [SciKit-Learn: Cross Validation](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/1f851533cd6a4dcd8a280fd9f37ef4e2/f3d518ff775b4545adac7642fa290993/)

- I also turned to some previous students work when I was stuck on how to proceed:
    * [Knutinator](https://github.com/knutinator/heritage-housing/tree/main)
    * [URiem](https://github.com/URiem/heritage-housing-PP5/tree/main)

- To help analyse the histograms and q-q plots I used the following:
    * [Q-Q Plots](https://www.ucd.ie/ecomodel/Resources/QQplots_WebVersion.html#:~:text=You%20can%20start%20to%20understand,on%20the%20QQ%2Dplot)
    * [Histogram](https://www.labxchange.org/library/items/lb:LabXchange:10d3270e:html:1#:~:text=A%20histogram%20shows%20how%20frequently,to%20be%20discrete%20positive%20integers.)

- To create the Streamlit app I used the following video tutorial:
    * Coding is fun [How to create a Streamlit Multi-page Web App](https://www.youtube.com/watch?v=YClmpnpszq8)

- [App Icons](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/) were found from the streamlit page.

- To create the dataset table I used the following website:
    * [st.data_editor](https://docs.streamlit.io/library/api-reference/data/st.data_editor)

## Acknowledgements
* I would like to thank my mentor, Precious, for his support for when I decided to change my idea due to the data not being sufficent enough and for answering all my questions when needed.
* I would also like to thank the slack community for answering questions.
