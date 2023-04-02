# Mengimpor library
import streamlit as st
import pandas as pd
import pickle

# Judul utama
st.write("<h1 style='text-align: center; '>Coal Calorie Value</h1>", unsafe_allow_html=True)


# Baris 1
st.write(f"<h2 style='text-align: left; '>Product Type & Surveyor</h2>", unsafe_allow_html=True)

with st.container():
    col1, col2, = st.columns(2)
    with col1:
            product_type = st.selectbox('Tipe Produk',['E4700','E4900','E5000','WB'])

    with col2:
            surveyor = st.selectbox('Surveyor',['GS', 'SC'])

# Baris 2
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            ton_stockpile = st.number_input('Ton(Stockpile)', value=1000)
    with col2:
            ton_krom = st.number_input('Ton(Krom)', value=500)
    with col3:
            ws_ton = st.number_input('WS TON', value=50)
    with col4:
            ch_liter = st.number_input('CH LITER', value=200)

# Baris 3
st.write(f"<h2 style='text-align: left; '>TPS</h2>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            tpshicv = st.number_input('TPSHICV', value=300)
    with col2:
            tps100 = st.number_input('TPS100', value=100)
    with col3:
            tps200 = st.number_input('TPS200', value=150)
    with col4:
            tpshica = st.number_input('TPSHICA', value=1700)

# Baris 4
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            tps300 = st.number_input('TPS300', value=1200)
    with col2:
            tps400 = st.number_input('TPS400', value=300)
    with col3:
            tpsa = st.number_input('TPSA', value=700)
    with col4:
            tps500 = st.number_input('TPS500', value=500)

# Baris 5
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            tps600 = st.number_input('TPS600', value=150)
    with col2:
            tpslocv = st.number_input('TPSLOCV', value=300)
    with col3:
            tpslocts = st.number_input('TPSLOCTS', value=250)
    with col4:
            tpsloca = st.number_input('TPSLOCA', value=200)

# Baris 6
st.write(f"<h2 style='text-align: left; '>PB</h2>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            pbhicv = st.number_input('PBHICV', value=800)
    with col2:
            pb600 = st.number_input('PB600', value=600)
    with col3:
            pb700 = st.number_input('PB700', value=400)
    with col4:
            pba = st.number_input('PBA', value=400)

# Baris 7
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            pbts = st.number_input('PBTS', value=1000)
    with col2:
            pblocts = st.number_input('PBLOCTS', value=500)
    with col3:
            pbloca = st.number_input('PBLOCA', value=150)

# Baris 8
st.write(f"<h2 style='text-align: left; '>TS</h2>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            tsc12 = st.number_input('TSC12', value=300)
    with col2:
            tsc13 = st.number_input('TSC13', value=1200)
    with col3:
            tsc33 = st.number_input('TSC33', value=500)
    with col4:
            tsc22 = st.number_input('TSC22', value=1900)

# Baris 9
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            tsc23 = st.number_input('TSC23', value=1800)
    with col2:
            tsclocv = st.number_input('TSCLOCV', value=500)
    with col3:
            tsca = st.number_input('TSCA', value=800)

# Baris 10
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            tsn100 = st.number_input('TSN100', value=800)
    with col2:
            tsn200 = st.number_input('TSN200', value=900)
    with col3:
            tsn300 = st.number_input('TSN300', value=200)
    with col4:
            tsnlocv = st.number_input('TSNLOCV', value=100)

# Baris 11
st.write(f"<h2 style='text-align: left; '>WS</h2>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            wshicv = st.number_input('WSHICV', value=1500)
    with col2:
            ws100 = st.number_input('WS100', value=1200)
    with col3:
            ws200 = st.number_input('WS200', value=100)
    with col4:
            ws300 = st.number_input('WS300', value=1000)

# Baris 12
st.write(f"<h2 style='text-align: left; '>BC</h2>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            bcslsa = st.number_input('BCSLSA', value=400)
    with col2:
            bcnlsa = st.number_input('BCNLSA', value=1500)
    with col3:
            bcscm = st.number_input('BCSCM', value=1800)
    with col4:
            bcnscm = st.number_input('BCNSCM', value=4000)

# Baris 13
st.write(f"<h2 style='text-align: left; '>Rainfall & Rainhour</h2>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            rainfall53 = st.number_input('RAINFALL53', value=3.15)
    with col2:
            rainhour54 = st.number_input('RAINHOUR54', value=2.75)
    with col3:
            rainfall55 = st.number_input('RAINFALL55', value=0.25)
    with col4:
            rainhour56 = st.number_input('RAINHOUR56', value=0.55)

# Baris 14
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            rainfall59 = st.number_input('RAINFALL59', value=20.5)
    with col2:
            rainhour60 = st.number_input('RAINHOUR60', value=0.65)
    with col3:
            rainfall61 = st.number_input('RAINFALL61', value=9.5)
    with col4:
            rainhour62 = st.number_input('RAINHOUR62', value=2.85)

# Baris 15
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
            rainfall63 = st.number_input('RAINFALL63', value=0.5)
    with col2:
            rainhour64 = st.number_input('RAINHOUR64', value=3.75)


# inference
data = {
 'PRODUCT':product_type,
 'TON\nSTOCKPILE':ton_stockpile,
 'TON\nKROM':ton_krom,
 'TPSHICV':tpshicv,
 'TPS100':tps100,
 'TPS200':tps200,
 'TPSHICA':tpshica,
 'TPS300':tps300,
 'TPS400':tps400,
 'TPSA':tpsa,
 'TPS500':tps500,
 'TPS600':tps600,
 'TPSLOCV':tpslocv,
 'TPSLOCTS':tpslocts,
 'TPSLOCA':tpsloca,
 'PBHICV':pbhicv,
 'PB600':pb600,
 'PB700':pb700,
 'PBA':pba,
 'PBTS':pbts,
 'PBLOCTS':pblocts,
 'PBLOCA':pbloca,
 'TSC12':tsc12,
 'TSC13':tsc13,
 'TSC33':tsc33,
 'TSC22':tsc22,
 'TSC23':tsc23,
 'TSCLOCV':tsclocv,
 'TSCA':tsca,
 'TSN100':tsn100,
 'TSN200':tsn200,
 'TSN300':tsn300,
 'TSNLOCV':tsnlocv,
 'WSHICV':wshicv,
 'WS100':ws100,
 'WS200':ws200,
 'WS300':ws300,
 'BCSLSA':bcslsa,
 'BCNLSA':bcnlsa,
 'BCSCM':bcscm,
 'BCNSCM':bcnscm,
 'RAINFALL53':rainfall53,
 'RAINHOUR54':rainhour54,
 'RAINFALL55':rainfall55,
 'RAINHOUR56':rainhour56,
 'RAINFALL59':rainfall59,
 'RAINHOUR60':rainhour60,
 'RAINFALL61':rainfall61,
 'RAINHOUR62':rainhour62,
 'RAINFALL63':rainfall63,
 'RAINHOUR64':rainhour64,
 'SURVEYOR':surveyor,
 ' WS_TON ':ws_ton,
 ' CH_LITER ':ch_liter
 }

columns = list(data.keys())
df = pd.DataFrame([data.values()],columns=columns)

# load model
with open('model_regresi_coal.pkl', 'rb') as f:
    model = pickle.load(f)

# Predict
res = model.predict(df)
formatted_string = "{:.2f}".format(res[0])

st.write(f"<h1 style='text-align: center; '>Calorie Value</h1>", unsafe_allow_html=True)
st.write(f"<h1 style='text-align: center; '>{formatted_string}</h1>", unsafe_allow_html=True)
