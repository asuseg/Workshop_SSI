import pytest
from eva_data_analysis import text_to_duration, calculate_crew_size

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth valeus
    for typical durations with a non-zero minute component
    """
    assert text_to_duration("10:20") == pytest.approx(10.3333333)


def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values
    for typical whole hour durations
    """
    input_value = "10:00"
    assert text_to_duration(input_value) == 10


# Decorator: specific to the function that comes just below 
@pytest.mark.parametrize("input_value, expected_result",[
    ("One L; Two B;", 2),
    (" One L; Two B; Three K; Four M N;", 4)                       
]) 
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that calculate_crew_size returns the correct number of 
    members in the crew for typical values
    """
    actual_result =  calculate_crew_size(input_value)
    assert actual_result == expected_result


def test_calculate_crew_size_edge():
    """
    Test that calculate_crew_size returns expected value when the 
    string is empty
    """    
    # Typical value 2
    actual_result =  calculate_crew_size(" ")
    assert actual_result is None
    
