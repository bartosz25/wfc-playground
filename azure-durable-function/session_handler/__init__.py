import logging
import azure.durable_functions as df


"""
An entity function intended to demonstrate:
- different state operations: read, write
- state storage: starts with a serialized value in Table Storage but gets transformed into a blob after going too big
"""

def entity_function(context: df.DurableEntityContext):
    # quite big state that should go to Storage Account after ???????? invocations
    state_value = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas convallis faucibus velit a posuere. Nullam ac tellus vitae nibh vehicula scelerisque non non diam. Phasellus fermentum mattis nibh nec feugiat. Etiam at accumsan massa, eget luctus erat. Nullam placerat facilisis vulputate. Nunc at neque tempus, eleifend est in, luctus nisl. Quisque venenatis quis nisi eu commodo. Proin non fermentum nulla. Proin vehicula pulvinar tincidunt. Cras id tincidunt lacus. Sed tincidunt libero purus, sit amet cursus magna rutrum at.

    Vestibulum maximus tempus risus eget ullamcorper. Proin eu sem nec eros auctor convallis malesuada eget odio. Curabitur mi erat, bibendum ut dui sit amet, placerat bibendum eros. Aliquam lobortis augue leo, at rutrum tellus viverra quis. Sed vulputate venenatis eros. Etiam et quam tristique, varius sapien dapibus, malesuada elit. Integer non tellus mauris. Nulla urna nisi, pharetra vel porttitor ut, pretium in ex. Etiam vestibulum vulputate nunc, sed tincidunt libero vehicula sollicitudin. Suspendisse dictum finibus sapien quis tristique. Mauris quis tempus est, quis vulputate eros.

    Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras quis odio ex. Proin porta dolor eget tortor pellentesque iaculis. Nulla accumsan purus quis sagittis fringilla. Integer eget nisi elit. Suspendisse commodo massa massa, ac dapibus nunc gravida vel. Duis id orci eu sapien ultrices finibus nec et metus. Donec mattis lacinia ligula. Nunc sed egestas eros. Sed dapibus fermentum risus vel euismod. Proin elementum maximus porttitor.

    Praesent laoreet nisl posuere ultricies maximus. Phasellus eu venenatis arcu. Fusce scelerisque est et interdum dignissim. Donec et eleifend urna. Aliquam vel molestie ligula. Praesent nunc turpis, aliquam ac orci eu, convallis ultricies risus. Donec blandit libero sit amet dolor condimentum tempus. Phasellus et dignissim mauris. Phasellus non ligula sem. Sed elementum aliquet neque quis finibus.

    Vivamus dictum dolor a risus consectetur, non fringilla enim porta. Aliquam ex nisi, sagittis cursus tellus non, eleifend scelerisque ex. Nulla vulputate purus a mollis mattis. Aenean in ultricies velit, eu auctor odio. Curabitur ultricies turpis in scelerisque fermentum. In et diam laoreet, finibus tortor ut, placerat tellus. In eget lectus egestas, tincidunt odio ut, dignissim est. Curabitur tempor risus sit amet turpis mattis, quis ornare ligula bibendum. Fusce mauris metus, lacinia at orci quis, tincidunt malesuada justo. Pellentesque lacus felis, egestas id faucibus a, vestibulum vel neque. Sed eu efficitur lacus, eu tincidunt augue.

    Vestibulum interdum non urna at lobortis. Duis sollicitudin turpis vel arcu luctus, sit amet porta risus commodo. Ut et odio vitae erat pretium faucibus. Fusce eu dolor vitae sem feugiat ornare vitae id metus. Fusce semper auctor dui. Aliquam eleifend aliquet mi, non suscipit ipsum iaculis ac. Suspendisse elementum, est sit amet rutrum pharetra, nisl dolor pretium mauris, posuere convallis nibh neque ut enim. Proin vel enim in risus blandit viverra vel nec nisi. Integer blandit eleifend ex quis efficitur. Nam faucibus imperdiet neque quis ultrices. Nunc mollis mi nulla, at elementum magna laoreet id. Integer sollicitudin sit amet justo et scelerisque. Duis lectus nulla, semper vestibulum leo at, tincidunt accumsan neque. Vestibulum in mi eget nibh laoreet aliquam. Cras imperdiet vulputate tellus sit amet tincidunt.

    Nam dapibus sollicitudin lacus vitae tempor. In hac habitasse platea dictumst. In vulputate tellus et laoreet iaculis. Fusce varius fermentum ornare. Aenean ac auctor elit, commodo elementum enim. Nunc iaculis libero eu fermentum feugiat. Donec nulla nisl, scelerisque eu semper vehicula, porta quis urna. Suspendisse potenti. Vestibulum sit amet erat sit amet ex feugiat vestibulum. Nunc massa mi, faucibus sed metus sed, facilisis lobortis ante. Sed vitae porttitor turpis, a mollis arcu.

    Nunc lacinia libero in est viverra, eu cursus ante dapibus. Aenean eu ullamcorper quam. Quisque ornare ex in ipsum finibus, egestas blandit orci lacinia. Phasellus porta sem pulvinar nibh convallis, ac volutpat nibh sollicitudin. Nam eu gravida quam. Phasellus interdum mollis arcu. Nullam sed sodales turpis, at semper massa. Donec varius tortor a neque convallis mattis. Nam ultrices commodo porttitor. Sed tincidunt aliquam luctus.

    Praesent quis interdum risus. Nulla molestie erat dolor, vel sodales nisi sodales sed. Nulla sed ex nunc. Aenean gravida ex blandit urna sollicitudin tempus. Suspendisse neque eros, finibus eu libero eu, eleifend imperdiet odio. Sed gravida, ipsum non pellentesque efficitur, justo velit pharetra ipsum, vitae venenatis nunc dolor ac libero. Integer sollicitudin, ex ac eleifend malesuada, erat libero suscipit ex, at hendrerit felis massa nec sem.

    Nunc hendrerit diam in tempor auctor. Mauris sapien dui, aliquet ut placerat sit amet, laoreet vel neque. Vivamus et nisl felis. Nulla pretium felis sit amet blandit euismod. Nam vitae dignissim erat. Mauris interdum augue in varius congue. Etiam semper augue nec augue vestibulum, vel scelerisque erat laoreet. Nullam id finibus elit. Proin convallis feugiat augue ut ornare. Vestibulum nec accumsan sapien, eu fringilla velit. Praesent tempus varius sapien, ac tincidunt sapien convallis quis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

    Donec ac enim eu elit pharetra posuere. Ut ultricies ut mi eget venenatis. Donec mollis facilisis sapien, at lobortis nunc. Quisque dapibus hendrerit nibh eu posuere. Duis pharetra lorem sit amet lectus interdum posuere. Cras eget auctor nunc, ac blandit sapien. Mauris felis nisl, consequat ut dolor eu, maximus iaculis nunc. Maecenas gravida nisi vitae magna imperdiet commodo. Vivamus pellentesque sagittis nunc et egestas. Donec massa turpis, tincidunt quis commodo non, dignissim a lectus. Suspendisse id suscipit massa. Aenean eget ipsum quis diam bibendum volutpat et sagittis metus.
    """
    current_value = context.get_state(lambda: state_value)
    operation = context.operation_name
    if operation == 'add':
        repetition_factor = context.get_input()
        logging.info(f'Accumulating the state x{repetition_factor}!')
        current_value += state_value * repetition_factor
        context.set_state(current_value)
    elif operation == 'reset':
        logging.info('Resetting the state!')
        current_value = state_value
        context.set_state(current_value)
    elif operation == 'get':
        logging.info('Getting results!')
        context.set_result(current_value)


main = df.Entity.create(entity_function)
