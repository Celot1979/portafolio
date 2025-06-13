"""Estado para la página de proyectos."""

import reflex as rx
from sqlalchemy.orm import Session
from ..models import Repository
from ..database import get_db
from .event_state import EventState

class ProyectosState(rx.State):
    """Estado para la página de proyectosdd."""

    repositories: list = []

    def load_repositories(self):
        """Carga los repositorios de la base de datos."""
        try:
            db = next(get_db())
            self.repositories = db.query(Repository).all()
        except Exception as e:
            print(f"Error al cargar repositorios: {str(e)}")
        finally:
            db.close()
    
    def on_mount(self):
        """Se ejecuta cuando el componente se monta."""
        EventState.connect()
        self.load_repositories()
    
    def on_unmount(self):
        """Se ejecuta cuando el componente se desmonta."""
        EventState.disconnect()
    
    def handle_event(self, event_data: dict):
        """Maneja los eventos recibidos."""
        event_type = event_data.get("type")
        data = event_data.get("data", {})
        
        if event_type == "repository_added":
            # Añadir el nuevo repositorio a la lista
            new_repo = Repository(
                id=data["id"],
                title=data["title"],
                url=data["url"],
                image_url=data["image_url"]
            )
            self.repositories.append(new_repo)
        elif event_type == "repository_deleted":
            # Eliminar el repositorio de la lista
            self.repositories = [r for r in self.repositories if r.id != data["id"]] 