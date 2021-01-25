import requests # noqa

from celery import chain, shared_task # noqa
from home.models import Currency # noqa


@shared_task
def currency_load():

    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5') # noqa
    return response.json()


@shared_task
def currency_save(currency):
    for line in currency:
        new_currency = Currency()
        new_currency.ccy = line['ccy']
        new_currency.base_ccy = line['base_ccy']
        new_currency.buy = line['buy']
        new_currency.sale = line['sale']

        new_currency.save()


@shared_task
def private_bank():
    return chain(currency_load.s(), currency_save.s())()
