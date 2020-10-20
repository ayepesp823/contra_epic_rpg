"""
Este es un bot destinado a realizar las actividades de colecta
del bot-juego de discord epic-rpg.
Su función es hacer caza y el trabajo determinado.
Se basará en la dependencia temporal para realizar las distintas acciones
Cumplirá tambin con la función de comprar pociones de vida y curarse
version: 3.0.2
"""
#! Paquetes en uso:

from time import time as Time
import time
import pyautogui as pag
import keyboard

#! Constantes:

minuto = 60.0 #? un minuto son 60 segundos
hora = 60.0 #? una hora son 60 minutos
t_caza = minuto #? tiempo entre cada operacion de caza
t_trabajo = 5.0 * minuto #? tiempo entre cada trabajo
t_aventura = hora * minuto #? tiempo entre cada aventura
t_raid = 3 * hora * minuto #? tiempo entre cada raid
t_entrenamiento = 15.0 * minuto #? tiempo entre cada entrenemiento
t_lootbox = 2 * hora * minuto
adicion = 1.0 #? tiempo adicionado para despistar el antibot
intervalo = 0.08 #? itervalo de escritura
numero_max_int_f = 5 #? numero maximo de intentos fallidos
entrada_no_valida = '\n Entrada no valida, vuelva a intentar. \n'
mensaje_salida = '\n Usted ha excetido el numero máximo de intentos fallidos.\n Favor reinicie el programa.'
trabajos_dic = {'Pesca': 'fish', 'Tala':'chop', 'Recoger': 'pickup',
                'Hacha': 'axe', 'Atarraya': 'net', 'Escalera': 'ladder',
                 'Minar': 'mine', 'Serrucho': 'bowsaw', 'Barco': 'boat',
                 'Pico': 'pickaxe', 'Tractor': 'tractor', 'Motosierra': 'chainsaw',
                 'Botezote': 'bigboat', 'Perforadora': 'drill','Invernadero': 'greenhouse',
                 'Dinamita': 'dynamite'}#? comando que se escribe
lootbox_dic = {'Comun': ['common',1000], 'Extraña': ['uncommon',7500],'Rara': ['rare',50000],
               'Epica':['epic',200000],'Edgy':['edgy',420666]}#? cajas disponibles, incluye precio
no_curar = 300 #? si se ingresa un numero igual o superior a este
               #? al momento de configurar, no se aplicara curación.
pausa = 5 #? tiempo de espera
palabra_clave = 'Elmerkescoya123'


#! Oraciones:

caza = 'rpg hunt'
trabajo = 'rpg '
compra = 'rpg buy life potion'
curar = 'rpg heal'
aventura = 'rpg adv'
entranamiento = 'rpg training'
lootbox = 'rpg buy {} lootbox'
abrir = 'rpg open'
raid = 'rpg guild raid {}'
texto1 = '   {})    {}.\n'
texto2 = '   {})   {}.\n'
muestra = '{}.---->${}\n'
texto_trabajo = 'Trabajos disponibles a realizar:\n'
texto_lootbox = 'Caja---->Precio\n'
detectar_mouse = ('Iniciando deteccion de la posicion del mouse.\nEsta posicion se utilizará como punto\n inicial para la escritura del bot.\nSe Medirá en {} segundos')

#! Variables, inicialización:

ultima_caza = 0 #? tiempo en el que ocurio la ultima accion de cazar
ultimo_trabajo = 0 #? tiempo en el que ocurio el ultimo trabajo
ultima_aventura = 0 #? tiempo en el que ocurrio la ultima aventura
ultimo_entrenamiento = 0 #? tiempo en el que ocurrio el ultimo entrenamiento
ultima_caja = 0 #? tiempo en el que se compró la última caja
ultima_raid = 0 #? tiempo en el que ocurrio el ultimo raid.
numero_caza = 0 #? numero de cazas realizadas, se tiene en cueta para currarse
entrenamiento_auto = None #? activar training automaticamente
raid_auto = None #? activar raid automaticamente
numero_raid = None #? numero de energíaa buscar
numero_intentos = 0 #? numero de intentos
numero_intentos_alt = 0 #? variable de apoyo
posicion_x = None #? posicionar el mouse x 862
posicion_y = None #? posicionar el mose y 725
click_activo = None #? autoclick activo
numero_de_posiones = 0 #? cantidad de posiciones que se tiene
lootbox_auto = None #? realizar compra de cajas automática
contra = None #?
cuenta1 = 0
cuenta2 = 0
cuenta3 = 0

#! Funciones a usar:


def escribir(accion):
    """
    Esta funcion realiza la operacion de escribir,
    su entrada es la accion, debe ser tipo str.
    """
    if click_activo == 'activo':
        pag.click(posicion_x, posicion_y)
    pag.press('enter')
    pag.write(accion, interval = intervalo)
    pag.press('enter')
    time.sleep(1.2)

def salir_programa(n):
    """
    Esta funcion evaluda si el programa se debe detener por exceder
    el numero maximo de respuestas erradas. La variable es tipo int.
    """
    if n == numero_max_int_f:
        pag.alert(text = mensaje_salida, title = '', button = 'OK')
        exit()

def salir(palabra):
    """
    Esta funcion mira si se desea salir del programa
    """
    if palabra == 'terminar':
        pag.alert(text ='Terminando el programa', title = '', button = 'OK')
        exit()

#! Bot a funcionar:

pag.alert(text = detectar_mouse.format(pausa), title = 'Detección de Mouse', button = 'OK')

for i in range(pausa):
    time.sleep(1)

posicion_x, posicion_y = pag.position()
pag.alert(text = 'Posicion detectada correctamente.', title = 'Detección completada', button = 'OK')
time.sleep(0.5)

while numero_intentos < numero_max_int_f:
    numero_intentos += 1
    click_activo = str(pag.confirm(text = '¿Qué tipo de click desea realizar?',title = 'Tipo de click', buttons = ['Activo', 'Pasivo']))
    if click_activo == 'Activo' or click_activo == 'Pasivo':
        click_activo = click_activo.casefold()
        break
    else:
        pag.alert(text = entrada_no_valida, title = '',button = 'OK')
    time.sleep(0.5)

salir_programa(numero_intentos)
numero_intentos = 0

contra = pag.password(text = 'Introdusca la palabra clave,\n si no tiene una presione ok', title = 'Palabra clave', mask = 'X')

for loot in lootbox_dic.keys():
    texto_lootbox += muestra.format(loot,lootbox_dic[loot][1])
pag.alert(text = texto_lootbox,title = 'Lootbox disponibles',button = 'OK')

while numero_intentos < numero_max_int_f:
    numero_intentos += 1
    lootbox_auto = str(pag.confirm(text = '¿Desea que el bot ejecute automáticamete el comando de Comprar cajas?',title = 'Lootbox',buttons = ['si', 'no']))
    if lootbox_auto == 'si' or lootbox_auto == 'no':
        if lootbox_auto == 'si':
            while numero_intentos_alt < numero_max_int_f:
                numero_intentos_alt += 1
                Q_lootbox = str(pag.prompt(text = 'Escriba a continuación el tipo de caja:',title = 'Selección de la Lottbox',default = 'Comun'))
                salir(Q_lootbox)
                Q_lootbox = Q_lootbox.casefold().capitalize()
                if Q_lootbox in lootbox_dic.keys():
                    Q_lootbox = lootbox_dic[Q_lootbox][0]
                    break
                else:
                    pag.alert(text = entrada_no_valida, title = '',button = 'OK')
            salir_programa(numero_intentos_alt)
            lootbox = lootbox.format(Q_lootbox)
        break
    else:
        pag.alert(text = entrada_no_valida, title = '',button = 'OK')
    time.sleep(0.5)

salir_programa(numero_intentos)
numero_intentos = 0
numero_intentos_alt = 0



for n, trabajos in enumerate(trabajos_dic.keys()):
    if n <= 8:
        texto_trabajo += texto1.format(n+1, trabajos)
    if n<= 98 and n > 8:
        texto_trabajo += texto2.format(n+1, trabajos)
pag.alert(text = texto_trabajo, title = 'Trabjos Disponibles', button = 'OK')
time.sleep(0.5)

while numero_intentos < numero_max_int_f:
    numero_intentos += 1
    Q_trabajo = str(pag.prompt(text = 'Escriba a continuación el tipo de trabajo:',title = 'Selección del Trabajo',default = 'Pesca'))
    salir(Q_trabajo)
    Q_trabajo = Q_trabajo.casefold().capitalize()
    if Q_trabajo in trabajos_dic.keys():
        Q_trabajo = trabajos_dic[Q_trabajo]
        break
    else:
        pag.alert(text = entrada_no_valida, title = '',button = 'OK')
    time.sleep(0.5)

salir_programa(numero_intentos)
numero_intentos = 0

trabajo = trabajo + Q_trabajo

while numero_intentos < numero_max_int_f:
    numero_intentos += 1
    try:
        numero_max = int(pag.prompt(text = 'Numero de ataques antes de aplicar curación:', title = 'Ataques',default = '1'))
        break
    except:
        pag.alert(text = entrada_no_valida, title = '',button = 'OK')
    time.sleep(0.5)

salir_programa(numero_intentos)
numero_intentos = 0

while numero_intentos < numero_max_int_f:
    numero_intentos += 1
    entrenamiento_auto = str(pag.confirm(text = '¿Desea que el bot ejecute automaticamente el comando de entranamiento?',title = 'Entrenamiento', buttons = ['si', 'no']))
    if entrenamiento_auto == 'si' or entrenamiento_auto == 'no':
        break
    else:
        pag.alert(text = entrada_no_valida, title = '',button = 'OK')
    time.sleep(0.5)

salir_programa(numero_intentos)
numero_intentos = 0
if contra == palabra_clave:
    while numero_intentos < numero_max_int_f:
        numero_intentos += 1
        raid_auto = str(pag.confirm(text = '¿Desea que el bot ejecute automáticamete el comando de raid?',title = 'Raid',buttons = ['si', 'no']))
        if raid_auto == 'si' or raid_auto == 'no':
            if raid_auto == 'si':
                while numero_intentos_alt < numero_max_int_f:
                    numero_intentos_alt += 1
                    try:
                        numero_raid = int(pag.prompt(text = 'Nivel medio de energía a buscar en raid (tipo int):',title = 'Energía',default = '50'))
                        break
                    except:
                        pag.alert(text = entrada_no_valida, title = '',button = 'OK')
                    time.sleep(0.5)
                salir_programa(numero_intentos_alt)
            break
        else:
            pag.alert(text = entrada_no_valida, title = '',button = 'OK')
        time.sleep(0.5)
    salir_programa(numero_intentos)
    numero_intentos = 0
    numero_intentos_alt = 0

while numero_intentos < numero_max_int_f:
    numero_intentos += 1
    try:
        numero_de_posiones = int(pag.prompt(text = 'Escriba la cantidad de posiones con las que cuenta (tipo int): ',title = 'Cantidad de posiones',default = '0'))
        break
    except:
        pag.alert(text = entrada_no_valida, title = '',button = 'OK')
    time.sleep(0.5)

salir_programa(numero_intentos)
numero_intentos = 0

while numero_intentos < numero_max_int_f:
    numero_intentos += 1
    cura = str(pag.confirm(text = '¿Desea una cura inicial?',title = 'Cura inicial.',buttons = ['si', 'no']))
    pag.click(posicion_x, posicion_y)
    if cura == 'si':
        if numero_de_posiones == 0:
            escribir(compra)
            numero_de_posiones += 1
        escribir(curar)
        numero_de_posiones -= 1
        break
    elif cura == 'no':
        break
    else:
        pag.alert(text = entrada_no_valida, title = '',button = 'OK')
    time.sleep(0.5)

salir_programa(numero_intentos)
numero_intentos = 0

while True:
    t = Time()
    if (t - ultima_caja) > (t_lootbox + adicion) and lootbox_auto == 'si':
        escribir(abrir)
        escribir(lootbox)
        escribir(abrir)
        ultima_caja = Time()
    if (t - ultima_aventura) > (t_aventura + 3 * adicion) and numero_caza == 0:
        escribir(aventura)
        if numero_de_posiones == 0:
            escribir(compra)
            numero_de_posiones += 1
        escribir(curar)
        numero_de_posiones -= 1
        ultima_aventura = Time()
    if (t - ultima_raid) > (t_raid + 3 * adicion) and raid_auto == 'si':
        escribir(raid.format(numero_raid))
        ultima_raid = Time()
    if (t - ultima_caza) > (t_caza + adicion):
        if numero_max < no_curar:
            numero_caza += 1
        escribir(caza)
        ultima_caza = Time()
    if (t - ultimo_trabajo) > (t_trabajo + adicion):
        escribir(trabajo)
        ultimo_trabajo = Time()
    if numero_caza >= numero_max:
        if numero_de_posiones == 0:
            escribir(compra)
            numero_de_posiones +=1
        escribir(curar)
        numero_de_posiones -= 1
        numero_caza=0
    if (t - ultimo_entrenamiento) > (t_entrenamiento + adicion) and entrenamiento_auto == 'si':
        escribir(entranamiento)
        time.sleep(20)
        ultimo_entrenamiento = Time()
    try:
        if keyboard.is_pressed('q'):
            cuenta1 += 1
    except:
        break
    if cuenta1 > 0:
        if cuenta1 > 5000:
            salida = pag.confirm(text = '¿Seguro desea salir?',title = '',buttons = ['si','no'])
            if salida == 'si':
                exit()
            else:
                cuenta1 = 0
        if cuenta1 == cuenta2:
            cuenta3 += 1
        if cuenta3 > 5000:
            cuenta1 = 0
            cuenta2 = 0
            cuenta3 = 0
        cuenta2 = cuenta1