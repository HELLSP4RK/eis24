import json

from django.db.models import Max, Count
from django.http import HttpResponse

from first.models import Action


def show_actions_group_by_user(request):
    actions_queryset = Action.objects.values('session__user__number', 'type')\
        .annotate(last=Max('created_at'), count=Count('type')).order_by('session__user__number')

    data, numbers = [], []
    for action in actions_queryset:
        number = action['session__user__number']
        actions = {
            'type': action['type'],
            'last': action['last'].isoformat(),
            'count': action['count'],
        }
        if number not in numbers:
            data.append({
                'number': number,
                'actions': [actions]
            })
            numbers.append(number)
        else:
            data[-1]['actions'].append(actions)

    return HttpResponse(json.dumps(data), content_type="application/json")
