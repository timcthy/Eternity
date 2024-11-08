import pytest

import stats.stddev

def test_population_variance():
	assert stats.stddev.population_variance([6,2,3,1]) == pytest.approx(3.5)

def test_sample_variance():
	assert stats.stddev.sample_variance([2,2,5,7]) == pytest.approx(6)

def test_population_standard_deviation():
	assert stats.stddev.population_standard_deviation([6,2,3,1]) == pytest.approx(1.870828693387)
def test_sample_standard_deviation():
	assert stats.stddev.sample_standard_deviation([2,2,5,7]) == pytest.approx(2.4494897427832)
	# pass

def test_mean():
	assert stats.stddev.mean([6,2,3,1]) == 3
	assert stats.stddev.mean([2,2,5,7]) == 4


def test_algo():
	A_0: float = 0
	A = A_0
	Q: float = 0
	Q_0 = Q
	k: float = 0
	for x in [6,2,3,1]:
		k+=1 
		A = A_0 + (x-A_0)/k
		Q = Q_0 + (k-1)/k * (x-A_0)**2
		Q2 = Q_0 + (x - A_0) * (x - A)
		assert Q == pytest.approx(Q2)
		A_0 = A
