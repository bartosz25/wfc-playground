# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
import logging

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    logging.info(f'Got input {context.get_input()}')
    input_params = context.get_input() # this time, it's a dict!
    number_of_hellos = input_params['hellos_count']
    result1 = yield context.call_activity('message_logger', f'Text 1 - {number_of_hellos}')
    result2 = yield context.call_activity('message_logger', f'Text 2 - {number_of_hellos}')
    return [result1, result2]


main = df.Orchestrator.create(orchestrator_function)