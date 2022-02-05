import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_powertools_python.lambda_powertools_python_stack import LambdaPowertoolsPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_powertools_python/lambda_powertools_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaPowertoolsPythonStack(app, "lambda-powertools-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
