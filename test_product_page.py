from .pages.product_page import ProductPage
import pytest

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
xfail = 7
urls = [product_link+"{no}" for no in range(10) if no!= xfail]
xlink = pytest.param(product_link+str(xfail), marks=pytest.mark.xfail(reason="mistake on page"))
urls.insert(xfail, xlink)

@pytest.mark.parametrize('link', urls)

def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()             
    page.add_product_to_basket()
