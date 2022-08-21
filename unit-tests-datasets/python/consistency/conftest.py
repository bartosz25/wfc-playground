import pytest

from consistency.data_generators import DataGeneratorWrapper

def validate_item_against_data_profiling_endpoint(item) -> bool:
    return False

@pytest.fixture(scope="session", autouse=True)
def my_session_finish(request):
    def _end():
        items_to_validate = DataGeneratorWrapper().get_items()
        has_error = False
        print(f'items_to_validate={items_to_validate}')
        for item_to_validate in items_to_validate:
            if not validate_item_against_data_profiling_endpoint(item_to_validate):
                print(f'Error while validating {item_to_validate}')
                has_error = True

        if has_error:
            raise Exception("Test are inconsistent with the data profile")
    request.addfinalizer(_end)
