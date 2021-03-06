from django.core.cache import cache
from analystic.models import UserIpInfo

def website_static(request):
    online_user = cache.get("online_user", [])
    context = {
        "online_user": len(online_user),
        "total_number": UserIpInfo.objects.count(),
        "recent_users": UserIpInfo.objects.order_by("-id")[:3]
    }
    return context
