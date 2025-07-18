from django.http import JsonResponse
from subscriptions.models import UserSubscription
from django.contrib.auth import get_user_model


User = get_user_model()

class CheckSubscriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        path = request.path
        if path.startswith('/api/orders/'):
            user_id = request.headers.get('X-User-ID')

            if not user_id:
                return JsonResponse({'detail': 'Не передан X-User-ID'}, status=400)

            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return JsonResponse({'detail': 'Пользователь не найден'}, status=404)

            try:
                subscription = UserSubscription.objects.get(user=user)
                if not subscription.is_active:
                    return JsonResponse({'detail': 'Подписка неактивна'}, status=403)
            except UserSubscription.DoesNotExist:
                return JsonResponse({'detail': 'Подписка отсутствует'}, status=403)

        return self.get_response(request)
