"""Estado para manejar eventos del servidor."""

import reflex as rx
from typing import List, Dict
import json

class EventState(rx.State):
    """Estado para manejar eventos del servidor."""
    
    # Lista de clientes conectados
    clients: List[str] = []
    
    def connect(self):
        """Conecta un nuevo cliente."""
        client_id = str(self.get_client_id())
        if client_id not in self.clients:
            self.clients.append(client_id)
    
    def disconnect(self):
        """Desconecta un cliente."""
        client_id = str(self.get_client_id())
        if client_id in self.clients:
            self.clients.remove(client_id)
    
    def broadcast_update(self, event_type: str, data: Dict):
        """Envía una actualización a todos los clientes conectados."""
        message = {
            "type": event_type,
            "data": data
        }
        for client_id in self.clients:
            self.send_event(json.dumps(message), client_id) 