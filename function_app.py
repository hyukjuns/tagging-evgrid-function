import logging
import json
import azure.functions as func

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

default_credential = DefaultAzureCredential()
client = ResourceManagementClient(default_credential)

app = func.FunctionApp()

@app.function_name(name="eventgridtrigger")
@app.event_grid_trigger(arg_name="event")
def EventGridTrigger(event: func.EventGridEvent):
    
    # result = json.dumps({
    #     'id': event.id,
    #     'data': event.get_json(),
    #     'topic': event.topic,
    #     'subject': event.subject,
    #     'event_type': event.event_type,
    # })

    # logging.info('Python EventGrid trigger processed an event: %s', result)

    # Get dadta
    data = event.get_json()    
    # # # get resource id
    resource_id = data['resourceUri']
    logging.info(resource_id)
    # # get caller
    caller = data['claims']['name']
    logging.info(caller)
    # # check tag exists
    client.tags.list()
    # # update tag
