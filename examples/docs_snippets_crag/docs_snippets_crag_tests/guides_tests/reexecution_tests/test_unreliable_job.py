from dagster import execute_pipeline
from docs_snippets_crag.guides.dagster.reexecution.unreliable_job import unreliable_job


def test_job_compiles_and_executes():
    result = execute_pipeline(unreliable_job, solid_selection=["start"])
    assert result.success
