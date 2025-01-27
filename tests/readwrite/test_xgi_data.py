import pytest

from xgi import load_xgi_data
from xgi.exception import XGIError


@pytest.mark.webtest
@pytest.mark.slow
def test_load_xgi_data():
    H = load_xgi_data("email-enron")
    assert H.num_nodes == 148
    assert H.num_edges == 10885
    assert H["name"] == "email-Enron"
    assert H.nodes["4"]["name"] == "robert.badeer@enron.com"
    assert H.edges["0"]["timestamp"] == "2000-01-11T10:29:00"

    H2 = load_xgi_data("email-enron", max_order=2)
    assert len(H2.edges.filterby("order", 2, mode="gt")) == 0
    assert len(H.edges.filterby("order", 2, mode="gt")) == 1283

    with pytest.raises(XGIError):
        load_xgi_data("test")
