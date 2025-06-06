import reflex as rx

class Repository(rx.Model):
    name: str
    link: str
    image_url: str
    seo_description: str
    seo_keywords: str

class BlogPost(rx.Model):
    title: str
    content: str
    image_url: str 