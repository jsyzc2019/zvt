# -*- coding: utf-8 -*-
from zvt.domain import Block, BlockStock, Stock
from zvt.tag.tag_service import build_default_main_tag, build_default_sub_tags
from zvt.tag.tag_utils import build_initial_stock_pool_info, build_initial_main_tag_info, build_initial_sub_tag_info

if __name__ == "__main__":
    # init tag info
    build_initial_stock_pool_info()
    build_initial_main_tag_info()
    build_initial_sub_tag_info()

    Stock.record_data(provider="em")
    Block.record_data(provider="em", sleeping_time=0)
    BlockStock.record_data(provider="em", sleeping_time=0)
    # init default main tag
    build_default_main_tag()

    # init default sub tags
    build_default_sub_tags()
