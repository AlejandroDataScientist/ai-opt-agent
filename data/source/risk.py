def calculate_financial_risk(score: int, debt: float):
    if score < 300:
        return "Riesgo: ALTO (No elegible para crédito)"
    elif 300 <= score < 700:
        if debt > 5000:
            return "Riesgo: MEDIO (Requiere revisión manual)"
        return "Riesgo: BAJO (Elegible con condiciones)"
    return "Riesgo: MÍNIMO (Aprobado)"

def system_vulnerability_check(cpu_usage: float):
    if cpu_usage > 90:
        return "Alerta: Riesgo crítico de caída del sistema."
    return "Sistema estable."
