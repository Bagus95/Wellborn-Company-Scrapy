from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Wellborncompany(BasePortiaSpider):
    name = "www.wellborncompany.com"
    allowed_domains = [u'www.wellborncompany.com']
    start_urls = [
        u'https://www.wellborncompany.com/product-category/men/jackets/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PortiaItem,
                   None,
                   u'#wbrn-product-20497 > .woocommerce-LoopProduct-link',
                   [Field(u'IMAGE',
                          '.attachment-shop_catalog::attr(src)',
                          []),
                       Field(u'NAME',
                             'h3 *::text',
                             []),
                       Field(u'PRICE',
                             '.price > .woocommerce-Price-amount *::text',
                             [])])]]
