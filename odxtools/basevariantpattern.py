# SPDX-License-Identifier: MIT
from dataclasses import dataclass
from typing import List, Union
from xml.etree import ElementTree

from typing_extensions import override

from .exceptions import odxassert
from .matchingbasevariantparameter import MatchingBaseVariantParameter
from .matchingparameter import MatchingParameter
from .odxlink import OdxDocFragment
from .variantpattern import VariantPattern


@dataclass
class BaseVariantPattern(VariantPattern):
    """Base variant patterns are variant patterns used to identify the
    base variant of an ECU.
    """
    matching_base_variant_parameters: List[MatchingBaseVariantParameter]

    @staticmethod
    def from_et(et_element: ElementTree.Element,
                doc_frags: List[OdxDocFragment]) -> "BaseVariantPattern":

        matching_base_variant_parameters = [
            MatchingBaseVariantParameter.from_et(mbvp_el, doc_frags)
            for mbvp_el in et_element.iterfind("MATCHING-BASE-VARIANT-PARAMETERS/"
                                               "MATCHING-BASE-VARIANT-PARAMETER")
        ]

        odxassert(len(matching_base_variant_parameters) > 0)  # required by ISO 22901-1 Figure 141
        return BaseVariantPattern(matching_base_variant_parameters=matching_base_variant_parameters)

    @override
    def get_matching_parameters(
            self) -> Union[List[MatchingParameter], List[MatchingBaseVariantParameter]]:
        return self.matching_base_variant_parameters
