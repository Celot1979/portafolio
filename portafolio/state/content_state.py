"""Estado para manejar el contenido del portafolio."""

import reflex as rx
from typing import List, Optional
from ..models import BlogPost, Repository
from ..database import get_db

class ContentState(rx.State):
    """Estado para manejar el contenido del portafolio."""
    
    # Campos para blogs
    blog_title: str = ""
    blog_content: str = ""
    blog_image_url: str = ""
    blog_message: str = ""
    
    # Campos para repositorios
    repo_title: str = ""
    repo_url: str = ""
    repo_image_url: str = ""
    repo_message: str = ""
    
    # Listas de contenido
    blog_posts: List[BlogPost] = []
    repositories: List[Repository] = []
    
    def load_content(self):
        """Carga todo el contenido de la base de datos."""
        try:
            db = next(get_db())
            self.blog_posts = list(db.query(BlogPost).all())
            self.repositories = list(db.query(Repository).all())
        except Exception as e:
            print(f"Error al cargar el contenido: {str(e)}")
            self.blog_posts = []
            self.repositories = []
        finally:
            db.close()
    
    def add_blog_post(self):
        """Añade una nueva entrada de blog."""
        if not all([self.blog_title, self.blog_content]):
            self.blog_message = "El título y el contenido son obligatorios."
            return
            
        try:
            db = next(get_db())
            new_post = BlogPost(
                title=self.blog_title,
                content=self.blog_content,
                image_url=self.blog_image_url or None
            )
            db.add(new_post)
            db.commit()
            db.refresh(new_post)
            
            # Actualizar la lista de posts
            self.blog_posts = list(db.query(BlogPost).all())
            
            # Limpiar el formulario
            self.blog_title = ""
            self.blog_content = ""
            self.blog_image_url = ""
            self.blog_message = "Entrada de blog añadida correctamente"
            
        except Exception as e:
            self.blog_message = f"Error al añadir la entrada: {str(e)}"
        finally:
            db.close()
    
    def add_repository(self):
        """Añade un nuevo repositorio."""
        if not all([self.repo_title, self.repo_url]):
            self.repo_message = "El título y la URL son obligatorios."
            return
            
        try:
            db = next(get_db())
            new_repo = Repository(
                title=self.repo_title,
                url=self.repo_url,
                image_url=self.repo_image_url or None
            )
            db.add(new_repo)
            db.commit()
            db.refresh(new_repo)
            
            # Actualizar la lista de repositorios
            self.repositories = list(db.query(Repository).all())
            
            # Limpiar el formulario
            self.repo_title = ""
            self.repo_url = ""
            self.repo_image_url = ""
            self.repo_message = "Repositorio añadido correctamente"
            
        except Exception as e:
            self.repo_message = f"Error al añadir el repositorio: {str(e)}"
        finally:
            db.close()
    
    def delete_blog_post(self, post_id: Optional[int] = None):
        """Elimina una entrada de blog."""
        if post_id is None:
            return
            
        try:
            db = next(get_db())
            post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
            if post:
                db.delete(post)
                db.commit()
                self.blog_posts = list(db.query(BlogPost).all())
                self.blog_message = "Entrada eliminada correctamente"
            else:
                self.blog_message = "Entrada no encontrada"
        except Exception as e:
            self.blog_message = f"Error al eliminar la entrada: {str(e)}"
        finally:
            db.close()
    
    def delete_repository(self, repo_id: Optional[int] = None):
        """Elimina un repositorio."""
        if repo_id is None:
            return
            
        try:
            db = next(get_db())
            repo = db.query(Repository).filter(Repository.id == repo_id).first()
            if repo:
                db.delete(repo)
                db.commit()
                self.repositories = list(db.query(Repository).all())
                self.repo_message = "Repositorio eliminado correctamente"
            else:
                self.repo_message = "Repositorio no encontrado"
        except Exception as e:
            self.repo_message = f"Error al eliminar el repositorio: {str(e)}"
        finally:
            db.close() 