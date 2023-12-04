import psutil
import platform
import subprocess
import time

def ping_ip(ip_address):
    command = ['ping', '-c', '4', ip_address]
    result = subprocess.run(command, capture_output=True, text=True)
    print(f"\nTiempo de respuesta para la IP {ip_address}:")
    for respuesta in result.stdout.splitlines():
        if not respuesta.strip().startswith("Ping"):
            continue
        tiempo_de_respuesta = float(respuesta.split()[5])
        print(f"Tiempo de respuesta: {tiempo_de_respuesta} segundos")

def obtener_rendimiento_cpu():
    # Obtiene el uso del CPU en porcentaje
    return psutil.cpu_percent(interval=1)

def obtener_rendimiento_memoria():
    # Obtiene el uso de la memoria en porcentaje
    return psutil.virtual_memory().percent

def obtener_rendimiento_red():
    # Obtiene el uso de la red en porcentaje
    return psutil.net_io_counters().bytes_recv / 1024**3

def obtener_sistema_operativo():
    # Obtiene el sistema operativo de la PC
    return platform.system()

def imprimir_informacion_local():
    print("Información de tu PC:")
    # Muestra el rendimiento del CPU
    print("Rendimiento del CPU (%):", obtener_rendimiento_cpu())
    # Muestra el rendimiento de la memoria
    print("Rendimiento de la Memoria (%):", obtener_rendimiento_memoria())
    # Muestra el rendimiento de la red
    print("Rendimiento de la Red:", obtener_rendimiento_red())
    # Muestra el sistema operativo de la PC
    print("Sistema Operativo:", obtener_sistema_operativo())

def imprimir_informacion_ping(ip_address):
    ping_ip(ip_address)
    print("\nInformación de la PC con la IP", ip_address)
    # Muestra el rendimiento del CPU
    print("Rendimiento del CPU (%):", obtener_rendimiento_cpu())
    # Muestra el rendimiento de la memoria
    print("Rendimiento de la Memoria (%):", obtener_rendimiento_memoria())
    # Muestra el rendimiento de la red
    print("Rendimiento de la Red:", obtener_rendimiento_red())
    # Muestra el sistema operativo de la PC
    print("Sistema Operativo:", obtener_sistema_operativo())

if __name__ == "__main__":
    # Información de tu propia PC
    imprimir_informacion_local()

    # Información de la PC con la dirección IP especificada
    ip_a_pingear = "192.168.1.8"  # Reemplaza con la dirección IP que desees pinguear
    imprimir_informacion_ping(ip_a_pingear)
