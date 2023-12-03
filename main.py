import clases.lector
import clases.interfaz
import threading


hilo_log = threading.Thread(target=clases.lector.iniciarlector)
hilo_log.start()


clases.interfaz.iniciarinterfaz()

#clases.interfaz.prueba()









