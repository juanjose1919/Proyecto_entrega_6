import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title('¿AGUA POTABLE?')
st.header('Evaluar la potabilidad del agua es un factor importante de la vida humana, dado que si los seres humanos están consumiendo agua contaminada, lo más probable es desarrollar problemas de salud, vulnerando los derechos fundamentales. Por este motivo se evaluará la potabilidad del agua con las siguientes variables:')

data = pd.read_csv('https://raw.githubusercontent.com/labeconometria/MLxE/main/proyectos2do/datasets3.csv')

pot = [['Potability','Potabilidad ','Indica si el agua es segura para el consumo humano, donde 1 significa potable y 0 significa no potable.'],['Ph','Ph','El PH es un parámetro para evaluar el equilibrio ácido-base del agua. La OMS ha recomendado un limite máximo permisible de pH de 6,5 a 8,5'],['Hardness','Dureza','La dureza está causada principalmente por las sales de calcio y magnesio. Estas sales se disuelven en los depOsitos geolOgicos por los que pasa el agua'],['Solids','Solidos','El agua tiene la capacidad de disolver una amplia gama de minerales o sales inorgánicas y algunas orgánicas como el potasio, el calcio, el sodio, los bicarbonatos, los cloruros, el magnesio, los sulfatos, etc'],['Chloramines','Cloraminas','El cloro y la cloramina son los principales desinfectantes utilizados en los sistemas públicos de agua'],['Sulfate','Sulfato','Los sulfatos son sustancias naturales que se encuentran en los minerales, el suelo y las rocas'],['Conductivity','Conductividad','El agua pura no es un buen conductor de la corriente eléctrica más bien es un buen aislante'],['Organic_carbon','Carbono orgánico','El carbono orgánico total (COT) en las aguas de origen proviene de la materia orgánica natural en descomposiciOn (NOM), asi como de fuentes sintéticas'],['Trihalomethanes','Trihalometanos','Los THM son sustancias quimicas que pueden encontrarse en el agua tratada con cloro'],['Turbidity','Turbidez','La turbidez del agua depende de la cantidad de materia sOlida presente en estado de suspensiOn']]

st.table(pot)

#pot = data['Potability'].value_counts()
#pot.index = ['NO', 'SI']
#fig, ax = plt.subplots(1,1)
#ax.set_title('Proporción de potabilidad')
#ax.bar(pot.index, pot.values, color = 'orange')

st.pyplot(fig)

