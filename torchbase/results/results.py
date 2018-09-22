class TorchResult(object):
    def __init__(self):
        self.profile_elements = list()  # List of torchbase.reference.schema.ProfileElement objects
        self.presences = list()  # List of torchbase.reference.schema.Presence objects
        self.variants = list()  # List of torchbase.reference.schema.Variant objects


def find_match(torch_ref, torch_result):
    """
    :param torch_ref: torchbase.reference.schema.TorchModel
    :param torch_result: As yet uncreated output from our mapping.
    Should have 3 lists - profile_elements, presences, and variants.
    :return: Name of matching sequence type. None if no match
    """
    match_name = None
    # Convert alleles that were found into a dictionary, where locus names are keys
    # and allele hash values are values.
    found_alleles = profile_elements_to_dict(torch_result.profile_elements)
    found_genes = presence_elements_to_dict(torch_result.presences)
    for sequence_type in torch_ref.types:
        is_match = True
        if sequence_type.profile:
            # MLST-type matching
            reference_alleles = profile_elements_to_dict(sequence_type.profile)
            if reference_alleles != found_alleles:
                is_match = False
        if sequence_type.presence and is_match:
            # Gene presence/absence matching
            reference_genes = presence_elements_to_dict(sequence_type.presence)
            if reference_genes != found_genes:
                is_match = False
        if sequence_type.variants and is_match:
            # Variant matching
            # TODO
            pass

        if is_match:
            return sequence_type.Name

    return match_name


def presence_elements_to_dict(presence_element_list):
    """
    :param presence_element_list: List of torchbase.reference.schema.Presence objects
    :return: Dictionary where gene names are keys and gene presence True/False is value
    """
    present_genes = dict()
    for presence_element in presence_element_list:
            present_genes[presence_element.LocusName] = presence_element.Presence
    return present_genes


def profile_elements_to_dict(profile_element_list):
    """
    :param profile_element_list: List of torchbase.reference.schema.ProfileElement objects
    :return: Dictionary where gene names are keys and allele hash values are values
    """
    profile_dict = dict()
    for profile_element in profile_element_list:
        profile_dict[profile_element.LocusName] = profile_element.AlleleName
    return profile_dict
