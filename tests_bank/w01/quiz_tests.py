"""Week w01 tests — 12 tasks

Autograding imports student functions from:
  submissions/w01/answers.py
"""

import math
import numpy as np
import pytest
from scipy.stats import norm

from submissions.w01 import answers as A


@pytest.mark.task(taskno=1)
def test_q01():
    assert math.isclose(A.q01(), 0.875, rel_tol=0, abs_tol=1e-12)


@pytest.mark.task(taskno=2)
def test_q02():
    assert A.q02() == 120


@pytest.mark.task(taskno=3)
def test_q03():
    assert math.isclose(A.q03(), 10/18, rel_tol=0, abs_tol=1e-12)


@pytest.mark.task(taskno=4)
def test_q04():
    expected = 0.08755760368663597
    assert math.isclose(A.q04(), expected, rel_tol=0, abs_tol=1e-12)


@pytest.mark.task(taskno=5)
def test_q05():
    assert math.isclose(A.q05(), 2.0, rel_tol=0, abs_tol=1e-12)


@pytest.mark.task(taskno=6)
def test_q06():
    out = A.q06()
    assert isinstance(out, (list, tuple, np.ndarray))
    assert len(out) == 5
    expected = np.array([0.2401, 0.4116, 0.2646, 0.0756, 0.0081], dtype=float)
    got = np.array(out, dtype=float)
    assert np.all(got >= 0)
    assert math.isclose(float(got.sum()), 1.0, rel_tol=0, abs_tol=1e-10)
    assert np.allclose(got, expected, rtol=0, atol=1e-10)


@pytest.mark.task(taskno=7)
def test_q07():
    expected = 35/12
    assert math.isclose(A.q07(), expected, rel_tol=0, abs_tol=1e-12)


@pytest.mark.task(taskno=8)
def test_q08():
    expected = 1/6
    assert math.isclose(A.q08(), expected, rel_tol=0, abs_tol=1e-12)


@pytest.mark.task(taskno=9)
def test_q09():
    expected = float(norm.cdf(12, loc=10, scale=2) - norm.cdf(8, loc=10, scale=2))
    assert math.isclose(A.q09(), expected, rel_tol=0, abs_tol=1e-12)


@pytest.mark.task(taskno=10)
def test_q10():
    expected = 1.96 * 4 / 5
    assert math.isclose(A.q10(), expected, rel_tol=0, abs_tol=1e-12)


@pytest.mark.task(taskno=11)
def test_q11():
    expected = float(2 * (1 - norm.cdf(2.1)))
    assert math.isclose(A.q11(), expected, rel_tol=0, abs_tol=1e-12)


@pytest.mark.task(taskno=12)
def test_q12():
    got = float(A.q12())
    analytic = float(1 - norm.cdf(1.5))
    assert 0.0 <= got <= 1.0
    assert abs(got - analytic) <= 0.001
