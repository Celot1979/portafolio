"""Estado para la página de blog."""

import reflex as rx
from typing import List
from sqlalchemy.orm import Session
from ..models import BlogPost
from ..database import get_db
from .event_state import EventState


class BlogState(rx.State):
    """Estado para la página de blog."""

    blog_posts: List[BlogPost] = []

    def load_blog_posts(self):
        """Carga las entradas del blog de la base de datos."""
        try:
            db = next(get_db())
            self.blog_posts = db.query(BlogPost).all()
        except Exception as e:
            print(f"Error al cargar entradas de blog: {str(e)}")
        finally:
            db.close()
    
    def on_mount(self):
        """Se ejecuta cuando el componente se monta."""
        EventState.connect()
        self.load_blog_posts()
    
    def on_unmount(self):
        """Se ejecuta cuando el componente se desmonta."""
        EventState.disconnect()
    
    def handle_event(self, event_data: dict):
        """Maneja los eventos recibidos."""
        event_type = event_data.get("type")
        data = event_data.get("data", {})
        
        if event_type == "blog_post_added":
            # Añadir la nueva entrada de blog a la lista
            new_post = BlogPost(
                id=data["id"],
                title=data["title"],
                content=data["content"],
                image_url=data["image_url"]
            )
            self.blog_posts.append(new_post)
        elif event_type == "blog_post_deleted":
            # Eliminar la entrada de blog de la lista
            self.blog_posts = [p for p in self.blog_posts if p.id != data["id"]] 