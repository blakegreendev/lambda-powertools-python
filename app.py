#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambda_powertools_python.lambda_powertools_python_stack import LambdaPowertoolsPythonStack


app = cdk.App()
LambdaPowertoolsPythonStack(app, "LambdaPowertoolsPythonStack")

app.synth()
