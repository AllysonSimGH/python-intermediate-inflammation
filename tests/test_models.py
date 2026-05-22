"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_min, daily_max

#@pytest.mark.parametrize(                       # python decorator
#        "test_input, test_result",                # name of arguments
#        [
#            ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),   # values of arguments (copy from existing tests below)
#            ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
#        ])

@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
            ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
            (np.zeros((3, 5)), np.zeros(5)),
            ([[1, 2, 3]], [1, 2, 3]),
        ])


def test_daily_mean(test_input, test_result): # add input arguments from the parametrize decorator
    """Test that mean function works for an array of zeros and positive integers."""
    npt.assert_array_equal(daily_mean(test_input), test_result)


# def test_daily_mean_zeros():
#     """Test that mean function works for an array of zeros."""
    

#     test_input = np.array([[0, 0],
#                            [0, 0],
#                            [0, 0]])
#     test_result = np.array([0, 0])

#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)


#def test_daily_mean_integers():
    # """Test that mean function works for an array of positive integers."""

    # test_input = np.array([[1, 2],
    #                        [3, 4],
    #                        [5, 6]])
    # test_result = np.array([3, 4])

    # # Need to use Numpy testing functions to compare arrays
    # npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_mean_string():
    """Test for TypeError when passing strings"""      # Write summary before code clarifies purpose

    with pytest.raises(TypeError):                     # string instead of array give TypeError
        error_expected = daily_mean(['hi', 'there'])    # simple input  


@pytest.mark.parametrize(
        "test_input, test_result",
        [
            ([[1, 2], [3, 4], [5, 6]], [5, 6]),
            ([[1, 2, -9], [-3, 4, -2], [-1, 5, -6]], [1, 5, -2]),
        ])

def test_daily_max(test_input, test_result):
    """Test that max function works for an array of positive and negative integers."""
    npt.assert_array_equal(daily_max(test_input), test_result)


#def test_daily_max_integers():
    # """Test that the max function works for an array of positive and negative integers.
    # """
    
    # test_input = np.array([[1, 2, -9], [-3, 4, -2], [-1, 5, -6]])
    # test_result = np.array([1, 5, -2])              # update test_output accordingly


    # # Need to use Numpy testing functions to compare arrays
    # npt.assert_array_equal(daily_max(test_input), test_result) 


#def test_daily_max_string():
    # """Test for TypeError when passing strings"""      # Write summary before code clarifies purpose

    # with pytest.raises(TypeError):                     # string instead of array give TypeError
    #     error_expected = daily_max(['hi', 'there'])    # simple input      

