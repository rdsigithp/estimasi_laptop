import pickle
import streamlit as st

model = pickle.load(open('estimasi_laptop.sav', 'rb'))

st.title('Estimasi Harga Laptop')

#graphic_card_gb','warranty','old_price','discount','star_rating'
graphic_card_gb = st.number_input('Input VGA')
warranty = st.number_input('Input Garansi')
old_price = st.number_input('Input Harga Lama')
discount = st.number_input('Input Discount')
star_rating = st.number_input('Input Rating Bintang')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[graphic_card_gb,warranty,old_price,discount,star_rating]]
    )
    st.write ('Estimasi harga Laptop  dalam Rupee INR : ', predict)
    st.write ('Estimasi harga Laptop bekas dalam Rupiah IDR :', predict*180.95)