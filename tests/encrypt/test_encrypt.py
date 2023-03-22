import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    string = "python"

    assert encrypt_message(string, 3) == "typ_noh"
    assert encrypt_message(string, 4) == "no_htyp"
    assert encrypt_message(string, 9) == "nohtyp"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(string, "")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)
