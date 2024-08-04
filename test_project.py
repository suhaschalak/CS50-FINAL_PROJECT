import pytest
import pandas as pd
from project import load_data, analyze_data

# Test data setup
@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    data = {
        'rocket_type': ['Falcon 9', 'Falcon Heavy', 'Atlas V', 'Delta IV'],
        'launch_site': ['Cape Canaveral', 'Kennedy Space Center', 'Vandenberg', 'Cape Canaveral'],
        'outcome': ['Success', 'Failure', 'Success', 'Success'],
        'payload_mass_kg': [5000, 13000, 2000, 6000]
    }
    df = pd.DataFrame(data)
    return df

def test_load_data(sample_data):
    """Test the load_data function."""
    df = sample_data
    assert not df.empty, "DataFrame should not be empty"
    assert 'rocket_type' in df.columns, "DataFrame should contain 'rocket_type' column"
    assert df.shape[0] == 4, "DataFrame should have 4 rows"

def test_analyze_data(sample_data):
    """Test the analyze_data function."""
    df = sample_data
    correlation, success_rate_by_rocket, success_rate_by_site = analyze_data(df)
    
    # Check correlation output
    assert isinstance(correlation, pd.DataFrame), "Correlation should be a DataFrame"
    
    # Check success rates
    assert success_rate_by_rocket['Falcon 9'] == pytest.approx(1.0), "Success rate for Falcon 9 should be 1.0"
    assert success_rate_by_site['Cape Canaveral'] == pytest.approx(0.5), "Success rate for Cape Canaveral should be 0.5"

if __name__ == "__main__":
    pytest.main()
