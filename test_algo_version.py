from datetime import datetime

def test_algo_version_by_creation_date(decoded_implants):
    
    for implant in decoded_implants:
        # Check if the implant has a "coeffFile" key
        coeff = implant["coeffFile"]
        # Convert the "creationTime" string to a datetime object
        creation = datetime.fromisoformat(coeff["creationTime"])
        # Short if statement to determine the expected algoVersion
        expected_algo = 4 if creation.year < 2024 else 5\
        # Assert that the algoVersion matches the expected value
        assert coeff["algoVersion"] == expected_algo, \
            f"Implant {implant['implantId']} has algoVersion {coeff['algoVersion']} for year {creation.year}, expected {expected_algo}"