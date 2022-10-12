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
    st.image('./images/Organic_carbon_count.png')
    st.image('./images/Solids_count.png')
with col2:
    st.image('./images/Conductivity_count.png')
    st.image('./images/Hardness_count.png')
    st.image('./images/Sulfate_count.png')
    st.image('./images/Turbidity_count.png')
    
st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"Conclusiones intermedias"}</h1>', unsafe_allow_html=True)

st.write('Dentro de la muestra se observa que en mayor parte el agua no es potable, estando sobre 1750 datos. Además tanto el agua potable como la no potable se concentran en un ph cercano a 7 en el estudio, en niveles de dureza entre 175 y 225 (clasificando asi como agua dura), la cantidad de sOlidos disueltos predomina entre los 1000 y los 30000, mostrando asi que el agua muestra comportamientos similares en estas categorias. Por el otro lado, la cantidad de cloraminas se concentra en niveles cercanos a 7 para el agua no potable, mientras que para el agua potable se inclina a niveles cercanos a 8.')

st.write('En cuanto a la cantidad de sulfato tiene comportamientos similares para agua potable y no potable, los que se concentran mayormente en valores cercanos a 340, a diferencia de la conductividad que presenta valores mas dispersos mayormente en el rango de 330 y 500. La cantidad de carbon organico en ambos casos se concentran entre 12.5 y 15.4, en el caso de los trihalometanos existe una cantidad mas significativa en los datos cercanos a 68. Por ultimo la cantidad medida en unidades de turbiedad se dispersa en mayor medida entre 3.2 y 5.7 unidades nefelométricas de turbidez.')



st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"RelaciOn entre las varaibles (sin variable objetivo)"}</h1>', unsafe_allow_html=True)
st.image('./images/heatmap.png', width=600)

st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"Conclusiones intermedias"}</h1>', unsafe_allow_html=True)
st.write('Se evidencia que la menor correlaciOn existe entre la totalidad de sOlidos disueltos en el agua y la cantidad de sulfato disuelta, seguido de la totalidad de sOlidos disueltos con el número de ph, y el nivel de dureza frente a la cantidad de sulfato disuelta, mientras que la mayor correlaciOn es entre el nivel de ph y el nivel de dureza, siendo este de sOlo 0.15.')

st.image('./images/pairplot.png')
st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"Conclusiones intermedias"}</h1>', unsafe_allow_html=True)
st.write('Es posible observar que el agua se comporta de manera similar en cada categorias por separado, teniendo en cuenta que en la muestra predomina el agua no potable.Además se evidencia que el agua potable muestra más concentraciOn en el promedio entre cada variable, mientras que el agua no potable llega a tener una mayor dispersiOn. Se puede concluir que el agua no es potable cuando las variables no están en equilibrio y sus valores se alejan de los promedios esperados.')

st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"Boxplots con variable objetivo"}</h1>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.image('./images/ph_boxplot.png', width=340)
with col4:
    st.markdown(f'<h1 style="text-align: center; color:#CB4335 ;font-size:25px;">{"PH - POTABILITY"}</h1>', unsafe_allow_html=True)
    st.write('Tanto para para el agua potable como para la no potable el ph se concentra en niveles entre 6 y 8, ambos presentan una distribucion simetrica de los datos y en el caso del aguna no potable existe una mayor disperciOn.')

col5, col6 = st.columns(2)
with col5:
    st.markdown(f'<h1 style="text-align: center; color:#CB4335 ;font-size:25px;">{"SOLIDS - POTABILITY"}</h1>', unsafe_allow_html=True)
    st.write('Tanto para para el agua potable como para la no potable la cantidad de solidos disueltos se concentra cerca a 20000, en ambos casos se presenta una asimetria positiva lo que indica que la media puede ser mayor que la mediana y se presentan outliers en valores mayores a 40000, sobre el limite superior.')
with col6:
    st.image('./images/Solids_boxplot.png', width=340)


col7, col8 = st.columns(2)
with col7:
    st.image('./images/Hardness_boxplot.png')    
with col8:
    st.markdown(f'<h1 style="text-align: center; color:#CB4335 ;font-size:25px;">{"HARDNESS - POTABILITY"}</h1>', unsafe_allow_html=True)
    st.write('Para los dos casos los niveles de dureza se concentran en los 200, la distribuciOn de la dureza en el agua no potable es simetrica, por el contrario en el agua potable se presenta una asimetria negativa, indicando una media menor a la mediana. Se presentan outliers en tanto el limite inferior como el superior.')


col9, col10 = st.columns(2)
with col9:
    st.markdown(f'<h1 style="text-align: center; color:#CB4335 ;font-size:25px;">{"CHLORAMINES - POTABILITY"}</h1>', unsafe_allow_html=True)
    st.write('Igualmente para los dos casos los niveles se concentran entre 6 y 8, siendo la disperciOn del agua potable ligeramente mayor. En este caso aunque para el valor de la mediana se inclina mas hacia un nivel de cloraminas de 8 mostrando una asimetria negativa, además se presentan outliers que sobrepasan ambos limites.')
with col10:
    st.image('./images/Chloramines_boxplot.png')

col11, col12 = st.columns(2)
with col11:
    st.image('./images/Sulfate_boxplot.png')
with col12:
    st.markdown(f'<h1 style="text-align: center; color:#CB4335 ;font-size:25px;">{"SULFATE - POTABILITY"}</h1>', unsafe_allow_html=True)
    st.write('En el caso de la cantidad de sulfato el agua potable muestra mayor dispersiOn, mostrando también una asimetria positiva, aunque tanto esta como el agua no potable tienen medianas similares.')

col13, col14 = st.columns(2)
with col13:
    st.markdown(f'<h1 style="text-align: center; color:#CB4335 ;font-size:25px;">{"CONDUCTIVITY - POTABILITY"}</h1>', unsafe_allow_html=True)
    st.write('En la conductividad el agua no potable muestra una ligera asimetria positiva, ambas dispersiones se sitúan entre los 380 y 490 aproximadamente y sOlo en el caso del agua no potable se evidencian outliers en los dos limites.')
with col14:
    st.image('./images/Conductivity_boxplot.png')

col15, col16 = st.columns(2)
with col15:
    st.image('./images/Organic_carbon_boxplot.png')    
with col16:
    st.markdown(f'<h1 style="text-align: center; color:#CB4335 ;font-size:22px;">{"ORGANIC CARBON - POTABILITY"}</h1>', unsafe_allow_html=True)
    st.write('Para los dos casos los niveles se concentran entre 12 y 17, siendo la disperciOn del agua no potable ligeramente mayor. En este caso aunque para el valor de la mediana se inclina mas hacia un nivel mayor de carbOn mostrando una asimetria positiv, se presentan outliers que sobrepasan ambos limites siendo mayores en el agua no potable.')



col17, col18 = st.columns(2)
with col17:
    st.markdown(f'<h1 style="text-align: center; color:#CB4335 ;font-size:21px;">{"TRIHALOMETHANES - POTABILITY"}</h1>', unsafe_allow_html=True)
    st.write('Para para los trihalometanos se evidencian ambas dispersiones entre los 55 y 80, en este caso el agua no potable tiene una asimetria negativa mientras el agua potable una ligera asimetria positiva, las dos muestran outliers en ambos limites.')
with col18:
    st.image('./images/Trihalomethanes_boxplot.png')

col19, col20 = st.columns(2)
with col19:
    st.image('./images/Turbidity_boxplot.png')
with col20:
    st.markdown(f'<h1 style="text-align: center; color:#CB4335 ;font-size:25px;">{"TURBIDITY - POTABILITY"}</h1>', unsafe_allow_html=True)
    st.write('En la turbidez el agua potable y no potable muestran medianas similares, junto a distribuciones simétricas entre 3.5 y 4.5, ambos casos presentan outliers tanto en el limite inferior como en el superior.')

st.markdown(f'<h1 style="color:#117A65 ;font-size:35px;">{"Quinta parte: CategorizaciOn de los datos"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"¿El dataset sin la variable objetivo sigue una distribuciOn normal multivariada?"}</h1>', unsafe_allow_html=True)
st.image('./images/hist.png', width=600)

st.markdown(f'<h1 style="text-align: center; color:#000000 ;font-size:20px;">{"Pvalor=4.509462445228134e-66, Normalidad=False"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="text-align: center; color:#000000 ;font-size:20px;">{"Al analizar los datos sin la variable objetivo se rechaza la hipotesis nula, con un p-value menor a 0.05, se concluye que sin la variable objetivo el dataset no sigue una distribuciOn normal multivariada."}</h1>', unsafe_allow_html=True)


st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"¿Cada una de las variables sigue una distribuciOn normal?"}</h1>', unsafe_allow_html=True)

st.write('El P-valor de ph es 1.53318316701255e-13, se rechaza la HipOtesis nula, no se distribuye normalmente')
st.write('El P-valor de Hardness es 0.0021154317073524, se rechaza la HipOtesis nula, no se distribuye normalmente')
st.write('El P-valor de Solids es 1.8058356969296234e-17, se rechaza la HipOtesis nula, no se distribuye normalmente')
st.write('El P-valor de Chloramines es 0.07209037989377975, no hay evidencia suficiente para rechazar la HipOtesis nula, se distribuye normalmente')
st.write('El P-valor de Sulfate es 8.018465519323661e-18, se rechaza la HipOtesis nula, no se distribuye normalmente')
st.write('El P-valor de Conductivity es 2.0186627369689347e-10, se rechaza la HipOtesis nula, no se distribuye normalmente')
st.write('El P-valor de Organic_carbon es 0.3084251582622528, no hay evidencia suficiente para rechazar la HipOtesis nula, se distribuye normalmente')
st.write('El P-valor de Trihalomethanes es 0.0012772877234965563, se rechaza la HipOtesis nula, no se distribuye normalmente')
st.write('El P-valor de Turbidity es 0.6483234763145447, no hay evidencia suficiente para rechazar la HipOtesis nula, se distribuye normalmente')

st.write('El P-valor de Potability es 0.0, se rechaza la HipOtesis nula, no se distribuye normalmente')

st.markdown(f'<h1 style="color:#CB4335 ;font-size:25px;">{"¿Existe alguna diferencia en la media y la mediana de cada una de las variables si se divide el dataset en agua potable y no potable?"}</h1>', unsafe_allow_html=True)


st.table(data.groupby('Potability').agg({'ph':['mean','median'], 'Hardness':['mean','median'], 'Solids':['mean','median'], 'Chloramines':['mean','median'], 'Sulfate':['mean','median'], 'Conductivity':['mean','median'], 'Organic_carbon':['mean','median'], 'Trihalomethanes':['mean','median'], 'Turbidity':['mean','median']}))
st.write('Evaluando la media y la mediana de las variables de las caracteristicas del agua, se encuentra que tanto para agua potable como para agua no potable existen diferencias entre la media y la mediana pero no son significativas, puesto que en una aproximaciOn de los valores de la media estos llegan a ser iguales que los valores de la mediana.')

st.markdown(f'<h1 style="color:#117A65 ;font-size:35px;">{"ConclusiOn General "}</h1>', unsafe_allow_html=True)
st.write('En el dataset se puede observar en primer lugar que la muestra de agua no potable es significativamente mayor a la del modelo, lo cual puede afectar en los resultados. Se busca definir la pureza o potabilidad del agua a partir de diferentes variables las cuales no presentan correlaciones significativas entre ellas. Se puede observar que los componentes del agua tanto pura como potable tienen comportamientos similares, aún asi se evidencia que los datos del agua no potable tienen una dispersiOn mayor, en este caso si tan solo una de las caracteristicas de los componentes no alcanzan o sobrepasa los estándares ideales para un consumo sano creará un desequilibrio, lo que la ingresaria en la clasificaciOn de no potable.')

