import pandas as pd
import numpy as np
import streamlit as st
import pickle

st.title("Hello Welcome to Chennai House Price Prdeiction Dataset")

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction'])

if app_mode=='Home':
    st.title('Chennai House Price Prediction :')
    st.image('Real Estate.jpg')
    st.markdown('Dataset :')
    data=pd.read_csv("ML.csv")
    st.write(data.head())
    st.image('Graph.png')

elif app_mode == 'Prediction':
    st.subheader('Sir/Madem , YOU need to fill all necessary informations in order to predict sale price of property which you want to buy ! ')
    st.sidebar.header("Informations about the property :")
    area_dict = {"Karapakkam": 0,"Adyar": 1, "Chrompet": 2, "Velachery": 3,"KK Nagar" : 4, "Anna Nagar" : 5,"T Nagar": 6}
    sale_cond = {"Partial": 0,"Family": 1,"AbNormal": 2, "Normal Sale": 3,"AdjLand" : 4}
    utility = {"ELO": 0, "NoSeWa": 1, "NoSewr" : 2, "AllPub": 3}
    street = {"No Access": 0,"Paved": 1, "Gravel": 2}
    mzzone = {"A": 0,"C": 1, "I": 2, "RH": 3, "RL": 4, "RM" : 5}
    AREA = st.sidebar.radio('Area where you want to purchase property', tuple(area_dict.keys()))
    SALE_COND = st.sidebar.radio('Sales Condition of property', tuple(sale_cond.keys()))
    UTILITY_AVAIL = st.sidebar.radio('Utility looking in property', tuple(utility.keys()))
    STREET = st.sidebar.radio('Street Condition for property', tuple(street.keys()))
    MZZONE = st.sidebar.radio('Property in MZZONE', tuple(mzzone.keys()))
    buildtype = st.sidebar.radio('BUILD_TYPE',options=[ 'Commercial','House' , 'Others'])
    sqft = st.sidebar.slider('Area of property in SQFT',2500,500)
    dist_mainroad = st.sidebar.slider('Distance from mainroad',200,0)
    age = st.sidebar.slider('Age of Building',60,1)
    bedroom = {"1": 0,"2": 1, "3": 2, "4": 3}
    bathroom = {"1": 0, "2": 1}
    room = {"2": 2,"3": 3, "4": 4, "5": 5, "6": 6}
    park = {"Yes": 0, "No": 1}
    N_BEDROOM = st.sidebar.radio('Number of bedroom in property', tuple(bedroom.keys()))
    N_BATHROOM = st.sidebar.radio('Number of bathroom in property', tuple(bathroom.keys()))
    N_ROOM = st.sidebar.radio('Number of rooms in property', tuple(room.keys()))
    PARK = st.sidebar.radio('Parking facility in property', tuple(park.keys()))

    BUILDTYPE_Commercial, BUILDTYPE_House, BUILDTYPE_Others = 0, 0, 0
    if buildtype == 'Commercial':
        BUILDTYPE_Commercial = 1
    elif buildtype == 'House':
        BUILDTYPE_House = 1
    else:
        BUILDTYPE_Others = 1


    data1={
    'AREA': AREA,
    'INT_SQFT': sqft,
    'DIST_MAINROAD': dist_mainroad,
    'N_BEDROOM': N_BEDROOM,
    'N_BATHROOM': N_BATHROOM,
    'N_ROOM': N_ROOM,
    'PARK_FACIL': PARK,
    'SALE_COND': SALE_COND,
    'BUILD':[ BUILDTYPE_Commercial, BUILDTYPE_House, BUILDTYPE_Others],
    'UTILITY_AVAIL': UTILITY_AVAIL,
    'STREET': STREET,
    'MZZone': MZZONE,
    'AGE_OF_BUILDING': age
    }

    feature_list = [get_value(AREA,area_dict), sqft, dist_mainroad, get_value(N_BEDROOM,bedroom), get_value(N_BATHROOM,bathroom), get_value(N_ROOM,room), get_value(SALE_COND,sale_cond), get_value(PARK,park), get_value(UTILITY_AVAIL,utility), get_value(STREET,street), get_value(MZZONE,mzzone), age, data1['BUILD'][0], data1['BUILD'][1], data1['BUILD'][2]]
    single_sample = np.array(feature_list).reshape(1, -1)


    if st.button("Predict"):
        loaded_model = pickle.load(open('ChennaiPrice .sav', 'rb'))
        prediction = loaded_model.predict(single_sample)
        st.text("According to your Selection the price range lie between(in rupees): ")
        buffer = 0.05* prediction
        pred_1 = prediction - buffer
        pred_2 = prediction + buffer
        pred1 = int(pred_1)
        pred2 = int(pred_2)
        st.write( pred1 , pred2)