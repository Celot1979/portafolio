"""Estado para la página de proyectos."""

import reflex as rx

class ProyectosState(rx.State):
    """Estado para la página de proyectos."""

    repositories: list = []

    @staticmethod
    def load_repositories():
        # Datos de ejemplo como diccionarios
        ProyectosState.repositories = [
            {"name": "Repo 1", "description": "Descripción del repo 1", "url": "https://github.com/usuario/repo1"},
            {"name": "Repo 2", "description": "Descripción del repo 2", "url": "https://github.com/usuario/repo2"},
        ] 