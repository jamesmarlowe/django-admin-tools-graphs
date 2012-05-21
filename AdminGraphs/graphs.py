from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules
from django.core.urlresolvers import reverse
from models import DashboardGraph

def get_active_graphs():
    """Returns active graphs"""
    graph_list = []
    try:
        graph_list = DashboardGraph.objects.filter(is_visible=1)
        return graph_list
    except:
        return graph_list


class GoogleGraph(modules.DashboardModule):
    template = 'googlegraph.html'
    height=200
    graph_div = ''
    graph_type = ''
    graph_js_include = ''
    key='key'
    value='value'
    def __init__(self, title=None, **kwargs):
        if title is not None:
            self.title = title

        for key in kwargs:
            if hasattr(self.__class__, key):
                setattr(self, key, kwargs[key])

        self.graph_js_include = {
            'AnnotatedTimeLine': "google.load('visualization', '1', {packages: ['annotatedtimeline']});",
            'PieChart':          "google.load('visualization', '1', {packages: ['corechart']});"
        }[self.graph_type]

        self.css_classes = self.css_classes or []
        # boolean flag to ensure that the module is initialized only once
        self._initialized = False

    def init_with_context(self, context):
        if self._initialized:
            return
        self.graph_div = self.post_content
        self.post_content = ''
        self._initialized = True

    def is_empty(self):
        return False