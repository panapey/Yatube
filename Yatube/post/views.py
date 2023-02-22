from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Main window')


def group_posts(request, pk):
    return HttpResponse(f'Group number {pk}')
