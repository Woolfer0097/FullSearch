import sys

from geocoder import get_coordinates, get_ll_span
from mapapi import show_map


def param_get_spn():
    toponym_to_find = " ".join(sys.argv[1:])
    ll, spn = get_ll_span(toponym_to_find)
    coordinates = f"ll={ll}&spn={spn}"
    show_map(coordinates, "map")
    show_map(coordinates, "map", add_params=f"pt={ll}")
