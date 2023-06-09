
from prometheus_client import Counter
from prometheus_client import  Counter
from django.http import HttpResponse
from django.template import loader

# Counter metriği oluşturma
index_requests_total = Counter('index_requests_total', 'Total number of index requests')

def index(request):
    # Counter metriğini artırma
    index_requests_total.inc()
    index_requests_total._get_metric()
    print(index_requests_total.clear())
    template = loader.get_template('demo/index.html')

    return HttpResponse(template.render())

# Django prometheus metriklerini görüntülemek için
# urlpatterns += [path('metrics/', exports.ExportToDjangoView.as_view())]
