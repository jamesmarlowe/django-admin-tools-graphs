from django.utils.translation import ugettext_lazy as _
from django.db.models import get_models
from django.db import models
import settings

APP_CHOICES = ((i,i) for i in settings.INSTALLED_APPS)

MODEL_CHOICES = ((model.__name__,model.__name__) for model in get_models())

class DashboardStats(models.Model):
    graph_title = models.CharField(max_length=90, db_index=True,verbose_name=_('Graph Title'),help_text=_("Heading title of graph box"))
    model_app_name = models.CharField(max_length=90, choices=APP_CHOICES, verbose_name=_('App Name'),help_text=_("Ex. auth / QuestionOfTheDay"))
    model_name = models.CharField(max_length=90, choices=MODEL_CHOICES, verbose_name=_('Model Name'),help_text=_("Ex. User / Response"))
    is_visible = models.BooleanField(default=True, verbose_name=_('Visible'))
    class Meta:
        verbose_name = _("Dashboard Stat")
        verbose_name_plural = _("Dashboard Stats")

GRAPH_CHOICES = [
('AnnotatedTimeLine','AnnotatedTimeLine'),
('PieChart','PieChart'),]

FIELD_CHOICES = [(model.__name__,[(field.name,field.name) for field in model._meta.fields]) for model in get_models()]
MODEL_CHOICES = ((model.__name__,model.__name__) for model in get_models())

class DashboardGraph(models.Model):
    graph_title = models.CharField(max_length=90, db_index=True,verbose_name=_('Graph Title'),help_text=_("Heading title of graph box"))
    graph_type = models.CharField(max_length=90, choices=GRAPH_CHOICES, verbose_name=_('Graph Type'),help_text=_("The type of the google graph"))
    model_name = models.CharField(max_length=90, choices=MODEL_CHOICES, verbose_name=_('Model Name'),help_text=_("The model to show statistics for"))
    is_visible = models.BooleanField(default=True, verbose_name=_('Visible'))
    date_field_name = models.CharField(max_length=90, choices=FIELD_CHOICES, verbose_name=_("Date Field Name"), help_text=_("Only used if graph type needs it (AnnotatedTimeLine)"))
    bool_field_name = models.CharField(max_length=90, choices=FIELD_CHOICES, verbose_name=_("Bool Field Name"), help_text=_("Only used if graph type needs it (PieChart)"))
    value_field_name = models.CharField(max_length=90, choices=FIELD_CHOICES, verbose_name=_("Value Field Name"), help_text=_("The verticle axis for bar type graphs"))
    class Meta:
        verbose_name = _("Dashboard Graph")
        verbose_name_plural = _("Dashboard Graphs")