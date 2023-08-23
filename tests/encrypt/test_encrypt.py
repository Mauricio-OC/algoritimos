from challenges.challenge_ encrypt_message import encrypt_message
import pytest
    
def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("testa messagem", "invalido_key")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(12345, 2)

    assert encrypt_message("test message", 0) == "egassem tset"
    assert encrypt_message("test message", 100) == "egassem tset"
    
    assert encrypt_message("test message", 3) == "tse_egassem t"
    
    assert encrypt_message("test message", 4) == " et_tse_egassem"

    assert encrypt_message("abcdefghij", 5) == "e_dcba_ghij"
