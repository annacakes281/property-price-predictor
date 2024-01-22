# PPP: Property Price Predictor

### About
Propery Price Predictor (PPP) is a Machine Learning tool that can help users to predict the sale prices of properties by taking the properties features as inputs. Currently this tool will only predict prices on properties within *Ames, Iowa*.

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
<li><a href="#dashboard-design">Dashboard Design</a></li>
    <ul>
        <li><a href="#project-summary">Project Summary</a></li>
        <li><a href="#"></a></li>
        <li><a href="#"></a></li>
        <li><a href="#"></a></li>
        <li><a href="#"></a></li>
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
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

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


## Dashboard Design
The dashboard will consist of five pages:
1. Project Summary:
    * 


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.

