from auth import authenticate, login_required
from risk import calculate_financial_risk, system_vulnerability_check

def run_app():
    print("--- Sistema de Gestión de Riesgos ---")
    user = input("Usuario: ")
    password = input("Contraseña: ")

    is_logged_in = authenticate(user, password)

    if is_logged_in:
        print("\n[✔] Login exitoso.\n")
        
        score = 650
        deuda = 8000
        resultado = calculate_financial_risk(score, deuda)
        
        print(f"Evaluando cliente con Score {score} y Deuda {deuda}...")
        print(f"Resultado: {resultado}")
        
        status = system_vulnerability_check(45.5)
        print(f"Estado del servidor: {status}")
    else:
        print("\n[✘] Credenciales incorrectas.")

if __name__ == "__main__":
    run_app()
