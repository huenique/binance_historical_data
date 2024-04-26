========================
binance_historical_data
========================

.. image:: https://img.shields.io/github/last-commit/huenique/binance_historical_data
   :target: https://img.shields.io/github/last-commit/huenique/binance_historical_data
   :alt: GitHub last commit

.. image:: https://img.shields.io/github/license/huenique/binance_historical_data
    :target: https://github.com/huenique/binance_historical_data/blob/master/LICENSE.txt
    :alt: GitHub license<space><space>

.. image:: https://img.shields.io/pypi/v/binance_historical_data
   :target: https://img.shields.io/pypi/v/binance_historical_data
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/binance_historical_data
   :target: https://img.shields.io/pypi/pyversions/binance_historical_data
   :alt: PyPI - Python Version


.. contents:: **Table of Contents**

Overview
=========================
`binance_historical_data` is a Python package designed to simplify the download of historical cryptocurrency data (prices and volumes) from the Binance server. Notably, you can download all historical data without needing an account on binance.com.

Data is sourced from Binance Data Vision, where it is dumped locally and unzipped, providing you with a ready-to-use local copy.

Using this package, you can access comprehensive historical data on prices and volumes with just three lines of Python code. Additionally, updating already downloaded data requires only another three lines of code.

Limitations: Data from the previous day is only available on the Binance server a few minutes after 0:00 AM UTC, which introduces a delay in data availability.

Installation via pip:
======================

.. code-block:: bash

    pip install binance_historical_data

How to use it
===========================

Initialize main object: **data_dumper**
---------------------------------------------

.. code-block:: python

    from binance_historical_data import BinanceDataDumper

    data_dumper = BinanceDataDumper(
        path_dir_where_to_dump=".",
        asset_class="spot",  # spot, um, cm
        data_type="klines",  # aggTrades, klines, trades
        data_frequency="1m",
    )

Arguments:

#. **path_dir_where_to_dump**:
    | (string) Path to folder where to dump the data
#. **asset_class**:
    | (string) Source of data: [spot, um, cm] um: usd(t) margined futures, cm: coin margined futures
#. **data_type="klines"**:
    | (string) data type to dump:
    | [aggTrades, klines, trades] for spot
    | [aggTrades, klines, trades, indexPriceKlines, markPriceKlines, premiumIndexKlines, metrics] for futures (metrics only supported for um)
    | Refer to binance doc for additional info: https://github.com/binance/binance-public-data
#. **str_data_frequency**:
    | (string) One of [1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h]
    | Frequency of price-volume data candles to get

1) The only method to dump the data
------------------------------------------

.. code-block:: python

    data_dumper.dump_data(
        tickers=None,
        date_start=None,
        date_end=None,
        is_to_update_existing=False,
        tickers_to_exclude=["UST"],
    )

Arguments:

#. **tickers=None**:
    | (list) Trading pairs for which to dump data
    | *if equals to None* - all **USDT** pairs will be used
#. **date_start=None**:
    | (datetime.date) The date from which to start dump
    | *if equals to None* - every trading pair will be dumped from the early begining (the earliest is 2017-01-01)
#. **date_end=True=None**:
    | (datetime.date) The last date for which to dump data
    | *if equals to None* - Today's date will be used
#. **is_to_update_existing=False**:
    | (bool) Flag if you want to update the data if it's already exist
#. **tickers_to_exclude=None**:
    | (list) Tickers to exclude from dump


2) Delete outdated daily results
----------------------------------------------------

Deleta all daily data for which full month monthly data was already dumped

.. code-block:: python

    data_dumper.delete_outdated_daily_results()

.csv klines (candles) files columns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| "Open time" - Timestamp
| "Open"
| "High"
| "Low"
| "Close"
| "Volume"
| "Close time" - Timestamp
| "Quote asset volume"
| "Number of trades"
| "Taker buy base asset volume"
| "Taker buy quote asset volume"
| "Ignore"

Examples
===========================

How to dump all data for all USDT trading pairs
------------------------------------------------

Please be advised that the first data dump for all trading pairs might take some time (~40 minutes)

.. code-block:: python

    data_dumper.dump_data()

How to update data (get all new data)
----------------------------------------------

| It's as easy as running the exactly same method **dump_data** once again
| The **data_dumper** will find all the dates for which data already exists
| and will try to dump only the new data

.. code-block:: python

    data_dumper.dump_data()

How to update (reload) data for the asked time period
----------------------------------------------------------

.. code-block:: python

    data_dumper.dump_data(
        date_start=datetime.date(year=2021, month=1, day=1),
        date_end=datetime.date(year=2022, month=1, day=1),
        is_to_update_existing=True
    )

Other useful methods
===========================

Get all trading pairs (tickers) from binance
----------------------------------------------------

.. code-block:: python

    print(data_dumper.get_list_all_trading_pairs())


Get the first data when data for the ticker can be found
----------------------------------------------------------

.. code-block:: python

    print(data_dumper.get_min_start_date_for_ticker())


Get all tickers with locally saved data
----------------------------------------------------

.. code-block:: python

    print(
        data_dumper.get_all_tickers_with_data(timeperiod_per_file="daily")
    )


Get all dates for which there is locally saved data
----------------------------------------------------

.. code-block:: python

    print(
        data_dumper.get_all_dates_with_data_for_ticker(
            ticker,
            timeperiod_per_file="monthly"
        )
    )

Get directory where the local data of exact ticker lies
--------------------------------------------------------

.. code-block:: python

    print(
        data_dumper.get_local_dir_to_data(
            ticker,
            timeperiod_per_file,
        )
    )

Create file name for the local file
----------------------------------------------------

.. code-block:: python

    print(
        data_dumper.create_filename(
            ticker,
            date_obj,
            timeperiod_per_file="monthly",
        )
    )

Links
=====

    * `PYPI <https://pypi.org/project/binance_historical_data/>`_
    * `GitHub <https://github.com/stas-prokopiev/binance_historical_data>`_

Project local Links
===================

    * `CHANGELOG <https://github.com/stas-prokopiev/binance_historical_data/blob/master/CHANGELOG.rst>`_.
    * `CONTRIBUTING <https://github.com/stas-prokopiev/binance_historical_data/blob/master/CONTRIBUTING.rst>`_.

Contacts
========

    * Email: stas.prokopiev@gmail.com
    * `vk.com <https://vk.com/stas.prokopyev>`_
    * `Facebook <https://www.facebook.com/profile.php?id=100009380530321>`_

License
=======

This project is licensed under the MIT License.