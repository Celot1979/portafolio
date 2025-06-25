import reflex as rx

class BlogPageState(rx.State):
    modal_open: bool = False
    selected_post: dict = None

    def open_modal(self, post: dict):
        self.selected_post = post
        self.modal_open = True

    def close_modal(self):
        self.modal_open = False
        self.selected_post = None 