from git import Repo

from schema.schema_holder import SCHEMA_VERSION


def test_if_schema_tag_is_the_same_as_on_production():
    schema_repostiroy_repo = Repo.clone_from("https://github.com/bartosz25/data-generator.git", "/tmp/repo")
    tags = sorted(schema_repostiroy_repo.tags, key=lambda t: t.commit.committed_datetime)
    latest_tag = tags[-1]

    assert str(latest_tag) == SCHEMA_VERSION, "a new schema was released, please update the application code"

