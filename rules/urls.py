from django.urls import path ,re_path
from .views import CreateRuleView, CombineRulesView, EvaluateRuleView

urlpatterns = [
    path('create_rule', CreateRuleView.as_view(), name='create_rule'),
    path('combine_rules', CombineRulesView.as_view(), name='combine_rules'),
    path('evaluate_rule', EvaluateRuleView.as_view(), name='evaluate_rule'),
  

]
