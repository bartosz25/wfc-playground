import logging

import azure.functions as func
from azure.durable_functions import DurableOrchestrationClient, EntityId


"""
About the starter

From the doc (https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-bindings?tabs=csharp#entity-client)

> The entity client binding enables you to asynchronously trigger entity functions. 
> These functions are sometimes referred to as client functions.

From the doc (https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-instance-management?tabs=python#start-instances)
> The StartNewAsync (.NET), startNew (JavaScript), or start_new (Python) method on the orchestration client binding 
> starts a new orchestration instance. Internally, this method writes a message via the Durable Functions storag
> e provider and then returns. This message asynchronously triggers the start of an orchestration function 
> with the specified name.

"""
async def main(req: func.HttpRequest, starter: str):
    logging.info(f'Python HTTP trigger function processed a request. {req.params}')
    logging.info(f'Got starter {starter}')
    run_id = req.params.get('run_id')

    client = DurableOrchestrationClient(starter)
    # Direct call the entity
    entity_state_key = f'my_counter_{run_id}'
    entity_id = EntityId(name='session_handler', key=entity_state_key)
    await client.signal_entity(entity_id, "add", 2)
    await client.signal_entity(entity_id, "get")

    # Direct call the orchestrator to start activities pipeline
    # Doesn't support '#'
    # The doc recommends the automatic id generation
    instance_id = f'instance{run_id}'
    logging.info(f'Starting new orchestrator for {instance_id}')
    await client.start_new('message_orchestrator', instance_id, {'hellos_count': req.params.get('hellos_count')})

    return func.HttpResponse(status_code=202)

"""
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
"""
