from digital_root import digital_root


# Digital Root Cases
def test_digital_root_16():
    assert digital_root(16) == 7, "Failed for digital root case: 16"


def test_digital_root_942():
    assert digital_root(942) == 6, "Failed for digital root case: 942"


def test_digital_root_1():
    assert digital_root(1) == 1, "Failed for digital root case: 1"


def test_digital_root_0():
    assert digital_root(0) == 0, "Failed for digital root case: 0"


def test_digital_root_770353():
    assert digital_root(770353) == 7, "Failed for digital root case: 770353"


def test_digital_root_562346():
    assert digital_root(562346) == 8, "Failed for digital root case: 562346"


def test_digital_root_54904():
    assert digital_root(54904) == 4, "Failed for digital root case: 54904"


def test_digital_root_568599():
    assert digital_root(568599) == 6, "Failed for digital root case: 568599"


def test_digital_root_739679():
    assert digital_root(739679) == 5, "Failed for digital root case: 739679"


def test_digital_root_228707():
    assert digital_root(228707) == 8, "Failed for digital root case: 228707"


def test_digital_root_918963():
    assert digital_root(918963) == 9, "Failed for digital root case: 918963"


def test_digital_root_625743():
    assert digital_root(625743) == 9, "Failed for digital root case: 625743"


def test_digital_root_190862():
    assert digital_root(190862) == 8, "Failed for digital root case: 190862"


def test_digital_root_155073():
    assert digital_root(155073) == 3, "Failed for digital root case: 155073"
