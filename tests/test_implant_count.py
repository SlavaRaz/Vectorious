from collections import Counter

def test_implant_manufacturer_count(implants):
    """
    Test that the expected number of implants per manufacturer exists.

    Counts implants by manufacturer name and asserts the correct number 
    for 'sct' and 'schott'.

    Args:
        implants (list): A list of implant dictionaries.

    Raises:
        AssertionError: If the count for any expected manufacturer is incorrect.
    """
    # Count the occurrences of each manufacturer in the implants list
    manufacturer_counts = Counter([implant["manufacturer"] for implant in implants])
    # Check the counts of each manufacturer
    assert manufacturer_counts["sct"] == 3 ,f"Expected 3 'sct', got {manufacturer_counts['sct']}"
    assert manufacturer_counts["schott"] == 2 ,f"Expected 2 'schott', got {manufacturer_counts['schott']}"

