import subprocess
import time
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

def ping_ip(ip_address):
    command = ['ping', '-c', '4', ip_address]
    result = subprocess.run(command, capture_output=True, text=True)
    print(f"Tiempo de respuesta para la IP {ip_address}:")
    for respuesta in result.stdout.splitlines():
        if not respuesta.strip().startswith("Ping"):
            continue
        tiempo_de_respuesta = float(respuesta.split()[5])
        print(f"Tiempo de respuesta: {tiempo_de_respuesta} segundos")

def obtener_rendimiento_cpu(ip_address):
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Uso de CPU para la IP {ip_address}: {cpu_percent}%")

if __name__ == "__main__":
    # Muestra el rendimiento del CPU
    print("Uso del CPU:", get_cpu_usage())

    # Muestra el rendimiento de la memoria
    print("Uso de la memoria:", get_memory_usage())

    # Muestra el rendimiento de la red
    print("Uso de la red:", get_network_usage())

    # Muestra la temperatura del CPU
    print("Temperatura del CPU:", get_cpu_temperature())

    ips = ["10.3.21.194", "10.3.21.195", "10.3.21.196", "10.3.21.197"]

    for ip in ips:
        ping_ip(ip)
        obtener_rendimiento_cpu(ip)
        time.sleep(1)