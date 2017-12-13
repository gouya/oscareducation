from django import template
from resources.models import Resource
import json


register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.simple_tag
def get_average_rated_dict(dictionary, key1,key2):
    try:
        r = dictionary[key1].get(key2)
        return float(float(r)*20.0)
    except KeyError:
        return 0.0

@register.simple_tag
def get_average_student(id):
    try:
        resource = Resource.objects.get(pk=id)
    except Resource.DoesNotExist:
        print("Error: Resource with id %d doesn't exist" % id)
        return 0
    student,prof = resource.average()
    return float(student)

@register.simple_tag
def get_average_prof(id):
    try:
        resource = Resource.objects.get(pk=id)
    except Resource.DoesNotExist:
        print("Error: Resource with id %d doesn't exist"%id)
        return 0
    student,prof = resource.average()
    return float(prof)

@register.simple_tag
def owner(u,userother,t,f):
    if u==userother:
        return t
    else:
        return f

@register.filter
def get_json(dictionary):
    return json.dumps(dictionary)

@register.assignment_tag(takes_context=False)
def owns(dict,id):
    try:
        return dict[id].get("voted")
    except KeyError:
        return False
