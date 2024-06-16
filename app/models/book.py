from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    __odm_config__ = {"collection": "books"}
