import psutil

def obtener_rendimiento_cpu():
    # Obtiene el uso del CPU en porcentaje
    return psutil.cpu_percent(interval=1)

def obtener_rendimiento_memoria():
    # Obtiene el uso de la memoria en porcentaje
    return psutil.virtual_memory().percent

def obtener_rendimiento_red():
     # Obtiene el uso de la red en porcentaje
    return psutil.net_io_counters().bytes_recv / 1024**3

def obtener_temperatura_cpu():
    # Obtiene la temperatura del CPU en grados Celsius
    try:
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps:
            return temps['coretemp'][1].current
        elif 'fan' in temps:
            return temps['fan'][1].current
        else:
            return -1
    except (AttributeError, KeyError, IndexError):
        return -1

if __name__ == "__main__":
    # Muestra el rendimiento del CPU
    print("Rendimiento del CPU es (%):", obtener_rendimiento_cpu())
    # Muestra el rendimiento de la memoria
    print("Rendimiento de la Memoria (%):", obtener_rendimiento_memoria())
    # Muestra el rendimiento de la red
    print("Rendimiento de la Red (%):", obtener_rendimiento_red())
    # Muestra la temperatura del CPU
    print("Temperatura del CPU:", obtener_temperatura_cpu())

