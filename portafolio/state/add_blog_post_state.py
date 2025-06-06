"""Estado para añadir entradas de blog."""

import reflex as rx
from portafolio.models import BlogPost


class AddBlogPostState(rx.State):
    """Define el estado para añadir entradas de blog."""
    title: str = ""
    content: str = ""
    image_url: str = ""
    error_message: str = ""

    def handle_submit(self, form_data: dict):
        """Maneja el envío del formulario para añadir una entrada de blog."""
        self.title = form_data.get("title", "")
        self.content = form_data.get("content", "")
        self.image_url = form_data.get("image_url", "")
        
        try:
            new_blog_post = BlogPost(
                title=self.title,
                content=self.content,
                image_url=self.image_url
            )
            
            with rx.session() as session:
                session.add(new_blog_post)
                session.commit()
                self.title = ""
                self.content = ""
                self.image_url = ""
                return rx.redirect("/blog")
        except Exception as e:
            self.error_message = f"Error al añadir la entrada de blog: {str(e)}" 