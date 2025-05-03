
def test_implant_sequence_is_108(decoded_implants):
    """
    Test that all decoded implants have a sequence number of 108.

    Iterates through each implant and checks that the 'seq' key 
    in the decoded 'coeffFile' equals 108.

    Args:
        decoded_implants (list): A list of decoded implant dictionaries.

    Raises:
        AssertionError: If any implant has a 'seq' value other than 108.
    """
    for implant in decoded_implants:
        # Check if the implant has a "coeffFile" key has a "seq" key
        assert implant["coeffFile"].get("seq") == 108, \
        f"Implant {implant['implantId']} has sequence {implant["coeffFile"].get("seq")}, expected 108"