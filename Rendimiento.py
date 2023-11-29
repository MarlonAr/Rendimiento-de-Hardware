import psutil

def get_cpu_usage():
    # Obtiene el uso del CPU en porcentaje
    return psutil.cpu_percent()

def get_memory_usage():
    # Obtiene el uso de la memoria en porcentaje
    return psutil.virtual_memory().percent

def get_network_usage():
    # Obtiene el uso de la red en porcentaje
    return psutil.net_io_counters().bytes_recv / 1024**3

def get_cpu_temperature():
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
    print("Uso del CPU:", get_cpu_usage())

    # Muestra el rendimiento de la memoria
    print("Uso de la memoria:", get_memory_usage())

    # Muestra el rendimiento de la red
    print("Uso de la red:", get_network_usage())

    # Muestra la temperatura del CPU
    print("Temperatura del CPU:", get_cpu_temperature())

