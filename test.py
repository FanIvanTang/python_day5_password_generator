from main import get_inputs_from_user
from tud_test_base import set_keyboard_input, get_display_output


def test_case_1_get_inputs_from_user():

    set_keyboard_input(["8", "3", "2"])

    assert get_inputs_from_user() == (8, 3, 2)


def test_case_2_get_inputs_from_user():

    set_keyboard_input(["08", "03", "02"])

    assert get_inputs_from_user() == (8, 3, 2)
