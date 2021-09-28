import numpy as np
import pandas as pd
import statsmodels.api as sm

from ..univariate.metrics import t_value

__eps = np.finfo(np.float32).eps


def fit_robust_lm(x: np.ndarray, y: np.ndarray) -> list:
    """
    Fits a robust linear model between Numpy vectors `x` and `y`, with an
    intercept. Returns a list: [intercept, slope] of the fit. No extra
    checking on data consistency is done.

    See also:

    regression.repeated_median_slope
    """
    rlm_model = sm.RLM(
        y, np.vstack([np.ones(x.size), x.ravel()]).T, M=sm.robust.norms.HuberT()
    )
    rlm_results = rlm_model.fit()
    return rlm_results.params


def repeated_median_slope(x, y, nowarn=False):
    """
    Robust slope calculation.

    https://en.wikipedia.org/wiki/Repeated_median_regression

    An elegant (simple) method to compute the robust slope between a vector `x` and `y`.

    INVESTIGATE: algorithm speed-ups via these articles:
    https://link.springer.com/article/10.1007/PL00009190
    http://www.sciencedirect.com/science/article/pii/S0020019003003508
    """
    # Slope
    medians = []
    x = x.copy().ravel()
    y = y.copy().ravel()
    if not (nowarn):
        assert len(x) > 2, "More than two samples are required for this function."
        assert len(x) == len(y), "Vectors x and y must have the same length."

    for i in np.arange(len(x)):
        inner_medians = []
        for j in np.arange(len(y)):
            den = x[j] - x[i]
            if j != i and den != 0:
                inner_medians.append((y[j] - y[i]) / den)

        medians.append(np.nanmedian(inner_medians))

    return np.nanmedian(medians)


def simple_robust_regression(
    x, y, na_rm=None, conflevel=0.95, nowarn=False, pi_resolution=50
):
    """
    x and y: iterables
    na_rm: None; no effect for robust regression. Here for consistency with the non-robust case.
    nowarn: If True, then no error checking/warnings are issued. The user is committing to do that
    themselves ahead of time.

    TODO: handle the missing values case still. See the `multiple_linear_regression` function,
    especially for residuals: afterwards there are N residuals expected, even if <N points used
    during the fitting. Missing values in either x or y will have missing values.

    Simple robust regression between an `x` and a `y` using the `repeated_median_slope` method
    to calculate the slope. The intercept is the median intercept, when using that slope and the
    provided `x` and `y` values.

    The rest of the classical output from a regression are based on these robust parameter
    estimates.
    """
    x_, y_ = x.copy().ravel(), y.copy().ravel()
    x, y = x_[~np.isnan(x_) & ~np.isnan(y_)], y_[~np.isnan(x_) & ~np.isnan(y_)]

    slope = repeated_median_slope(x, y, nowarn=nowarn)
    intercept = np.nanmedian(y - slope * x)
    mean_x, mean_y = np.mean(x), np.mean(y)
    total_ssq = np.sum(np.power(y - mean_y, 2))

    out = {}

    out["N"] = min(
        x.size - np.count_nonzero(np.isnan(x)), y.size - np.count_nonzero(np.isnan(y))
    )
    out["intercept"] = intercept
    out["coefficients"] = [
        slope,
    ]
    out["fitted_values"] = intercept + slope * x
    regression_ssq = np.sum(np.power(out["fitted_values"] - mean_y, 2))
    out["residuals"] = y - out["fitted_values"]
    residual_ssq = np.sum(out["residuals"] * out["residuals"])
    # For robust method, calculate this way, since no guarantee both RegSS or RSS are < TSS.
    # So ensure this way that the TSS = RegSS + RSS, and R2 is the ratio of RegSS/TSS
    # https://learnche.org/pid/least-squares-modelling/least-squares-model-analysis
    total_ssq = regression_ssq + residual_ssq
    out["R2"] = regression_ssq / total_ssq
    out["SE"] = np.sqrt(residual_ssq / (len(x) - 2))
    out["x_ssq"] = np.sum(np.power(x - np.mean(x), 2))
    c_t = t_value(1 - (1 - conflevel) / 2, out["N"] - 2)  # 2 fitted parameters
    # out["t_value"] = np.array([c_t])  # for consistency with other regression models.
    # "pi" = prediction interval
    pi_range = np.linspace(np.min(x), np.max(x), pi_resolution)
    pi_y_pred = out["intercept"] + out["coefficients"][0] * pi_range
    if out["x_ssq"] < __eps:
        out["standard_error_intercept"] = SE_b0 = np.NaN
        out["standard_errors"] = [
            np.NaN,
        ]
        out["pi_range"] = np.vstack([pi_range, pi_y_pred, pi_y_pred]).T

    else:
        out["standard_error_intercept"] = SE_b0 = out["SE"] * np.sqrt(
            (1 / out["N"] + (mean_x) ** 2 / out["x_ssq"])
        )
        out["standard_errors"] = [
            out["SE"] * 1 / np.sqrt(out["x_ssq"]),
        ]
        var_y = (out["SE"] ** 2) * (
            1 + 1 / out["N"] + (pi_range - np.mean(x)) ** 2 / out["x_ssq"]
        )
        std_y = np.sqrt(var_y)
        lower = pi_y_pred - c_t * std_y
        upper = pi_y_pred + c_t * std_y
        out["pi_range"] = np.vstack([pi_range, lower, upper]).T

    out["conf_interval_intercept"] = np.array(
        [out["intercept"] - c_t * SE_b0, out["intercept"] + c_t * SE_b0],
    )
    out["conf_intervals"] = np.array(
        [
            [
                out["coefficients"][0] - c_t * out["standard_errors"][0],
                out["coefficients"][0] + c_t * out["standard_errors"][0],
            ],
        ]
    )
    out["leverage"] = 1 / out["N"] + np.power(x - mean_x, 2) / out["x_ssq"]
    out["k"] = 2
    if out["SE"] < __eps:
        out["influence"] = out["residuals"] * 0.0
    else:
        out["influence"] = (
            np.power(out["residuals"] / ((1 - out["leverage"]) * out["SE"]), 2)
            * out["leverage"]
            / out["k"]
        )

    return out


def multiple_linear_regression(
    X, y, fit_intercept=True, na_rm=True, conflevel=0.95, pi_resolution=50
):
    """
    Linear regression of the N rows and K columns of matrix `X` onto the single column 'y'.

    The matrix `X` will be augmented with a column of 1's if `fit_intercept` is True.
    `na_rm`: True:  removes all observations with one or more missing values.

    Notes and limitations:
        * does not handle weighting
        * N >= K at least as many rows as columns in X

    Returns a dictionary of outputs with these keys:

        coefficients:   a vector of K coefficients, one for each column in ``X``

        intercept:      returned if ``fit_intercept==True``

        standard_errors:a vector of K standard errors, one for each column in ``X``

        standard_error_intercept: standard error for the intercept

        R2:             the infamous R^2 values

        SE              the model's standard error

        fitted_values   the N predicted values, one per row in ``y``

        residuals       the N residuals

        t_value         the t-values for the standard errors

        conf_intervals  the 95% confidence intervals for the model terms: K rows,
                        2 columns: column 1 is lower, column 2 is upper

        pi_range       the prediction intervals, above an below, over the range of data.

    TODO: report hatvalues, discrepancy:  for residual detection
    """

    alpha = 1.0 - conflevel
    out = {
        "N": None,
        "coefficients": [
            np.nan,
        ],
        "intercept": np.nan,
        "standard_errors": [
            np.nan,
        ],
        "standard_error_intercept": np.nan,
        "R2": np.nan,
        "SE": np.nan,
        "fitted_values": np.nan,
        "residuals": np.nan,
        "t_value": np.nan,
        "conf_intervals": [np.nan, np.nan],
    }

    #  Data pre-processing: handle both Pandas and NumPy -> use Pandas internally for X and y
    if isinstance(X, np.ndarray):
        X_ = pd.DataFrame(X, copy=True)
    else:
        X_ = pd.DataFrame(X.values, copy=True)

    if isinstance(y, np.ndarray):
        y_ = pd.DataFrame(y.ravel(), copy=True)
    else:
        y_ = pd.DataFrame(y.values, copy=True)

    # Removing missing values:
    missing_idx = y_.isna().any(axis=1)
    if na_rm:
        missing_idx = y_.isna().any(axis=1) | X_.isna().any(axis=1)
        X_ = X_.loc[~missing_idx, :]
        y_ = y_.loc[~missing_idx]

    # CASE when there is no data, or only 1 data point
    if (y_.size <= 1) or (X_.size <= 1):
        return out

    #  Hard checks: to be converted to graceful errors later on
    out["N"], k = X_.shape
    mean_y = np.mean(y_.values)
    total_ssq = np.sum(np.power(y_.values - mean_y, 2))
    x_vector = X_.copy()
    if fit_intercept:
        # Was this: X_ = sm.add_constant(X_); but this created warnings/noise.
        X_["__constant__"] = 1.0
        X_.insert(0, "__constant__", X_.pop("__constant__"))
        k = k + 1

    assert (
        out["N"] >= k
    ), "N >= K: You need at least as many rows as there are columns to fit a linear regression."
    assert out["N"] == y_.size

    if x_vector.shape[1] == 1:
        mean_X = np.mean(x_vector)
        out["x_ssq"] = np.sum(np.power(x_vector - mean_X, 2))[0]

        # Can be calculated before the model is even fit:
        out["leverage"] = (
            1 / out["N"] + np.power(x_vector - mean_X, 2) / out["x_ssq"]
        ).values.ravel()

    # Do the work
    model = sm.OLS(y_, X_)
    results = model.fit()

    #  Report the results:
    if fit_intercept:
        out["intercept"] = results.params.values[0]
        out["standard_error_intercept"] = results._results.bse[0]
        out["coefficients"] = results.params.values[1:]
        out["standard_errors"] = results._results.bse[1:]
        out["t_value"] = results.tvalues[1:]
        out["conf_intervals"] = results._results.conf_int(alpha)[1:, :]
        out["conf_interval_intercept"] = results._results.conf_int(alpha)[0, :]
    else:
        out["coefficients"] = results.params[:]
        out["t_value"] = results.tvalues[:]
        out["standard_errors"] = results._results.bse[:]
        out["conf_intervals"] = results._results.conf_int(alpha)

    out["fitted_values"] = results._results.fittedvalues
    out["R2"] = results._results.rsquared
    regression_ssq = np.sum(np.power(out["fitted_values"] - mean_y, 2))

    out["residuals"] = (
        np.nan * np.ones((1, len(y))).ravel()
    )  # NOTE: the original y-shape is used, not y_'s shape!
    # residuals are defined as: y.values.ravel() - out["fitted_values"]
    out["residuals"][~missing_idx] = results._results.resid
    residual_ssq = np.nansum(out["residuals"] * out["residuals"])
    out["R2_regression_based"] = regression_ssq / total_ssq
    out["R2_residual_based"] = 1 - (residual_ssq / total_ssq)
    out["SE"] = np.sqrt(results._results.scale)  # np.sqrt(residual_ssq / (len(x_) - 2))
    out["k"] = k

    if x_vector.shape[1] == 1 and fit_intercept:
        # "pi" = prediction interval
        pi_range = np.linspace(
            np.min(X_.values[:, 1]), np.max(X_.values[:, 1]), pi_resolution
        )
        pi_y_pred = out["intercept"] + out["coefficients"][0] * pi_range
        if out["SE"] < __eps:
            out["influence"] = out["residuals"] * 0.0
        else:
            out["influence"] = (
                np.power(
                    results._results.resid / ((1 - out["leverage"]) * out["SE"]), 2
                )
                * out["leverage"]
                / k
            )
            var_y = (out["SE"] ** 2) * (
                1
                + 1 / out["N"]
                + (pi_range - np.mean(X_.values[:, 1])) ** 2 / out["x_ssq"]
            )
            std_y = np.sqrt(var_y)
            c_t = t_value(1 - (1 - conflevel) / 2, out["N"] - 2)  # 2 fitted parameters
            lower = pi_y_pred - c_t * std_y
            upper = pi_y_pred + c_t * std_y
            out["pi_range"] = np.vstack([pi_range, lower, upper]).T

    return out
