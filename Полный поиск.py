import sys

from geocoder import get_coordinates, get_ll_span
from mapapi import show_map


def main():
    toponym_to_find = " ".join(sys.argv[1:])
    longitude, lattitude = get_coordinates(toponym_to_find)
    ll = get_ll_span(f"ll={longitude},{lattitude}&spn=0.005,0.005")
    show_map(ll, "map")


if __name__ == '__main__':
    main()
