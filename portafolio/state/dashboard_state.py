"""Estado del dashboard."""

import reflex as rx
from sqlalchemy.orm import Session
from ..models import Repository, BlogPost
from ..database import get_db

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
            
        except Exception as e:
            self.repository_message = f"Error al añadir el repositorio: {str(e)}"
        finally:
            db.close()

    def handle_add_blog_post(self):
        """Maneja la adición de una nueva entrada de blog."""
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
                # Forzar la actualización de la página
                return rx.redirect("/dashboard")
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
                # Forzar la actualización de la página
                return rx.redirect("/dashboard")
            else:
                self.blog_message = "Entrada de blog no encontrada"
        except Exception as e:
            self.blog_message = f"Error al eliminar la entrada de blog: {str(e)}"
        finally:
            db.close()

    pass  # Por ahora está vacío, pero podemos añadir más funcionalidad más tarde 