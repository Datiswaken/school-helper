import random

from src.pupil import Pupil
from src.school_class import SchoolClass


def test_draw_pupil_all_healthy(mocker):
    def mock_pupils(self):
        return [Pupil(name) for name in ["foo", "bar", "baz"]]

    mocker.patch(
        "src.school_class.SchoolClass.load_pupils",
        mock_pupils
    )

    school_class = SchoolClass("5d")
    random.seed(13)
    rnd_pupil = school_class.draw_pupil()

    assert rnd_pupil.name == "bar"

def test_draw_pupil_not_all_healthy(mocker):
    def mock_pupils(self):
        return [Pupil(name, is_sick) for name, is_sick in [("foo", False), ("bar", True), ("baz", False)]]

    mocker.patch(
        "src.school_class.SchoolClass.load_pupils",
        mock_pupils
    )

    school_class = SchoolClass("5d")
    random.seed(13)
    rnd_pupil = school_class.draw_pupil(only_healthy=True)

    assert len(school_class.get_healthy_pupils()) == 2
    assert rnd_pupil.name == "baz"


def test_split_into_n_groups(mocker):
    def mock_pupils(self):
        return [Pupil(name) for name in ["foo", "bar", "baz", "hello", "world", "I", "need", "more", "pupils"]]

    mocker.patch(
        "src.school_class.SchoolClass.load_pupils",
        mock_pupils
    )

    school_class = SchoolClass("5d")
    random.seed(13)
    groups = school_class.split_into_n_groups(4)

    assert len(groups) == 4
    assert len(groups[0]) == 3
    for group in groups[1:]:
        assert len(group) == 2

def test_make_groups_of_n_pupils(mocker):
    def mock_pupils(self):
        return [Pupil(name) for name in ["foo", "bar", "baz", "hello", "world", "I", "need", "more", "pupils"]]

    mocker.patch(
        "src.school_class.SchoolClass.load_pupils",
        mock_pupils
    )

    school_class = SchoolClass("5d")
    groups = school_class.make_groups_of_n_pupils(2)

    assert len(groups) == 4
    assert len(groups[0]) == 3
    for group in groups[1:]:
        assert len(group) == 2


