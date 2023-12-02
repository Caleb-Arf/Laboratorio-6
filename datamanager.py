import time
import random
import threading
from EventManager import EventManager 

class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()
        #variable para detener la generacion de datos
        self.stop_data = False
    
    def start_real_time_updates(self):
        while self.stop_data == False:
            self.generate_real_time_data()
            self.event_manager.notify("data_update", self.data)
            time.sleep(1)

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)

if __name__ == "__main__":
    
    real_time_data_manager = RealTimeDataManager()

    # Suscribir callback al EventManager
    def print_updated_data(data):
        print(f"Datos en tiempo real actualizados: {data}")

    real_time_data_manager.event_manager.subscribe("data_update", print_updated_data)

    # Iniciar actualizaciones en tiempo real
    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    update_thread.start()

    try:
        while True:
            time.sleep(0)                            
    except KeyboardInterrupt:
        real_time_data_manager.stop_data = True
        update_thread.join()
        print("\nPrograma terminado.")