class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if self.quality > 0:
            self.quality -= 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality -= 1


class LegendaryItem(Item):
    def update_quality(self):
        pass  # Legendary items do not change in quality or sell_in


class RefinedItem(Item):
    def update_quality(self):
        # Refined items increase in quality over time
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality += 1


class RefinedItemWithExpiration(RefinedItem):
    def update_quality(self):
        # Refined items increase in quality over time, but degrade after expiration
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality += 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0  # Quality drops to 0 after expiration
