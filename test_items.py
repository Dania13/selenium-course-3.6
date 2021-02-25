link = "http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/"


def test_item_should_have_button_add_to_basket(browser):
    browser.get(link)
    add_to_card = browser.find_element_by_css_selector("#add_to_basket_form button")
    assert add_to_card.text == "Añadir al carrito", "Button in es should be Añadir al carrito"
