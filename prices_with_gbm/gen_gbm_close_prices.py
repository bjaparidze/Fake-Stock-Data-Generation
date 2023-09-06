import numpy as np
from prices_with_gbm.geometric_brownian_12 import (
    ConstantDrift,
    ConstantSigma,
    DataInitP,
    GenGeoBrownian,
    RandomInitP,
    estimate_drift_constants,
    estimate_gBrownian_correlation,
    estimate_sigma_constants,
)


def generate_close_prices(
    num_of_companies: int, sample_size: int, num_of_days: int
) -> np.ndarray:
    """
    Generates close prices for a specified number of companies over specified number of days
    Returns a pandas dataframe
    """

    np.random.seed(101)

    # constant drift instance
    # sample size for gen geo Brownian simulation
    T = sample_size + 1
    # Define the range
    lower_bound_mu = 3e-4  # Lower bound of the range (inclusive)
    upper_bound_mu = -3e-4  # Upper bound of the range (exclusive)

    # Generate random floats
    mu_constants = np.random.uniform(lower_bound_mu, upper_bound_mu, num_of_companies)

    constant_drift = ConstantDrift(T, tuple(mu_constants))

    # constant sigma instance
    lower_bound_sigma = -3e-2
    upper_bound_sigma = 3e-2

    sigma_constants = np.random.uniform(
        lower_bound_sigma, upper_bound_sigma, num_of_companies
    )

    constant_sigma = ConstantSigma(T, tuple(sigma_constants))

    # init P instance
    lower_bound = 1
    upper_bound = 1000
    n_procs = num_of_companies
    random_init_P = RandomInitP(lower_bound, upper_bound, n_procs)

    # generalized geometric Brownian motion with dependency injection
    rho = 0.8
    gen_geo_brownian = GenGeoBrownian(
        constant_drift, constant_sigma, random_init_P, rho=rho
    )

    # real data sim
    initial_gen_gbm_values = gen_geo_brownian.get_P(random_state=100)

    # estimate constant drift
    mu_constants = estimate_drift_constants(initial_gen_gbm_values)
    # implementation of Drift protocol
    constant_drift = ConstantDrift(T, mu_constants)

    # estimate constant sigma
    sigma_constants = estimate_sigma_constants(initial_gen_gbm_values)
    # implementation of sigma Protocol
    constant_sigma = ConstantSigma(T, sigma_constants)

    # init P from data
    data_init_P = DataInitP(initial_gen_gbm_values)

    # estimate gen geo Brownian correlation
    rho = estimate_gBrownian_correlation(initial_gen_gbm_values)

    # generalized geometric Brownian motion with dependency injection
    gen_geo_brownian = GenGeoBrownian(
        constant_drift, constant_sigma, data_init_P, rho=rho
    )
    close_prices = gen_geo_brownian.get_P(random_state=100)

    close_prices = close_prices[
        np.concatenate(
            ([0], np.arange(1, len(close_prices), sample_size // num_of_days))
        )
    ]

    return close_prices
