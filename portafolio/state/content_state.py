"""Estado para manejar el contenido del portafolio."""

import reflex as rx
from typing import List, Dict, Optional
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
    repo_description: str = ""
    repo_url: str = ""
    repo_image_url: str = ""
    repo_message: str = ""
    
    # Listas de contenido
    blog_posts: List[Dict] = []
    repositories: List[Dict] = []
    
    # Estado de edición para blogs
    blog_edit_id: Optional[int] = None
    
    # Estado de edición para repositorios
    repo_edit_id: Optional[int] = None
    
    # Métodos set_ para actualizar los atributos
    def set_blog_title(self, title: str):
        self.blog_title = title

    def set_blog_content(self, content: str):
        self.blog_content = content

    def set_blog_image_url(self, image_url: str):
        self.blog_image_url = image_url

    def set_repo_title(self, title: str):
        self.repo_title = title

    def set_repo_description(self, description: str):
        self.repo_description = description

    def set_repo_url(self, url: str):
        self.repo_url = url

    def set_repo_image_url(self, image_url: str):
        self.repo_image_url = image_url
    
    def load_content(self):
        """Carga el contenido de la base de datos."""
        try:
            db = next(get_db())
            blog_posts = db.query(BlogPost).all()
            repositories = db.query(Repository).all()
            
            # Convertir los objetos a diccionarios
            self.blog_posts = [
                {
                    "id": post.id,
                    "title": post.title,
                    "content": post.content,
                    "image_url": post.image_url,
                }
                for post in blog_posts
            ]
            
            self.repositories = [
                {
                    "id": repo.id,
                    "title": repo.title,
                    "url": repo.url,
                    "image_url": repo.image_url,
                }
                for repo in repositories
            ]
        except Exception as e:
            print(f"Error al cargar el contenido: {str(e)}")
        finally:
            db.close()
    
    def create_blog_post(self):
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
            
            self.blog_posts.append({
                "id": new_post.id,
                "title": new_post.title,
                "content": new_post.content,
                "image_url": new_post.image_url,
            })
            
            # Limpiar el formulario
            self.blog_title = ""
            self.blog_content = ""
            self.blog_image_url = ""
            self.blog_message = "Entrada de blog añadida correctamente"
            
        except Exception as e:
            self.blog_message = f"Error al añadir la entrada: {str(e)}"
        finally:
            db.close()
    
    def create_repository(self):
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
            
            self.repositories.append({
                "id": new_repo.id,
                "title": new_repo.title,
                "url": new_repo.url,
                "image_url": new_repo.image_url,
            })
            
            # Limpiar el formulario
            self.repo_title = ""
            self.repo_description = ""
            self.repo_url = ""
            self.repo_image_url = ""
            self.repo_message = "Repositorio añadido correctamente"
            
        except Exception as e:
            self.repo_message = f"Error al añadir el repositorio: {str(e)}"
        finally:
            db.close()
    
    def delete_blog_post(self, post_id: int):
        """Elimina un post de blog."""
        try:
            db = next(get_db())
            post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
            if post:
                db.delete(post)
                db.commit()
                self.blog_posts = [p for p in self.blog_posts if p["id"] != post_id]
                self.blog_message = "Entrada eliminada correctamente"
            else:
                self.blog_message = "Entrada no encontrada"
        except Exception as e:
            self.blog_message = f"Error al eliminar la entrada: {str(e)}"
        finally:
            db.close()
    
    def delete_repository(self, repo_id: int):
        """Elimina un repositorio."""
        try:
            db = next(get_db())
            repo = db.query(Repository).filter(Repository.id == repo_id).first()
            if repo:
                db.delete(repo)
                db.commit()
                self.repositories = [r for r in self.repositories if r["id"] != repo_id]
                self.repo_message = "Repositorio eliminado correctamente"
            else:
                self.repo_message = "Repositorio no encontrado"
        except Exception as e:
            self.repo_message = f"Error al eliminar el repositorio: {str(e)}"
        finally:
            db.close()

    def start_edit_blog(self, post_id: int):
        """Carga los datos del blog a editar en el formulario."""
        post = next((p for p in self.blog_posts if p["id"] == post_id), None)
        if post:
            self.blog_edit_id = post_id
            self.blog_title = post["title"]
            self.blog_content = post["content"]
            self.blog_image_url = post.get("image_url", "")
            self.blog_message = "Editando entrada de blog"

    def save_edit_blog(self):
        """Guarda los cambios de la entrada de blog editada."""
        if self.blog_edit_id is None:
            self.blog_message = "No hay entrada seleccionada para editar."
            return
        if not all([self.blog_title, self.blog_content]):
            self.blog_message = "El título y el contenido son obligatorios."
            return
        try:
            db = next(get_db())
            post = db.query(BlogPost).filter(BlogPost.id == self.blog_edit_id).first()
            if post:
                post.title = self.blog_title
                post.content = self.blog_content
                post.image_url = self.blog_image_url or None
                db.commit()
                # Actualizar en la lista local
                for p in self.blog_posts:
                    if p["id"] == self.blog_edit_id:
                        p["title"] = self.blog_title
                        p["content"] = self.blog_content
                        p["image_url"] = self.blog_image_url
                        break
                self.blog_message = "Entrada de blog actualizada correctamente"
            else:
                self.blog_message = "Entrada no encontrada para editar"
            # Limpiar el formulario y salir del modo edición
            self.blog_edit_id = None
            self.blog_title = ""
            self.blog_content = ""
            self.blog_image_url = ""
        except Exception as e:
            self.blog_message = f"Error al editar la entrada: {str(e)}"
        finally:
            db.close()

    def start_edit_repo(self, repo_id: int):
        """Carga los datos del repositorio a editar en el formulario."""
        repo = next((r for r in self.repositories if r["id"] == repo_id), None)
        if repo:
            self.repo_edit_id = repo_id
            self.repo_title = repo["title"]
            self.repo_description = repo.get("description", "")
            self.repo_url = repo["url"]
            self.repo_image_url = repo.get("image_url", "")
            self.repo_message = "Editando repositorio"

    def save_edit_repo(self):
        """Guarda los cambios del repositorio editado."""
        if self.repo_edit_id is None:
            self.repo_message = "No hay repositorio seleccionado para editar."
            return
        if not all([self.repo_title, self.repo_url]):
            self.repo_message = "El título y la URL son obligatorios."
            return
        try:
            db = next(get_db())
            repo = db.query(Repository).filter(Repository.id == self.repo_edit_id).first()
            if repo:
                repo.title = self.repo_title
                repo.url = self.repo_url
                repo.image_url = self.repo_image_url or None
                db.commit()
                # Actualizar en la lista local
                for r in self.repositories:
                    if r["id"] == self.repo_edit_id:
                        r["title"] = self.repo_title
                        r["url"] = self.repo_url
                        r["image_url"] = self.repo_image_url
                        break
                self.repo_message = "Repositorio actualizado correctamente"
            else:
                self.repo_message = "Repositorio no encontrado para editar"
            # Limpiar el formulario y salir del modo edición
            self.repo_edit_id = None
            self.repo_title = ""
            self.repo_description = ""
            self.repo_url = ""
            self.repo_image_url = ""
        except Exception as e:
            self.repo_message = f"Error al editar el repositorio: {str(e)}"
        finally:
            db.close()

    @classmethod
    def submit_blog_post(cls, state):
        state.create_blog_post()

    @classmethod
    def submit_repository(cls, state):
        state.create_repository() 