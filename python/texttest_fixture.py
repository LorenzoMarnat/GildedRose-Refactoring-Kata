# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import GildedRose
from item import Item, LegendaryItem, RefinedItem, RefinedItemWithExpiration


def main():
    print("OMGHAI!")
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        RefinedItem(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        LegendaryItem(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        LegendaryItem(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        RefinedItemWithExpiration(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        RefinedItemWithExpiration(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        RefinedItemWithExpiration(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]
    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()


if __name__ == "__main__":
    main()
