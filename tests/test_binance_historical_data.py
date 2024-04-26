from binance_historical_data import BinanceDataDumper


def test_main_class_init():
    # Test BinanceDataDumper initialization with spot data
    data_dumper = BinanceDataDumper(
        path_dir_where_to_dump=".",
        data_type="klines",
        data_frequency="1m",
    )
    assert data_dumper.path_dir_where_to_dump == "."
    assert data_dumper.data_type == "klines"
    assert data_dumper.data_frequency == "1m"

    # Test BinanceDataDumper initialization with futures data
    data_dumper = BinanceDataDumper(
        asset_class="um",
        path_dir_where_to_dump="./BianceFutures",
        data_type="klines",
        data_frequency="1m",
    )
    assert data_dumper.asset_class == "um"
    assert data_dumper.path_dir_where_to_dump == "./BianceFutures"
    assert data_dumper.data_type == "klines"
    assert data_dumper.data_frequency == "1m"


def test_dump_data():
    # Test BinanceDataDumper dump_data method
    data_dumper = BinanceDataDumper(
        path_dir_where_to_dump=".",
        data_type="klines",
        data_frequency="1m",
    )
    data_dumper.dump_data(
        tickers="BTCUSDT",
        date_start=None,
        date_end=None,
        is_to_update_existing=False,
        tickers_to_exclude=["UST"],
    )
    # Add assertions to validate the behavior of the dump_data method
    # based on your specific requirements
