import pathlib

test_image_dir = pathlib.Path(__file__).parent.resolve() / "sample-images"


def test_extract():
    from nms_translator.textract import extract_from_file

    for num in [1, 2, 3]:
        test_output = extract_from_file(test_image_dir / f"{num}.png")
        assert test_output == f"Sample Text {num}"


def test_grab():
    from nms_translator.grabber import grab_screen
    from os import path

    temp_path = grab_screen()
    assert path.isfile(temp_path)


def test_translate_from_img():
    from nms_translator.textract import extract_from_file
    from nms_translator.translator import translate

    encoded_str = extract_from_file(test_image_dir / "binary.png")
    print(encoded_str)
    decoded_str = translate(encoded_str)
    assert decoded_str == "this is a test"
