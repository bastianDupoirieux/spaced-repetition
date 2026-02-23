from utils.parameter_loaders import load_parameters, load_leitner_method_parameters

def test_load_parameters_leitner():
    leitner_method_name="leitner_method"
    assert load_parameters(leitner_method_name) == load_leitner_method_parameters()
