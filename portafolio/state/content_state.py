"""Estado para manejar el contenido del portafolio."""

import reflex as rx
from typing import List, Dict, Optional
from ..models import BlogPost, Repository
from ..database import get_db

class ContentState(rx.State):
    """Estado para manejar el contenido del portafolio."""
    
    content_loaded: bool = False
    
    # Campos para blogs
    blog_title: str = ""
    blog_content: str = ""
    blog_image_url: str = ""
    blog_message: str = ""
    blog_seo_description: str = ""
    
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
    
    # Estado para confirmación de borrado de repositorios
    repo_confirm_delete_id: Optional[int] = None
    
    # Estado para confirmación de borrado de blogs
    blog_confirm_delete_id: Optional[int] = None
    
    # Variables de paginación
    blog_page: int = 1
    repo_page: int = 1
    per_page: int = 10
    blog_no_more: bool = False
    repo_no_more: bool = False
    
    @rx.var
    def selected_post_from_list(self) -> List[Dict]:
        """Filtra la lista de posts para encontrar el que coincide con el post_id de la URL."""
        post_id = self.router.page.params.get("post_id", "")
        if not self.blog_posts or not post_id:
            return []
        return [p for p in self.blog_posts if str(p.get("id")) == post_id]
    
    # Métodos set_ para actualizar los atributos
    def set_blog_title(self, title: str):
        self.blog_title = title

    def set_blog_content(self, content: str):
        self.blog_content = content

    def set_blog_image_url(self, image_url: str):
        self.blog_image_url = image_url

    def set_blog_seo_description(self, seo_description: str):
        self.blog_seo_description = seo_description

    def set_repo_title(self, title: str):
        self.repo_title = title

    def set_repo_description(self, description: str):
        self.repo_description = description

    def set_repo_url(self, url: str):
        self.repo_url = url

    def set_repo_image_url(self, image_url: str):
        self.repo_image_url = image_url
    
    def load_content(self, page: int = 1, per_page: int = 10, append: bool = False, tipo: str = "all"):
        """Carga el contenido de la base de datos de forma paginada y optimizada."""
        try:
            db = next(get_db())
            if tipo in ("all", "blog"):
                blog_posts = (
                    db.query(BlogPost.id, BlogPost.title, BlogPost.image_url, BlogPost.seo_description, BlogPost.created_at)
                    .order_by(BlogPost.created_at.desc())
                    .limit(per_page)
                    .offset((page - 1) * per_page)
                    .all()
                )
                nuevos_blogs = [
                    {
                        "id": int(post.id) if post.id is not None else None,
                        "title": post.title,
                        "image_url": post.image_url,
                        "seo_description": post.seo_description,
                        "created_at": post.created_at.isoformat() if post.created_at else None,
                    }
                    for post in blog_posts
                ]
                if append:
                    self.blog_posts += nuevos_blogs
                else:
                    self.blog_posts = nuevos_blogs
                self.blog_no_more = len(nuevos_blogs) < per_page
            if tipo in ("all", "repo"):
                repositories = (
                    db.query(Repository.id, Repository.title, Repository.url, Repository.description, Repository.image_url, Repository.created_at)
                    .order_by(Repository.created_at.desc())
                    .limit(per_page)
                    .offset((page - 1) * per_page)
                    .all()
                )
                nuevos_repos = [
                    {
                        "id": repo.id,
                        "title": repo.title,
                        "url": repo.url,
                        "description": repo.description,
                        "image_url": repo.image_url,
                        "created_at": repo.created_at.isoformat() if repo.created_at else None,
                    }
                    for repo in repositories
                ]
                if append:
                    self.repositories += nuevos_repos
                else:
                    self.repositories = nuevos_repos
                self.repo_no_more = len(nuevos_repos) < per_page
        except Exception as e:
            print(f"Error al cargar el contenido: {str(e)}")
        finally:
            self.content_loaded = True
            db.close()

    def load_more_blogs(self):
        if not self.blog_no_more:
            self.blog_page += 1
            self.load_content(page=self.blog_page, per_page=self.per_page, append=True, tipo="blog")

    def load_more_repos(self):
        if not self.repo_no_more:
            self.repo_page += 1
            self.load_content(page=self.repo_page, per_page=self.per_page, append=True, tipo="repo")
    
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
                image_url=self.blog_image_url or None,
                seo_description=self.blog_seo_description or None
            )
            db.add(new_post)
            db.commit()
            db.refresh(new_post)
            
            self.blog_posts.append({
                "id": int(new_post.id) if new_post.id is not None else None,
                "title": new_post.title,
                "content": new_post.content,
                "image_url": new_post.image_url,
                "seo_description": new_post.seo_description,
            })
            
            # Limpiar el formulario
            self.blog_title = ""
            self.blog_content = ""
            self.blog_image_url = ""
            self.blog_seo_description = ""
            self.blog_message = "Entrada de blog añadida correctamente"
            # Recargar la lista completa para asegurar sincronización
            self.load_content()
            
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
                description=self.repo_description,
                image_url=self.repo_image_url
            )
            db.add(new_repo)
            db.commit()
            db.refresh(new_repo)
            self.repositories.append({
                "id": new_repo.id,
                "title": new_repo.title,
                "url": new_repo.url,
                "description": new_repo.description,
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
            self.blog_seo_description = post.get("seo_description", "")
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
                post.seo_description = self.blog_seo_description or None
                db.commit()
                # Actualizar en la lista local
                for p in self.blog_posts:
                    if p["id"] == self.blog_edit_id:
                        p["title"] = self.blog_title
                        p["content"] = self.blog_content
                        p["image_url"] = self.blog_image_url
                        p["seo_description"] = self.blog_seo_description
                        break
                self.blog_message = "Entrada de blog actualizada correctamente"
            else:
                self.blog_message = "Entrada no encontrada para editar"
            # Limpiar el formulario y salir del modo edición
            self.blog_edit_id = None
            self.blog_title = ""
            self.blog_content = ""
            self.blog_image_url = ""
            self.blog_seo_description = ""
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
                repo.description = self.repo_description
                repo.image_url = self.repo_image_url
                db.commit()
                # Actualizar en la lista local
                for r in self.repositories:
                    if r["id"] == self.repo_edit_id:
                        r["title"] = self.repo_title
                        r["url"] = self.repo_url
                        r["description"] = self.repo_description
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

    def confirm_delete_repository(self, repo_id: int):
        """Marca un repositorio para confirmación de borrado."""
        self.repo_confirm_delete_id = repo_id

    def cancel_delete_repository(self):
        """Cancela la confirmación de borrado."""
        self.repo_confirm_delete_id = None

    def delete_and_reset_repository(self, repo_id: int):
        """Borra el repositorio y limpia la confirmación."""
        self.delete_repository(repo_id)
        self.repo_confirm_delete_id = None

    def submit_repository(self, form_data=None):
        if self.repo_edit_id is not None:
            self.save_edit_repo()
        else:
            self.create_repository()

    def confirm_delete_blog(self, post_id: int):
        """Establece el ID del blog a borrar."""
        self.blog_confirm_delete_id = post_id

    def cancel_delete_blog(self):
        """Cancela la confirmación de borrado de blog."""
        self.blog_confirm_delete_id = None

    def delete_and_reset_blog(self, post_id: int):
        """Elimina el blog y resetea el estado de confirmación."""
        self.delete_blog_post(post_id)
        self.cancel_delete_blog() 