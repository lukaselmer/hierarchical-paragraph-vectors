from helpers.learning_rate_helper import alpha_for_epoch


def assert_similar(a, b):
    assert abs(a - b) < 0.0001


def test_alpha_for_3_linear():
    assert_similar(alpha_for_epoch(1, 3, 0.025, 0.001, 'linear'), .025)
    assert_similar(alpha_for_epoch(2, 3, 0.025, 0.001, 'linear'), .013)
    assert_similar(alpha_for_epoch(3, 3, 0.025, 0.001, 'linear'), .001)


def test_alpha_for_4_linear():
    assert_similar(alpha_for_epoch(1, 4, 0.025, 0.001, 'linear'), .025)
    assert_similar(alpha_for_epoch(2, 4, 0.025, 0.001, 'linear'), .017)
    assert_similar(alpha_for_epoch(3, 4, 0.025, 0.001, 'linear'), .009)
    assert_similar(alpha_for_epoch(4, 4, 0.025, 0.001, 'linear'), .001)


def test_alpha_for_3_exp():
    assert_similar(alpha_for_epoch(1, 3, 0.025, 0.001, 'exp'), .025)
    assert_similar(alpha_for_epoch(2, 3, 0.025, 0.001, 'exp'), .005)
    assert_similar(alpha_for_epoch(3, 3, 0.025, 0.001, 'exp'), .001)


def test_alpha_for_4_exp():
    assert_similar(alpha_for_epoch(1, 4, 0.025, 0.001, 'exp'), .025)
    assert_similar(alpha_for_epoch(2, 4, 0.025, 0.001, 'exp'), .00854988)
    assert_similar(alpha_for_epoch(3, 4, 0.025, 0.001, 'exp'), .002924018)
    assert_similar(alpha_for_epoch(4, 4, 0.025, 0.001, 'exp'), .001)
