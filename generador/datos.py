#En este script se guardan los datos sensibles en la aplicación.
#No debe compartirse este archivo, mas que como binario al momento 
#de compartir una aplicación.

#Por la misma seguridad que se usará en este script q almacena los tokens de acceso 
#se usara este mismo archivo como repositorio de los mensajes de información que 
#no se va a cambiar. 

#TOKENS

#El token de telegram, que se consigue con el fatherbot
token = '1869878107:AAF1KJIuUK6j-l08AH4LE0u1J1hqqLyP5o8'
#El token de openWeather maps para consultas de clima
tauken = '5191c33b7b0079d23ef33dfee00d6084'
#el numero id telegram del creador del bot. 
master = 89650251



#Aqui se declararán tres categorias de mensajes:
# 1 consejos practicos (random).
# 2 consejos covid (bajo consejo médico).
# 3 información vacunas (información técnica).


messages = [
    'QUÉDATE EN CASA. SALVA VIDAS.',
    'QUÉDATE en casa lo máximo posible',
    'MANTÉN el distanciamiento social',
    'LÁVATE las manos con frecuencia',
    'TOSE cubriéndote con el codo',
    'LLAMA al médico de familia si tienes síntomas',
    '''Puede reducir el riesgo de infección:
- Lavándose las manos regularmente con agua y jabón o con desinfectante de manos a base de alcohol
- Cubriéndose la nariz y la boca al toser y estornudar con un pañuelo de papel desechable o con la parte interna del codo
- Evitando el contacto directo (1 metro o 3 pies) con cualquier persona con síntomas de resfriado o gripe (influenza)''',
    '''Los signos y síntomas pueden ser:
- dolor de garganta
- tos
- fiebre
- dificultad para respirar (en casos graves)''']




#una función para randomizar consejos
import time
import random

random.seed(time.perf_counter())

doctors = ['👨‍⚕️','👨🏻‍⚕️','👨🏼‍⚕️','👨🏽‍⚕️','👨🏾‍⚕️','👨🏿‍⚕️','👩‍⚕️','👩🏻‍⚕️','👩🏼‍⚕️','👩🏽‍⚕️','👩🏾‍⚕️','👩🏿‍⚕️']

def getDoc():
    return doctors[random.randint(0, len(doctors)-1)]

def getMessage():
    return getDoc() + ' ' + messages[random.randint(0, len(messages)-1)]









