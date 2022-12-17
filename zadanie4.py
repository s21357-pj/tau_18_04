class XmasSong:
    days = ['zero', 'first', 'second', 'third', 'fourth',
            'fifth', 'sixth', 'seventh', 'eighth',
            'ninth', 'tenth', 'eleventh', 'twelfth']
    data = {
        'first': 'a Partridge in a Pear Tree',
        'second': 'two Turtle Doves',
        'third': 'three French Hens',
        'fourth': 'four Calling Birds',
        'fifth': 'five Gold Rings',
        'sixth': 'six Geese-a-Laying',
        'seventh': 'seven Swans-a-Swimming',
        'eighth': 'eight Maids-a-Milking',
        'ninth': 'nine Ladies Dancing',
        'tenth': 'ten Lords-a-Leaping',
        'eleventh': 'eleven Pipers Piping',
        'twelfth': 'twelve Drummers Drumming'
    }

    def get_line(self, day):
        gifts = []
        try:
            for item in range(0, day):
                gifts.append(self.data[self.days[item+1]])
            if self.data[self.days[day]] and day > 1:
                gifts[0] = "and %s" % (gifts[0])
            result = "On the %s day of Christmas my true love gave " \
                     "to me: %s." % (self.days[day], ', '.join(gifts[::-1]))
        except Exception:
            raise ValueError("Out of range")
        return result

    def get_range(self, day_start, day_end):
        lines = []
        if day_start <= day_end:
            for item in range(day_start, day_end+1):
                lines.append(self.get_line(item))
            return '\n\n'.join(lines)
        raise ValueError("Out of range")

    def get_all(self):
        return self.get_range(1, 12)
