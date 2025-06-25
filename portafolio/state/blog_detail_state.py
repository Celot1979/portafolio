import reflex as rx
from portafolio.models import BlogPost
from portafolio.database import get_db

class BlogDetailState(rx.State):
    selected_post: dict = {}
    error_message: str = ""

    @rx.var
    def has_post(self) -> bool:
        return bool(self.selected_post)

    def load_post(self, id):
        self.error_message = f"Intentando cargar post con id: {id}"
        try:
            db = next(get_db())
            post_id = int(id) if id is not None else None
            print(f"[DEBUG] Buscando post con id: {post_id}")
            post = db.query(BlogPost).filter(BlogPost.id == post_id).first()
            print(f"[DEBUG] Post encontrado: {post}")
            if post:
                self.selected_post = {
                    "id": post.id,
                    "title": post.title,
                    "content": post.content,
                    "image_url": post.image_url,
                }
                self.error_message = ""
            else:
                self.selected_post = {}
                self.error_message = "Entrada de blog no encontrada."
        except Exception as e:
            self.selected_post = {}
            self.error_message = f"Error al cargar la entrada: {str(e)}"
        finally:
            db.close()

    def set_error_message(self, msg: str):
        self.error_message = msg 