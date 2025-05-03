
def test_implant_sequence_is_108(decoded_implants):
    
    for implant in decoded_implants:
        # Check if the implant has a "coeffFile" key has a "seq" key
        assert implant["coeffFile"].get("seq") == 108, \
        f"Implant {implant['implantId']} has sequence {implant["coeffFile"].get("seq")}, expected 108"