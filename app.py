import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor



st.title("Tashkent uylari narxini bashorat qiluvchi web-sayt")
from PIL import Image

image = Image.open('image.jpg')

st.image(image, caption='Tashkent')


# inputs
st.subheader("Kerakli barcha ma'lumotlarni to'ldiring!")
rooms=st.number_input("Uyning xonalari soni:",min_value=1)
size=st.number_input("Uyning yuzasi(m):",min_value=14.0)
level=st.number_input("Uy joylashgan qavat:",min_value=1)
max_level=st.number_input("Uy joylashgan bino qavatlari soni:",min_value=1)
option = st.selectbox(
    'Tumanni tanlang',
    ('Bektemir', 'Chilonzor', 'Mirobod','Mirzo Ulugbek','Olmzor','Sergeli','Shayhontohur','Uchtepa','Yakkasaroy','Yangihayot','Yashnobod','Yunusobod'))



# model
with open("model.pkl","rb") as file:
    model = pickle.load(file)
dict = {"rooms":rooms, "size":size, "level":level, "max_level":max_level,'Bektemir':0, 'Chilonzor':0, 'Mirobod':0,'Mirzo Ulugbek':0,'Olmzor':0,'Sergeli':0,'Shayhontohur':0,'Uchtepa':0,'Yakkasaroy':0,'Yangihayot':0,'Yashnobod':0,'Yunusobod':0}
dict[option]=1
obj = pd.Series(dict)
df = pd.DataFrame(obj).T

# prediction
if st.button('Calculate'):
    st.dataframe(df)
    prediction = model.predict(df.values)[0]
    st.success(f"Kiritgan ma'lumotlaringiz asosida sizning uyingizning taxminiy narxi: {np.round(prediction, decimals=-4)}$")

st.warning("Bu model 2019 yil va undan oldingi ma'lumotlar asosida qurilgan!", icon="⚠️")
