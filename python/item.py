class Item:
    quality_evolution = -1

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = max(0, min(50, value))

    def update_quality(self):
        self.quality += self.quality_evolution
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality += self.quality_evolution


class LegendaryItem(Item):
    @Item.quality.setter
    def quality(self, value):
        self._quality = 80  # Legendary items always have quality of 80

    def update_quality(self):
        pass  # Legendary items do not change in quality or sell_in


class RefinedItem(Item):
    quality_evolution = 1  # Refined items increase in quality over time


class RefinedItemWithExpiration(RefinedItem):
    def update_quality(self):
        # Refined items increase in quality over time, but degrade after expiration
        self.quality_evolution = 1 + \
            int(self.sell_in <= 10) + int(self.sell_in <= 5)
        super().update_quality()
        if self.sell_in < 0:
            self.quality = 0  # Quality drops to 0 after expiration


class ConjuredItem(Item):
    # Conjured items degrade in quality twice as fast
    quality_evolution = Item.quality_evolution * 2
