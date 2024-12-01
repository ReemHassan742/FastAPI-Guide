from models import MenuItem, Order, Review 

menu = [
    MenuItem(id=1, name="Espresso", price=2.7 , description="Strong black coffee."),
    MenuItem(id=2, name="Cappuccino", price=3.5 , description="An espresso-based coffee drink that is traditionally prepared with steamed milk including a layer of milk."),
    MenuItem(id=3, name="Latte", price=3.3 , description="Is a coffee drink of Italian origin made with espresso and steamed milk, traditionally served in a glass. "),
    MenuItem(id=4, name="Guillermo", price=4 , description="Originally one or two shots of hot espresso poured over slices of lime. It can also be served on ice, sometimes with a touch of milk.")
]

orders = []

reviews = []

print(menu, orders, reviews)
