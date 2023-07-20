"""_summary_x
"""

from collections import namedtuple
from math import asin, cos, radians, sin, sqrt


def haversine(ϕ1, λ1, ϕ2, λ2):
    earth_radius_km = 6371

    return 2 * earth_radius_km * asin(
        sqrt(
            sin((ϕ2 - ϕ1) / 2) ** 2
            + cos(ϕ1) * cos(ϕ2) * sin((λ2 - λ1) / 2) ** 2
        )
    )


def print_dist(loc_1, loc_2):
    ϕ1, λ1 = radians(loc_1.x), radians(loc_1.y)
    ϕ2, λ2 = radians(loc_2.x), radians(loc_2.y)
    print(f"Distance between {loc_1.name} and {loc_2.name}: {haversine(ϕ1, λ1, ϕ2, λ2):.2f} km")


def main():
    Location = namedtuple("Location", "name x y")

    san_fran = Location("San Fransisco", 37.8, 122.4)
    ny = Location("New York", 40.7, 74.)
    munich = Location("Munich", 48.1, 11.6)
    amsterdam = Location("Amsterdam", 52.4, 4.9)
    bcn = Location("Barcelona", 41.4, 2.2)
    cornwall_uk = Location("Cornwall UK", 50.3, 5.1)
    cph = Location("Copenhagen DK", 55.7, 12.6)

    print_dist(san_fran, ny)
    print_dist(cph, bcn)


if __name__ == "__main__":
    main()
