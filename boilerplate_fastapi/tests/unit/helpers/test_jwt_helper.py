import os

from boilerplate_fastapi.helpers.jwt_helper import encode, decode


def test_encode_jwt(mocker):
    secret = "SECRET"
    token = "t0k3n"
    mock_encode = mocker.patch("jwt.encode", return_value=token)
    mocker.patch("boilerplate_fastapi.helpers.jwt_helper.config", return_value=secret)
    data = {"email": "teste@teste.com"}
    res = encode(data)
    assert res == token
    mock_encode.assert_called_with(payload=data, key=secret, algorithm="HS256")


def test_decode_jwt(mocker):
    secret = "SECRET"
    token = "t0k3n"
    data = {"email": "teste@teste.com"}
    mock_decode = mocker.patch("jwt.decode", return_value=data)
    os.environ.get = mocker.patch("boilerplate_fastapi.helpers.jwt_helper.config", return_value=secret)
    decode(token)
    mock_decode.assert_called_with(jwt=token, key=secret, algorithms=["HS256"])


def test_decode_jwt_with_error(mocker):
    secret = "SECRET"
    token = "t0k3n"
    data = {"email": "teste@teste.com"}
    mock_decode = mocker.patch("jwt.decode", side_effect=Exception("error when decode jwt"))
    # mock_decode.side_effect = Exception("AAAA")
    mocker.patch("boilerplate_fastapi.helpers.jwt_helper.config", return_value=secret)
    result = decode(token)
    assert result == {}
    mock_decode.assert_called_with(jwt=token, key=secret, algorithms=["HS256"])