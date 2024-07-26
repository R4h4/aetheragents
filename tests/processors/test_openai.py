import pytest
from aetheragents.processors.openai import OpenAIProcessor, InputType
from unittest.mock import MagicMock


@pytest.fixture
def openai_processor():
    return OpenAIProcessor(
        api_key="test_api_key",
        model="test_model",
        prompt="Hello, {name}!",
        system_prompt="System message",
        output_schema={
            "type": "object",
            "properties": {"response": {"type": "string"}},
        },
        input_type=InputType.TEXT,
    )


def test_process_text_input(openai_processor):
    openai_processor.client = MagicMock()
    openai_processor.client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Test response"))]
    )
    result = openai_processor.process(name="World")
    assert result == "Test response"
    openai_processor.client.chat.completions.create.assert_called_once()


def test_process_image_input():
    processor = OpenAIProcessor(
        api_key="test_api_key",
        model="test_model",
        prompt="Describe the image of {object}.",
        input_type=InputType.IMAGE,
    )
    processor.client = MagicMock()
    processor.client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Image response"))]
    )
    result = processor.process(object="cat", image="base64encodedimage")
    assert result == "Image response"
    processor.client.chat.completions.create.assert_called_once()


def test_prepare_messages_text(openai_processor):
    messages = openai_processor._prepare_messages({"name": "World"})
    assert messages == [
        {"role": "system", "content": "System message"},
        {"role": "user", "content": "Hello, World!"},
        {
            "role": "system",
            "content": "Please provide your response in JSON format according to this schema: {'type': 'object', 'properties': {'response': {'type': 'string'}}}",
        },
    ]


def test_prepare_messages_image():
    processor = OpenAIProcessor(
        api_key="test_api_key",
        model="test_model",
        prompt="Describe the image of {object}.",
        input_type=InputType.IMAGE,
    )
    messages = processor._prepare_messages(
        {"object": "cat", "image": "base64encodedimage"}
    )
    assert messages == [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe the image of cat."},
                {
                    "type": "image_url",
                    "image_url": {"url": "data:image/jpeg;base64,base64encodedimage"},
                },
            ],
        }
    ]


def test_validate_input_missing_keys(openai_processor):
    with pytest.raises(ValueError, match="Missing required arguments: name"):
        openai_processor.validate_input(set())


def test_validate_input_extra_keys(openai_processor):
    with pytest.raises(ValueError, match="Unexpected arguments provided: extra"):
        openai_processor.validate_input({"name", "extra"})
