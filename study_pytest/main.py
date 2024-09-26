import pytest


# pytest.main(["-vs","test_setup_module.py"])
# pytest.main(["-s","-m","not login","test_05.py"])
pytest.main(["-s","-m","login","test_05.py"])
pytest.main(["-s","-m","login or quit","test_05.py"])