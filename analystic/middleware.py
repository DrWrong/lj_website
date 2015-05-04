from analystic.models import UserIpInfo
from django.core.cache import cache
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ObjectDoesNotExist


class IpAnalysticMiddleware(object):

    def process_request(self, request):
        ip = self.get_ip_address(request)
        try:
            UserIpInfo.objects.filter(
                visit_time__gte=timezone.now() - timedelta(minutes=5)
            ).get(ip_address=ip)
        except ObjectDoesNotExist:
            UserIpInfo.objects.create(ip_address=ip)

    def get_ip_address(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class OnlineMemberMiddleware(object):

    def process_request(self, request):
        session_key = request.session.session_key
        online_user = cache.get("online_user", [])
        if session_key not in online_user:
            online_user.append(session_key)
        cache.set("online_user",  online_user, 60 * 5)
