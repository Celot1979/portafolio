"""Estado para la página de blog."""

import reflex as rx
from typing import List
from portafolio.models import BlogPost


class BlogState(rx.State):
    """Estado para la página de blog."""

    blog_posts: List[BlogPost] = []

    @staticmethod
    def load_blog_posts():
        """Carga las entradas del blog de la base de datos."""
        BlogState.blog_posts = BlogPost.query.all() 