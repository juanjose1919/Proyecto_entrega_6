import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


data = pd.read_csv('datasets3.csv')

st.markdown(f'<<h1 style="text-align: center ;color:#2980B9 ;font-size:50px;">{"¿AGUA POTABLE?"}</h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="text-align: center; color:#D35400 ;font-size:30px;">{"Evaluar la potabilidad del agua es un factor importante de la vida humana, dado que si los seres humanos están consumiendo agua contaminada, lo más probable es desarrollar problemas de salud, vulnerando los derechos fundamentales. Por este motivo se evaluará la potabilidad del agua con las siguientes variables:"}</h1>', unsafe_allow_html=True)

pot = [['Potability','Potabilidad ','Indica si el agua es segura para el consumo humano, donde 1 significa potable y 0 significa no potable.'],['Ph','Ph','El PH es un parámetro para evaluar el equilibrio ácido-base del agua. La OMS ha recomendado un limite máximo permisible de pH de 6,5 a 8,5'],['Hardness','Dureza','La dureza está causada principalmente por las sales de calcio y magnesio. Estas sales se disuelven en los depOsitos geolOgicos por los que pasa el agua'],['Solids','Solidos','El agua tiene la capacidad de disolver una amplia gama de minerales o sales inorgánicas y algunas orgánicas como el potasio, el calcio, el sodio, los bicarbonatos, los cloruros, el magnesio, los sulfatos, etc'],['Chloramines','Cloraminas','El cloro y la cloramina son los principales desinfectantes utilizados en los sistemas públicos de agua'],['Sulfate','Sulfato','Los sulfatos son sustancias naturales que se encuentran en los minerales, el suelo y las rocas'],['Conductivity','Conductividad','El agua pura no es un buen conductor de la corriente eléctrica más bien es un buen aislante'],['Organic_carbon','Carbono orgánico','El carbono orgánico total (COT) en las aguas de origen proviene de la materia orgánica natural en descomposiciOn (NOM), asi como de fuentes sintéticas'],['Trihalomethanes','Trihalometanos','Los THM son sustancias quimicas que pueden encontrarse en el agua tratada con cloro'],['Turbidity','Turbidez','La turbidez del agua depende de la cantidad de materia sOlida presente en estado de suspensiOn']]

st.table(pot)



st.markdown(f'<h1 style="color:#117A65 ;font-size:35px;">{"Primera parte: ExploraciOn inicial de los datos"}</h1>', unsafe_allow_html=True)
st.write(' En la exploraciOn inicial se busca identificar los datos obtenidos y revisar su coherencia en disposicion al analisis.')
st.write('Como los datos obtenidos son bastabtes vamos a observar los primeros 10 datos')
st.table(data.head(10))
st.write('Aqui observamos los últimos 10 datos por el mismo motivo anteriormente nombrado')
st.table(data.tail(10))
st.write('La siguiente tabla describe de los datos como los valores minimos, valores maximos, la media de los datos respecto a su variable, al igual que la mediana, los porcentajes de los datos, etc.')
st.table(data.describe())

st.markdown(f'<h1 style="color:#117A65 ;font-size:35px;">{"Segunda parte: Limpieza de los datos"}</h1>', unsafe_allow_html=True)
st.text('En este apartado tenmos las variables que presentan datos nulos.')

lista = []
for i in data.isna().sum():
    if i > 0:
        lista.append(data.isna().sum()==i)
st.table(lista)

df = pd.read_csv('data_mahalanobis.csv')

st.write('Mediante el calculo de Mahalanobis, se predijo el valor de dichos valores nulos como varibales objetivo y las variables explicativas fueron las demás variables con valores valederos, recuerda que es la forma más utilizada de medir la distancia entre vectores')
st.table(df.isna().sum())
st.write('Como podemos observar, ahora no hay evidencia de la existencia de datos nulos, lo que permite continual con nuestro analisis')

st.markdown(f'<h1 style="color:#117A65 ;font-size:35px;">{"Tercera parte: TransformaciOn de datos"}</h1>', unsafe_allow_html=True)
st.write('La transformaciOn de datos está enfocada a la variable objetibo, puesto que es la única que presenta dos valores (bool variable), en este caso si el agua es potable o no, con valor de 1 para la respuesta afirmativa y 0 con la negativa')

st.table(data.pivot_table(index=["Potability"],
                  values=['ph','Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'],
                  aggfunc=["mean"]))

st.markdown(f'<h1 style="color:#117A65 ;font-size:35px;">{"Cuarta parte: CategorizaciOn de los datos"}</h1>', unsafe_allow_html=True)

st.table(data.pivot_table(index=["Potability"],
                  values=['ph','Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'],
                  aggfunc=["mean"]))

st.write('En la tabla pivot se muestra las medias de cada variable diferenciadas por agua potable y no potable. En primer lugar el promedio de las cloraminas es mayor en el agua potable por lo que en primer lugar se podria inferir que entre menor cantidad de cloraminas baja la pureza del agua, después se muestra que el promedio de la conductividad para agua potable es menor, por lo que se entenderia que a mayor conductividad menor pureza del agua. En este orden de ideas la dureza tendria una relaciOn de efecto negativo en la pureza del agua, la presencia de carbOn orgánico, igualmente, un efecto negativo, la presencia de sOlidos en el agua tendria un efecto positivo en su pureza, asi como el sulfato, los trihalometanos y la turbidez, por último el ph mostraria un efecto negativo, es decir se presenta un mayor ph en agua no potable.')

st.text('Ahora se dividen las variables dependientes:')

data_corte = pd.read_csv('data_corte.csv')

st.table(data_corte.pivot_table(index=["Potability"],
                columns=["ph_p1"]))

st.write('Al separar las variables por categoria se evidencia que, en realidad los dos primeros rangos de presencia de cloraminas tienen un efecto negativo en la pureza del agua, mientras los dos siguientes rangos tienen un efecto positivo. Para la conductividad se evidencia que tanto el primer como último rango tienen efectos positivos en la pureza, mientras que el los restantes un mayor promedio se relaciona a aguas no potables. En la dureza se muestra una diferencia significativa entre los promedios del primer rango y únicamente en el último rango se muestra un efecto positivo en la potabilidad. Se evidencia también que en los dos primeros rangos de presencia de carbOn orgánico tienen un efecto negativo en la pureza del agua, los dos siguientes rangos tienen un efecto positivo. Para la presencia de sOlidos en el agua se muestra que únicamente en el segundo rango una mayor presencia de sOlidos indica la no potabilidad de agua. En el caso de la presencia de sulfato se evidencia en los dos rangos mayores un efecto negativo en la potabilidad. En los trihalometanos solo el tercer rango indica un efecto positivo entre la cantidad y la potabilidad del agua, presentando el mismo caso que la turbidez. Asi, el ph evidencia un efecto positivo en los dos primeros rangos y un efecto negativo en los restantes.')

st.markdown(f'<h1 style="color:#117A65 ;font-size:35px;">{"Quinta parte: VisualizaciOn de los datos"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"DistribuciOn de las variables"}</h1>', unsafe_allow_html=True)

st.write('En este apartado se observan las relaciones graficas entre las variables respecto a la objetivo')


col1, col2 = st.columns(2)
with col1:
    st.image('./images/Potability_count.png')
    st.image('./images/Chloramines_count.png')
    st.image('./images/Organic_carbon_count')
    st.image('./images/Solids_count')
with col2:
    st.image('./images/Conductivity_count')
    st.image('./images/Hardness_count')
    st.image('./images/Sulfate_count')
    st.image('./images/Turbidity_count')
    
st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"Conclusiones intermedias"}</h1>', unsafe_allow_html=True)

st.write('Dentro de la muestra se observa que en mayor parte el agua no es potable, estando sobre 1750 datos. Además tanto el agua potable como la no potable se concentran en un ph cercano a 7 en el estudio, en niveles de dureza entre 175 y 225 (clasificando asi como agua dura), la cantidad de sOlidos disueltos predomina entre los 1000 y los 30000, mostrando asi que el agua muestra comportamientos similares en estas categorias. Por el otro lado, la cantidad de cloraminas se concentra en niveles cercanos a 7 para el agua no potable, mientras que para el agua potable se inclina a niveles cercanos a 8.')

st.write('En cuanto a la cantidad de sulfato tiene comportamientos similares para agua potable y no potable, los que se concentran mayormente en valores cercanos a 340, a diferencia de la conductividad que presenta valores mas dispersos mayormente en el rango de 330 y 500. La cantidad de carbon organico en ambos casos se concentran entre 12.5 y 15.4, en el caso de los trihalometanos existe una cantidad mas significativa en los datos cercanos a 68. Por ultimo la cantidad medida en unidades de turbiedad se dispersa en mayor medida entre 3.2 y 5.7 unidades nefelométricas de turbidez.')
    

#pot = data['Potability'].value_counts()
#pot.index = ['NO', 'SI']
#fig, ax = plt.subplots(1,1)
#ax.set_title('Proporción de potabilidad')
#ax.bar(pot.index, pot.values, color = 'orange')

#st.pyplot(fig)

