from digital_root import digital_root
from convert_string_to_camel_case import to_camel_case
from categorize_new_member import open_or_senior, process_member


# String to Camel Case Cases
def test_string_to_camel_case_1():
    assert (
        to_camel_case("the-stealth-warrior") == "theStealthWarrior"
    ), "Failed for camel case: the-stealth-warrior"


def test_string_to_camel_case_2():
    assert (
        to_camel_case("The_Stealth_Warrior") == "TheStealthWarrior"
    ), "Failed for camel case: The_Stealth_Warrior"


def test_string_to_camel_case_3():
    assert (
        to_camel_case("The_Stealth-Warrior") == "TheStealthWarrior"
    ), "Failed for camel case: The_Stealth-Warrior"


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


# Categorize New Member cases
def test_process_member_open_young():
    assert process_member([30, 10]) == "Open"


def test_process_member_open_age_limit():
    assert process_member([55, 7]) == "Open"


def test_process_member_senior_min_criteria():
    assert process_member([55, 8]) == "Senior"


def test_process_member_senior_above_criteria():
    assert process_member([60, 10]) == "Senior"


def test_open_or_senior_mixed_cases():
    assert open_or_senior(
        [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
    ) == ["Open", "Open", "Senior", "Open", "Open", "Senior"]


def test_open_or_senior_edge_cases():
    assert open_or_senior([[55, 7], [56, 7], [54, 8], [55, 8]]) == [
        "Open",
        "Open",
        "Open",
        "Senior",
    ]


def test_open_or_senior_empty_list():
    assert open_or_senior([]) == []
