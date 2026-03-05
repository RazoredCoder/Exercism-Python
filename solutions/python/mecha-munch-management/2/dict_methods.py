"""Functions to manage a users shopping cart items."""


def add_item(current_cart:dict, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
            continue
        current_cart[item] = 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    shopping_cart = {}
    for item in notes:
        shopping_cart[item] = 1
    return shopping_cart


def update_recipes(ideas:dict, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart:dict):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart:dict, aisle_mapping:dict):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fullfilment_cart = {}
    for item in aisle_mapping:
        if item in fullfilment_cart:
            fullfilment_cart[item][0] += 1
            continue
        if item in cart:
            fullfilment_cart[item] = [cart[item], aisle_mapping[item][0], aisle_mapping[item][1]]
    return dict(sorted(fullfilment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart:dict, store_inventory:dict):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item in fulfillment_cart:
        if isinstance(store_inventory[item][0], int):
            store_inventory[item][0] -= fulfillment_cart[item][0]
            if store_inventory[item][0] == 0: store_inventory[item][0] = 'Out of Stock'
    return store_inventory