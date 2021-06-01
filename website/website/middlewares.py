from time import time


class TimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time()
        # ejecutar el request
        response = self.get_response(request)
        print(f'----> response time: {((time() - start_time)*1000):.4f}ms')
        # devolver el response
        return response