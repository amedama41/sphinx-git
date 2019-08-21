from nose.tools import assert_equal, assert_raises

from sphinx_git import get_details_style, get_flag


class TestGetDetailsStyle(object):
    def test_pre_argument(self):
        style = get_details_style('pre')
        assert_equal(style, 'pre')

    def test_rst_argument(self):
        style = get_details_style('rst')
        assert_equal(style, 'rst')

    def test_md_argument(self):
        style = get_details_style('md')
        assert_equal(style, 'md')

    def test_non_argument(self):
        assert_raises(ValueError, get_details_style, None)

    def test_other_argument(self):
        assert_raises(ValueError, get_details_style, 'other')


class TestGetFlag(object):
    def test_none_argument(self):
        flag = get_flag(None)
        assert_equal(flag, True)

    def test_no_argument(self):
        flag = get_flag('')
        assert_equal(flag, True)

    def test_false_argument(self):
        flag = get_flag('False')
        assert_equal(flag, False)

    def test_zero_argument(self):
        flag = get_flag('0')
        assert_equal(flag, False)

    def test_true_argument(self):
        flag = get_flag('True')
        assert_equal(flag, True)

    def test_one_argument(self):
        flag = get_flag('1')
        assert_equal(flag, True)
