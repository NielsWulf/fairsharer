from fairsharer import fair_sharer

def test_fair_sharer():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert np.allclose(result, np.array([100, 800, 900, 0]), atol=1e-5, rtol=1e-5)
