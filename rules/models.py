from django.db import models
import json

class Rule(models.Model):
    rule_string = models.TextField()  # Stores the rule in string form
    ast = models.JSONField()          # Stores the rule in AST form as JSON

    def __str__(self):
        return self.rule_string
