import os
import crypt
from pwd import getpwuid, getpwnam
import pytest
from functions import *

@pytest.mark.parametrize("test_input_1, test_input_2, expected_output", [
    ([0, 1, 2, 3, 4], [3, 10, 56], 3),
    ([1, 2, 3, 4], [5, 6, 7, 8], None),
])
def test_find_repeated_number(test_input_1, test_input_2, expected_output):
    assert find_repeated_number(test_input_1, test_input_2) == expected_output

@pytest.fixture
def setup_teardown_for_test_find_file(capsys):
    with capsys.disabled():
        print("\n====SETUP====")
    try:
        getpwnam('admin')
        user_exists = 1
        with capsys.disabled():
            print("-- user \'admin\' already exists, skip creating it")
    except KeyError:
        user_exists = 0
        with capsys.disabled():
            print("-- creating user \'admin\'")
        passwd = "p@ssword1234"
        encpasswd = crypt.crypt(passwd,"22")
        os.system("sudo useradd -p "+encpasswd+" admin")

    yield

    with capsys.disabled():
        print("====TEARDOWN====")
    if not user_exists:
        with capsys.disabled():
            print("-- deleting user \'admin\'")
        os.system("sudo userdel admin")

def test_find_file(tmp_path, setup_teardown_for_test_find_file, capsys):
    with capsys.disabled():
        print("-- creating test folder")
    folder = tmp_path / "test_folder"
    folder.mkdir()
    with capsys.disabled():
        print("test folder="+str(folder))
    f1 = folder / "regular.txt"
    f2 = folder / "executable.sh"
    f1.write_text("Lorem Ipsum")
    f2.write_text("#/bin/bash\n echo \"Hello world!\"\n")
    os.system("chmod +x "+str(f2))
    os.system("sudo chown admin "+str(f2))
    assert find_file(str(folder)) == str(f2)

@pytest.mark.parametrize("test_input, expected_output", [
    ([0, 1, 1, 0], 1),
    ([1, 1, 1, 0, 0, 0], 2),
])
def test_find_swaps(test_input, expected_output):
    assert find_swaps(test_input) == expected_output