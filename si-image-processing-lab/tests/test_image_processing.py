import os

from si_image_processing.pipelines.image_processing.nodes import process_image


def test_process_image_returns_path():
    result = process_image(
        "data/01_raw/marte.jpg",
        "data/03_primary/test_output.jpg",
        45,
        "EMBOSS",
        "UCV Test"
    )
    assert result == "data/03_primary/test_output.jpg"


def test_process_image_file_exists():
    result = process_image(
        "data/01_raw/marte.jpg",
        "data/03_primary/test_output2.jpg",
        0,
        "EMBOSS",
        "Test"
    )
    assert os.path.exists(result)


def test_process_image_find_edges():
    result = process_image(
        "data/01_raw/marte.jpg",
        "data/03_primary/test_find_edges.jpg",
        90,
        "FIND_EDGES",
        "FIND EDGES Test"
    )
    assert result is not None


def test_process_image_custom_angle():
    result = process_image(
        "data/01_raw/marte.jpg",
        "data/03_primary/test_angle.jpg",
        180,
        "EMBOSS",
        "Rotacion 180"
    )
    assert os.path.exists(result)


def test_process_image_custom_watermark():
    result = process_image(
        "data/01_raw/marte.jpg",
        "data/03_primary/test_watermark.jpg",
        45,
        "EMBOSS",
        "Marca Personalizada UCV 2025"
    )
    assert result is not None