from czaSpider.czaTools import *
from .czaBaseItem import czaBaseItem, process_base_item


class Item(czaBaseItem):
    # �˴��̳и��࣬��ָ����Ҫ��չ����
    source = scrapy.Field()


def sourceItem(**kwargs):
    item = Item()
    item.update(process_base_item(**kwargs))

    item["source"] = kwargs.pop('source', None)
    return item
