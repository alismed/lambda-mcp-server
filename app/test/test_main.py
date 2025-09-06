import pytest
from unittest.mock import MagicMock
import app.src.main as main


def test_list_resources(monkeypatch):
    mock_client = MagicMock()
    mock_client.describe_instances.return_value = {
        "Reservations": [
            {
                "Instances": [
                    {
                        "InstanceId": "i-1234567890abcdef0",
                        "InstanceType": "t2.micro",
                        "State": {"Name": "running"},
                        "PublicIpAddress": "1.2.3.4",
                        "PrivateIpAddress": "10.0.0.1",
                    }
                ]
            }
        ]
    }

    monkeypatch.setattr(main.boto3, "client", lambda service: mock_client)

    result = main.list_resources()
    assert isinstance(result, list)
    assert len(result) == 1
    r = result[0]
    assert r["InstanceId"] == "i-1234567890abcdef0"
    assert r["InstanceType"] == "t2.micro"
    assert r["State"] == "running"
    assert r["PublicIpAddress"] == "1.2.3.4"
    assert r["PrivateIpAddress"] == "10.0.0.1"


def test_lambda_handler_list_resources(monkeypatch):
    monkeypatch.setattr(main, "list_resources", lambda: [{"InstanceId": "i-1"}])
    event = {"info": {"fieldName": "ListResources"}}
    context = {}
    result = main.lambda_handler(event, context)
    assert result == [{"InstanceId": "i-1"}]


def test_lambda_handler_unknown_field():
    event = {"info": {"fieldName": "UnknownField"}}
    context = {}
    with pytest.raises(Exception) as excinfo:
        main.lambda_handler(event, context)
    assert "Unknown field" in str(excinfo.value)


def test_lambda_handler_missing_fieldName_with_action():
    # When info present but no fieldName, current handler returns message
    event = {"info": {"action": "ECS"}}
    context = {}
    result = main.lambda_handler(event, context)
    assert "fieldName must be provided" in result


def test_lambda_handler_missing_info():
    # When info missing entirely, handler returns message
    event = {}
    context = {}
    result = main.lambda_handler(event, context)
    assert "fieldName must be provided" in result
