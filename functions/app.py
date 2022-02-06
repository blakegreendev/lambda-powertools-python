from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, ProxyEventType
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths

logger = Logger(service="APP")
tracer = Tracer(service="APP")
app = ApiGatewayResolver(proxy_type=ProxyEventType.APIGatewayProxyEventV2)

#Route annotations as decorators for methods. It enables the parameters passed in the request directly, and responses are simply dictionaries.
@app.get("/hello")
@tracer.capture_method
def hello():
    tracer.put_annotation(key="User", value="unknown")
    logger.info(f"Request from unknown received!")
    return {"message": "hello unknown!"}

@app.get("/hello/<name>")
@tracer.capture_method
def hello_name(name):
    tracer.put_annotation(key="User", value=name)
    logger.info(f"Request from {name} recieved!")
    return {"message": f"hello {name}!!!"}

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP, log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    # Event Handler resolves routes, injects the current request, handle servialization, route validation, etc.
    return app.resolve(event, context)