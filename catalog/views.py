from django.views.generic.base import TemplateView
class home(TemplateView):
    template_name=('base.html')

    def get_context_data(self,**kwargs):
        return {'name':'Am a datalava','ok':'hello()'}
