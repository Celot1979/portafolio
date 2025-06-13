"""Estado del dashboard. Buscando la forma de que solo se pueda acceder a esta página si el usuario está logeado."""

import reflex as rx
from sqlalchemy.orm import Session
from ..models import Repository, BlogPost
from ..database import get_db
from .proyectos_state import ProyectosState
from .blog_state import BlogState
from .event_state import EventState

class DashboardState(rx.State):
    """Estado del dashboard."""
    
    # Campos para el formulario de repositorio
    repository_title: str = ""
    repository_url: str = ""
    repository_image_url: str = ""
    
    # Campos para el formulario de blog
    title: str = ""
    content: str = ""
    image_url: str = ""
    
    # Mensajes de estado
    repository_message: str = ""
    blog_message: str = ""

    # Listas de datos
    repositories: list = []
    blog_posts: list = []

    def set_repository_title(self, value: str):
        """Establece el título del repositorio."""
        self.repository_title = value

    def set_repository_url(self, value: str):
        """Establece la URL del repositorio."""
        self.repository_url = value

    def set_repository_image_url(self, value: str):
        """Establece la URL de la imagen del repositorio."""
        self.repository_image_url = value

    def set_title(self, value: str):
        """Establece el título de la entrada de blog."""
        self.title = value

    def set_content(self, value: str):
        """Establece el contenido de la entrada de blog."""
        self.content = value

    def set_image_url(self, value: str):
        """Establece la URL de la imagen de la entrada de blog."""
        self.image_url = value

    def load_data(self):
        """Carga los datos de la base de datos."""
        try:
            db = next(get_db())
            self.repositories = db.query(Repository).all()
            self.blog_posts = db.query(BlogPost).all()
        except Exception as e:
            print(f"Error al cargar datos: {str(e)}")
        finally:
            db.close()

    def on_mount(self):
        """Se ejecuta cuando el componente se monta."""
        EventState.connect()
        self.load_data()
    
    def on_unmount(self):
        """Se ejecuta cuando el componente se desmonta."""
        EventState.disconnect()
    
    def handle_event(self, event_data: dict):
        """Maneja los eventos recibidos."""
        event_type = event_data.get("type")
        data = event_data.get("data", {})
        
        if event_type == "repository_added":
            # Añadir el nuevo repositorio a la lista
            self.repositories.append(Repository(**data))
        elif event_type == "repository_deleted":
            # Eliminar el repositorio de la lista
            self.repositories = [r for r in self.repositories if r.id != data["id"]]
        elif event_type == "blog_post_added":
            # Añadir la nueva entrada de blog a la lista
            self.blog_posts.append(BlogPost(**data))
        elif event_type == "blog_post_deleted":
            # Eliminar la entrada de blog de la lista
            self.blog_posts = [p for p in self.blog_posts if p.id != data["id"]]

    def handle_add_repository(self):
        """Maneja la adición de un nuevo repositorio."""
        print(f"Título: {self.repository_title}, URL: {self.repository_url}, Imagen: {self.repository_image_url}")
        if not self.repository_title or not self.repository_url or not self.repository_image_url:
            self.repository_message = "Todos los campos son obligatorios."
            return
        try:
            db = next(get_db())
            new_repository = Repository(
                title=self.repository_title,
                url=self.repository_url,
                image_url=self.repository_image_url
            )
            db.add(new_repository)
            db.commit()
            db.refresh(new_repository)
            
            # Limpiar el formulario
            self.repository_title = ""
            self.repository_url = ""
            self.repository_image_url = ""
            self.repository_message = "Repositorio añadido correctamente"
            
            # Actualizar los datos
            self.load_data()
            ProyectosState.load_repositories()
            
            # Notificar a todos los clientes
            EventState.broadcast_update("repository_added", {
                "id": new_repository.id,
                "title": new_repository.title,
                "url": new_repository.url,
                "image_url": new_repository.image_url
            })
            
        except Exception as e:
            self.repository_message = f"Error al añadir el repositorio: {str(e)}"
        finally:
            db.close()

    def handle_add_blog_post(self):
        """Maneja la adición de una nueva entrada de blog."""
        print(f"Título: {self.title}, Contenido: {self.content}, Imagen: {self.image_url}")
        if not self.title or not self.content or not self.image_url:
            self.blog_message = "Todos los campos son obligatorios."
            return
        try:
            db = next(get_db())
            new_blog_post = BlogPost(
                title=self.title,
                content=self.content,
                image_url=self.image_url
            )
            db.add(new_blog_post)
            db.commit()
            db.refresh(new_blog_post)
            
            # Limpiar el formulario
            self.title = ""
            self.content = ""
            self.image_url = ""
            self.blog_message = "Entrada de blog añadida correctamente"
            
            # Actualizar los datos
            self.load_data()
            BlogState.load_blog_posts()
            
            # Notificar a todos los clientes
            EventState.broadcast_update("blog_post_added", {
                "id": new_blog_post.id,
                "title": new_blog_post.title,
                "content": new_blog_post.content,
                "image_url": new_blog_post.image_url
            })
            
        except Exception as e:
            self.blog_message = f"Error al añadir la entrada de blog: {str(e)}"
        finally:
            db.close()

    def delete_repository(self, repo_id: int):
        """Elimina un repositorio de la base de datos."""
        try:
            db = next(get_db())
            repo = db.query(Repository).filter(Repository.id == repo_id).first()
            if repo:
                db.delete(repo)
                db.commit()
                self.repository_message = "Repositorio eliminado correctamente"
                
                # Actualizar los datos
                self.load_data()
                ProyectosState.load_repositories()
                
                # Notificar a todos los clientes
                EventState.broadcast_update("repository_deleted", {
                    "id": repo_id
                })
            else:
                self.repository_message = "Repositorio no encontrado"
        except Exception as e:
            self.repository_message = f"Error al eliminar el repositorio: {str(e)}"
        finally:
            db.close()

    def delete_blog_post(self, post_id: int):
        """Elimina una entrada de blog de la base de datos."""
        try:
            db = next(get_db())
            post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
            if post:
                db.delete(post)
                db.commit()
                self.blog_message = "Entrada de blog eliminada correctamente"
                
                # Actualizar los datos
                self.load_data()
                BlogState.load_blog_posts()
                
                # Notificar a todos los clientes
                EventState.broadcast_update("blog_post_deleted", {
                    "id": post_id
                })
            else:
                self.blog_message = "Entrada de blog no encontrada"
        except Exception as e:
            self.blog_message = f"Error al eliminar la entrada de blog: {str(e)}"
        finally:
            db.close()

    pass  # Por ahora está vacío, pero podemos añadir más funcionalidad más tarde 