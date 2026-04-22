import psutil


def metrics_tool(query: str) -> str:
    """
    Proporciona las métricas del sistema en tiempo real (CPU, memoria, disco).
    Úsala para diagnosticar lentitud o estado del hardware.
    """
    query = query.lower()
    
    cpu_warn = "(Si el uso de CPU supera el 80%, advierte sobre alto consumo y posible lentitud)."
    mem_warn = "(Si el uso de memoria supera el 80%, advierte sobre posible falta de recursos)."
    
    if "cpu" in query:
        cpu = psutil.cpu_percent(interval=1)
        return f"El uso del CPU es {cpu}%. {cpu_warn}"
        
    elif "memoria" in query or "ram" in query:
        memory = psutil.virtual_memory()
        return (f"El uso de la memoria es {memory.percent}%, con "
                f"{round(memory.available / (1024**3), 2)} GB disponibles. {mem_warn}")
        
    elif "disco" in query or "hdd" in query or "ssd" in query:
        disk = psutil.disk_usage('/')
        return f"El uso del disco es {disk.percent}%."
        
    else:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return (
            f"Reporte General: CPU al {cpu}% {cpu_warn}. "
            f"Memoria al {memory.percent}% con {round(memory.available / (1024**3), 2)} GB disponibles {mem_warn}. "
            f"Disco al {disk.percent}%."
        )
