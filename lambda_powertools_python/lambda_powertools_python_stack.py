from aws_cdk import (
    CfnOutput,
    Stack,
    aws_lambda as lambda_
)
import aws_cdk.aws_lambda_python_alpha as lambda_python
import aws_cdk.aws_apigatewayv2_alpha as apiv2
from aws_cdk.aws_apigatewayv2_integrations_alpha import HttpLambdaIntegration
from cdk_lambda_powertools_python_layer import LambdaPowertoolsLayer
from constructs import Construct

class LambdaPowertoolsPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        powertoolsLayer = LambdaPowertoolsLayer(self, 'LambdaPowertools')

        fn = lambda_python.PythonFunction(self, "function",
            entry="functions",
            runtime=lambda_.Runtime.PYTHON_3_9,
            index="app.py",
            handler="lambda_handler",
            tracing=lambda_.Tracing.ACTIVE,
            layers=[powertoolsLayer]
        )

        api_integ = HttpLambdaIntegration("integ", fn)
        http_api = apiv2.HttpApi(self, 'httpapi')
        http_api.add_routes(
            path="/{proxy+}",
            methods=[apiv2.HttpMethod.ANY],
            integration=api_integ
        )

        CfnOutput(self, "api_url", value=http_api.api_endpoint)

