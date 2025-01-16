from src.RequestGenerator.CategoryEnum import Category
from src.RequestGenerator.ColorEnum import Color
from src.RequestGenerator.StateEnum import State


class SearchUrl:

    url = "https://www.olx.ua/uk/moda-i-stil/"
    queries = ""
    category = ""

    def __init__(self, search_query: str):
        self.queries = f"q-{search_query}/?currency=UAH"

    def add_price_from(self, price_from: int):
        self.queries += f"&search[filter_float_price:from]={price_from}"

    def add_price_to(self, price_to: int):
        self.queries += f"&search[filter_float_price:to]={price_to}"

    def add_state(self, state: State):
        if state == State.used:
            self.queries += "&search[filter_enum_state][0]=used"
        elif state == State.new:
            self.queries += "&search[filter_enum_state][0]=new"

    def add_category(self, category: Category):
        self.category += category.value

    def add_color(self, color: Color):
        self.queries += color.value

    def get_url(self):
        return f"{self.url}{self.category}{self.queries}"


if __name__ == "__main__":
    # example
    var = SearchUrl("кросівки")
    var.add_state(State.new)
    var.add_category(Category.men_footwear)
    var.add_price_from(500)
    var.add_price_to(5000)
    var.add_color(Color.black)
    var.add_color(Color.pink)
    print(var.get_url())

