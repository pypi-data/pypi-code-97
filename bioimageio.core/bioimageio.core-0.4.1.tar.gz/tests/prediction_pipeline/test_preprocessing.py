import numpy as np
import xarray as xr

from bioimageio.core.prediction_pipeline._combined_processing import CombinedProcessing


def test_scale_linear():
    from bioimageio.core.prediction_pipeline._processing import ScaleLinear

    preprocessing = ScaleLinear("data_name", offset=[1, 2, 42], gain=[1, 2, 3], axes="yx")
    data = xr.DataArray(np.arange(6).reshape((1, 2, 3)), dims=("x", "y", "c"))
    expected = xr.DataArray(np.array([[[1, 4, 48], [4, 10, 57]]]), dims=("x", "y", "c"))
    result = preprocessing.apply(data)
    xr.testing.assert_allclose(expected, result)


def test_scale_linear_no_channel():
    from bioimageio.core.prediction_pipeline._processing import ScaleLinear

    preprocessing = ScaleLinear("data_name", offset=1, gain=2, axes="yx")
    data = xr.DataArray(np.arange(6).reshape(2, 3), dims=("x", "y"))
    expected = xr.DataArray(np.array([[1, 3, 5], [7, 9, 11]]), dims=("x", "y"))
    result = preprocessing.apply(data)
    xr.testing.assert_allclose(expected, result)


def test_zero_mean_unit_variance_preprocessing():
    from bioimageio.core.prediction_pipeline._processing import ZeroMeanUnitVariance

    preprocessing = ZeroMeanUnitVariance("data_name")
    data = xr.DataArray(np.arange(9).reshape(3, 3), dims=("x", "y"))
    expected = xr.DataArray(
        np.array(
            [
                [-1.54919274, -1.16189455, -0.77459637],
                [-0.38729818, 0.0, 0.38729818],
                [0.77459637, 1.16189455, 1.54919274],
            ]
        ),
        dims=("x", "y"),
    )
    result = preprocessing(data)
    xr.testing.assert_allclose(expected, result)


def test_zero_mean_unit_across_axes():
    from bioimageio.core.prediction_pipeline._processing import ZeroMeanUnitVariance

    preprocessing = ZeroMeanUnitVariance("data_name", axes=("x", "y"))
    data = xr.DataArray(np.arange(18).reshape((2, 3, 3)), dims=("c", "x", "y"))
    expected = xr.DataArray(
        np.array(
            [
                [-1.54919274, -1.16189455, -0.77459637],
                [-0.38729818, 0.0, 0.38729818],
                [0.77459637, 1.16189455, 1.54919274],
            ]
        ),
        dims=("x", "y"),
    )
    result = preprocessing(data)
    xr.testing.assert_allclose(expected, result[dict(c=0)])


def test_zero_mean_unit_variance_fixed():
    from bioimageio.core.prediction_pipeline._processing import ZeroMeanUnitVariance

    np_data = np.arange(9).reshape(3, 3)
    mean = np_data.mean()
    std = np_data.mean()
    eps = 1.0e-7
    preprocessing = ZeroMeanUnitVariance("data_name", mode="fixed", mean=mean, std=std, eps=eps)

    data = xr.DataArray(np_data, dims=("x", "y"))
    expected = xr.DataArray((np_data - mean) / (std + eps), dims=("x", "y"))
    result = preprocessing(data)
    xr.testing.assert_allclose(expected, result)


def test_binarize():
    from bioimageio.core.prediction_pipeline._processing import Binarize

    preprocessing = Binarize("data_name", threshold=14)
    data = xr.DataArray(np.arange(30).reshape((2, 3, 5)), dims=("x", "y", "c"))
    expected = xr.zeros_like(data)
    expected[{"x": slice(1, None)}] = 1
    result = preprocessing(data)
    xr.testing.assert_allclose(expected, result)


def test_clip_preprocessing():
    from bioimageio.core.prediction_pipeline._processing import Clip

    preprocessing = Clip("data_name", min=3, max=5)
    data = xr.DataArray(np.arange(9).reshape(3, 3), dims=("x", "y"))
    expected = xr.DataArray(np.array([[3, 3, 3], [3, 4, 5], [5, 5, 5]]), dims=("x", "y"))
    result = preprocessing(data)
    xr.testing.assert_equal(expected, result)


def test_combination_of_preprocessing_steps_with_dims_specified():
    from bioimageio.core.prediction_pipeline._processing import ZeroMeanUnitVariance

    preprocessing = ZeroMeanUnitVariance("data_name", axes=("x", "y"))
    data = xr.DataArray(np.arange(18).reshape((2, 3, 3)), dims=("c", "x", "y"))

    expected = xr.DataArray(
        np.array(
            [
                [-1.54919274, -1.16189455, -0.77459637],
                [-0.38729818, 0.0, 0.38729818],
                [0.77459637, 1.16189455, 1.54919274],
            ]
        ),
        dims=("x", "y"),
    )

    result = preprocessing(data)
    xr.testing.assert_allclose(expected, result[dict(c=0)])


def test_scale_range():
    from bioimageio.core.prediction_pipeline._processing import ScaleRange

    preprocessing = ScaleRange("data_name")
    np_data = np.arange(9).reshape(3, 3).astype("float32")
    data = xr.DataArray(np_data, dims=("x", "y"))
    preprocessing.set_computed_sample_statistics(
        CombinedProcessing.compute_sample_statistics(
            {"data_name": data}, preprocessing.get_required_sample_statistics()
        )
    )

    exp_data = (np_data - np_data.min()) / np_data.max()
    expected = xr.DataArray(exp_data, dims=("x", "y"))

    result = preprocessing(data)
    xr.testing.assert_allclose(expected, result)


def test_scale_range_axes():
    from bioimageio.core.prediction_pipeline._processing import ScaleRange

    min_percentile = 1.0
    max_percentile = 99.0
    preprocessing = ScaleRange(
        "data_name", axes=("x", "y"), min_percentile=min_percentile, max_percentile=max_percentile
    )

    np_data = np.arange(18).reshape((2, 3, 3)).astype("float32")
    data = xr.DataArray(np_data, dims=("c", "x", "y"))

    preprocessing.set_computed_sample_statistics(
        CombinedProcessing.compute_sample_statistics(
            {"data_name": data}, preprocessing.get_required_sample_statistics()
        )
    )

    p_low = np.percentile(np_data, min_percentile, axis=(1, 2), keepdims=True)
    p_up = np.percentile(np_data, max_percentile, axis=(1, 2), keepdims=True)
    exp_data = (np_data - p_low) / p_up
    expected = xr.DataArray(exp_data, dims=("c", "x", "y"))

    result = preprocessing(data)
    xr.testing.assert_allclose(expected, result)


def test_sigmoid():
    from bioimageio.core.prediction_pipeline._processing import Sigmoid

    shape = (3, 32, 32)
    axes = ("c", "y", "x")
    np_data = np.random.rand(*shape)
    data = xr.DataArray(np_data, dims=axes)

    sigmoid = Sigmoid("data_name")
    res = sigmoid(data)

    exp = xr.DataArray(1.0 / (1 + np.exp(-np_data)), dims=axes)
    xr.testing.assert_allclose(res, exp)
