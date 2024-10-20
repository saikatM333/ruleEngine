from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rule
from .serializers import RuleSerializer
from .utils import parse_rule, combine_rules, evaluate_rule

class CreateRuleView(APIView):
    def post(self, request):
        rule_string = request.data.get('rule_string')
        ast = parse_rule(rule_string)
        rule = Rule(rule_string=rule_string, ast=ast.to_dict())
        rule.save()
        serializer = RuleSerializer(rule)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CombineRulesView(APIView):
    def post(self, request):
        rule_strings = request.data.get('rules', [])
        combined_ast = combine_rules(rule_strings)
        return Response(combined_ast.to_dict(), status=status.HTTP_200_OK)

class EvaluateRuleView(APIView):
    def post(self, request):
        ast = request.data.get('ast')
        data = request.data.get('data', {})
        result = evaluate_rule(ast, data)
        return Response({"result": result}, status=status.HTTP_200_OK)
