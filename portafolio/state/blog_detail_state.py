import reflex as rx
from portafolio.models import BlogPost
from portafolio.database import get_db

class BlogDetailState(rx.State):
    selected_post: dict = {}
    error_message: str = ""

    @rx.var
    def has_post(self) -> bool:
        return bool(self.selected_post)

    def load_post(self, post_id):
        print(f"[DEBUG] load_post llamado con post_id: {post_id}")
        self.error_message = f"Intentando cargar post con id: {post_id}"
        try:
            db = next(get_db())
            print(f"[DEBUG] Buscando post con id convertido: {post_id}")
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
            print(f"[DEBUG] Excepción en load_post: {e}")
            self.selected_post = {}
            self.error_message = f"Error al cargar la entrada: {str(e)}"
        finally:
            db.close()

    def set_error_message(self, msg: str):
        self.error_message = msg

    def load_post_from_state(self):
        post_id = int(str(rx.State.post_id))
        self.load_post(post_id)

    def load_post_from_state(self):
        self.load_post(rx.State.post_id) 