import logging
import uuid

from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):

    logging.basicConfig(level=logging.INFO)
    def process_request(self, request):
        # процесинг запроса
        resolved_path_info = resolve(request.path_info)
        logging.info(
            'Request %s View name %s route %s',
            request, resolved_path_info.view_name, resolved_path_info.route)

    def process_response(self, request, response):
        # процесинг ответа
        logging.info('For request %s response %s', request, response)
        return response


class RawDataMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.META['id_request'] = uuid.uuid4().hex
        logging.info(request.META['id_request'])


class IdentifyResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        response['id_request'] = request.META['id_request']
        logging.info('Request hash is %s', response['id_request'])
        return response


