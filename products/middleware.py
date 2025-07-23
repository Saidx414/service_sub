from django.http import JsonResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed


from subscriptions.models import UserSubscription


class CheckSubscriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.basic_auth = BasicAuthentication()

    def __call__(self, request):
        path = request.path

        if path.startswith('/api/orders/'):
            try:
                auth_result = self.basic_auth.authenticate(request)
                if auth_result is None:
                    return JsonResponse({'detail': 'Пользователь не авторизован'}, status=401)

                user, auth = auth_result
                request.user = user

            except AuthenticationFailed:
                return JsonResponse({'detail': 'Неверные учётные данные'}, status=401)

            try:
                subscription = UserSubscription.objects.get(user=user)
                if not subscription.is_active:
                    return JsonResponse({'detail': 'Подписка неактивна'}, status=403)
            except UserSubscription.DoesNotExist:
                return JsonResponse({'detail': 'Подписка отсутствует'}, status=403)

        return self.get_response(request)