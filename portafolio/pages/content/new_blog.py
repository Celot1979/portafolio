"""Página para crear un nuevo post de blog."""

import reflex as rx
from ...components.menu import menu
from ...state.content_state import ContentState
from ...state.login_state import LoginState

def new_blog_page():
    """Página para crear un nuevo post de blog."""
    # Estado local para la confirmación de borrado
    confirm_delete_id = rx.var(None)

    def render_blog(post):
        return rx.vstack(
            rx.heading(
                post.get("title", ""),
                as_="h3",
                font_size=["1.2em", "1.3em", "1.5em"],
                color="white",
                font_family="sans-serif",
                width="100%",
                word_wrap="break-word"
            ),
            rx.markdown(
                post.get("content", ""),
                color="white",
                font_family="sans-serif",
                width="100%",
                font_size=["0.9em", "1em", "1em"]
            ),
            rx.cond(
                post.get("image_url"),
                rx.image(
                    src=post.get("image_url", ""),
                    alt=post.get("title", ""),
                    width="100%",
                    height="auto",
                    border_radius="lg"
                )
            ),
            rx.cond(
                ContentState.blog_edit_id == post["id"],
                rx.text("Editando esta entrada", color="yellow"),
                None
            ),
            rx.cond(
                ContentState.blog_confirm_delete_id == post["id"],
                rx.hstack(
                    rx.text("¿Seguro que quieres borrar esta entrada?", color="red"),
                    rx.button(
                        "Confirmar",
                        color_scheme="red",
                        on_click=lambda: ContentState.delete_and_reset_blog(post["id"]),
                        size="2"
                    ),
                    rx.button(
                        "Cancelar",
                        color_scheme="gray",
                        on_click=ContentState.cancel_delete_blog,
                        size="2"
                    ),
                    spacing="2"
                ),
                rx.hstack(
                    rx.button(
                        "Borrar",
                        color_scheme="red",
                        on_click=lambda: ContentState.confirm_delete_blog(post["id"]),
                        size="2"
                    ),
                    rx.button(
                        "Modificar",
                        color_scheme="yellow",
                        on_click=lambda: ContentState.start_edit_blog(post["id"]),
                        size="2"
                    ),
                    spacing="2"
                )
            ),
            spacing="2",
            width="100%",
            padding_y=["2", "3"],
            padding_x=["2", "3"],
            background_color="#232526",
            border_radius="md",
            margin_bottom="1em"
        )

    return rx.vstack(
        menu(),
        rx.hstack(
            rx.spacer(),
            rx.button(
                "Cerrar sesión",
                on_click=LoginState.logout,
                color_scheme="red",
                mr="2"
            ),
            rx.link(
                rx.button(
                    "Gestor de contenido",
                    color_scheme="blue"
                ),
                href="/content-manager"
            ),
            mt="2",
            width="100%"
        ),
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading("Nuevo Post de Blog", size="7", color="white", mb="1.5em", text_align="center"),
                    rx.form(
                        rx.vstack(
                            rx.input(
                                placeholder="Título",
                                id="title",
                                mb="4",
                                width="100%",
                                value=ContentState.blog_title,
                                on_change=ContentState.set_blog_title,
                                size="3"
                            ),
                            rx.input(
                                placeholder="URL de la imagen (opcional)",
                                id="image_url",
                                mb="4",
                                width="100%",
                                value=ContentState.blog_image_url,
                                on_change=ContentState.set_blog_image_url,
                                size="3"
                            ),
                            rx.text_area(
                                placeholder="Descripción SEO (máx. 160 caracteres)",
                                id="seo_description",
                                mb="4",
                                width="100%",
                                value=ContentState.blog_seo_description,
                                on_change=ContentState.set_blog_seo_description,
                                size="3",
                                max_length=160
                            ),
                            rx.text("""
Puedes usar **Markdown** para dar formato al contenido:
- **Negrita**: `**texto**`
- *Cursiva*: `*texto*`
- __Subrayado__: `<u>texto</u>`
- [Enlace](https://reflex.dev): `[texto](url)`
- ![Imagen](https://url.com/img.png): `![alt](url)`
- > Cita: `> texto`
- Listas: `- item1\n- item2`
""", color="gray", font_size="0.9em", mb="2"),
                            rx.text_area(
                                placeholder="Contenido (usa Markdown para formato)",
                                id="content",
                                mb="4",
                                width="100%",
                                value=ContentState.blog_content,
                                on_change=ContentState.set_blog_content,
                                size="3"
                            ),
                            rx.button(
                                rx.cond(
                                    (ContentState.blog_edit_id is not None) & (ContentState.blog_posts.length() > 0),
                                    "Guardar cambios",
                                    "Guardar entrada"
                                ),
                                type_="submit",
                                color_scheme="blue",
                                size="3",
                                width="100%",
                                mt="2",
                                is_disabled=rx.cond(
                                    (ContentState.blog_edit_id is not None) & (ContentState.blog_posts.length() == 0),
                                    True,
                                    False
                                )
                            ),
                            align_items="center",
                            spacing="4",
                            width="100%"
                        ),
                        on_submit=rx.cond(
                            (ContentState.blog_edit_id is not None) & (ContentState.blog_posts.length() > 0),
                            ContentState.save_edit_blog,
                            ContentState.create_blog_post
                        ),
                        width="100%"
                    ),
                    rx.text(ContentState.blog_message, color="red", mt="2"),
                    rx.divider(margin_y="2"),
                    rx.heading("Entradas subidas", size="6", color="white", mb="1em", text_align="center"),
                    rx.cond(
                        ContentState.blog_posts,
                        rx.foreach(ContentState.blog_posts, render_blog),
                        rx.text("No hay entradas guardadas.", color="white")
                    ),
                    spacing="4",
                    align_items="center",
                    width="100%"
                ),
                background="#18181b",
                border_radius="xl",
                box_shadow="0 8px 32px rgba(0,0,0,0.35)",
                p="8",
                max_width="600px",
                width="100%",
                mt="4"
            ),
            width="100%",
            min_height="calc(100vh - 64px)",
            align_items="center",
            justify_content="center"
        ),
        width="100%",
        min_height="100vh",
        background_color="#111"
    ) 