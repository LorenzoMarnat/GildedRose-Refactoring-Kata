# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item, LegendaryItem, RefinedItem, RefinedItemWithExpiration


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 2, 10),
                 Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(9, items[0].quality)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(8, items[1].quality)
        self.assertEqual(-1, items[1].sell_in)

    def test_aged_brie(self):
        items = [RefinedItem("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_sulfuras(self):
        items = [LegendaryItem("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes(self):
        items = [RefinedItemWithExpiration("Backstage passes to a TAFKAL80ETC concert", 15, 20),
                 RefinedItemWithExpiration("Backstage passes to a TAFKAL80ETC concert", 10, 20),
                 RefinedItemWithExpiration("Backstage passes to a TAFKAL80ETC concert", 5, 20),
                 RefinedItemWithExpiration("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(22, items[1].quality)
        self.assertEqual(4, items[2].sell_in)
        self.assertEqual(23, items[2].quality)
        self.assertEqual(-1, items[3].sell_in)
        self.assertEqual(0, items[3].quality)


if __name__ == '__main__':
    unittest.main()
