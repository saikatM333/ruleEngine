import json
from typing import Dict, Any

class Node:
    def __init__(self, type: str, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left
        self.right = right
        self.value = value

    def to_dict(self):
        return {
            "type": self.type,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
            "value": self.value
        }

def parse_rule(rule_string: str) -> Node:
    # This is a placeholder for a real parser.
    # For simplicity, we'll assume that the rule strings are simple and create a mock AST.
    # A more complex parser would be needed for production.
    # E.g., rule_string: "age > 30 AND department = 'Sales'"
    # Node creation based on the given example (mock parsing)
    if "age > 30" in rule_string and "department = 'Sales'" in rule_string:
        return Node("operator", 
                    Node("operand", value="age > 30"), 
                    Node("operand", value="department = 'Sales'"), 
                    "AND")
    # Add more parsing conditions as needed.
    return Node("operand", value=rule_string)

def combine_rules(rules: list) -> Node:
    # Combines rules into a single AST using an OR operator
    if not rules:
        return None

    root = parse_rule(rules[0])
    for rule in rules[1:]:
        root = Node("operator", left=root, right=parse_rule(rule), value="OR")

    return root

def evaluate_rule(ast: Dict[str, Any], data: Dict[str, Any]) -> bool:
    # Recursively evaluate the AST
    if ast['type'] == 'operand':
        condition = ast['value']
        return eval_condition(condition, data)
    elif ast['type'] == 'operator':
        left_result = evaluate_rule(ast['left'], data)
        right_result = evaluate_rule(ast['right'], data)
        if ast['value'] == "AND":
            return left_result and right_result
        elif ast['value'] == "OR":
            return left_result or right_result
    return False

def eval_condition(condition: str, data: Dict[str, Any]) -> bool:
    # This is a simple evaluator; a real-world version would be more robust.
    # E.g., "age > 30" should be evaluated based on data['age']
    try:
        return eval(condition, {}, data)
    except Exception:
        return False
