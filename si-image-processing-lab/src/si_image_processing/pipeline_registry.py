from kedro.pipeline import Pipeline

from si_image_processing.pipelines.image_processing.pipeline import (
    create_pipeline as image_processing_pipeline,
)


def register_pipelines() -> dict[str, Pipeline]:
    image_pipeline = image_processing_pipeline()
    return {
        "__default__": image_pipeline,
        "image_processing": image_pipeline,
    }