from typing import Any, Tuple

import pytest
from aibaba_ai_core.structured_query import (
    Comparator,
    Comparison,
    Operation,
    Operator,
)

from aibaba_ai_community.query_constructors.dashvector import DashvectorTranslator

DEFAULT_TRANSLATOR = DashvectorTranslator()


@pytest.mark.parametrize(
    "triplet",
    [
        (Comparator.EQ, 2, "foo = 2"),
        (Comparator.LT, 2, "foo < 2"),
        (Comparator.LTE, 2, "foo <= 2"),
        (Comparator.GT, 2, "foo > 2"),
        (Comparator.GTE, 2, "foo >= 2"),
        (Comparator.LIKE, "bar", "foo LIKE '%bar%'"),
    ],
)
def test_visit_comparison(triplet: Tuple[Comparator, Any, str]) -> None:
    comparator, value, expected = triplet
    actual = DEFAULT_TRANSLATOR.visit_comparison(
        Comparison(comparator=comparator, attribute="foo", value=value)
    )
    assert expected == actual


@pytest.mark.parametrize(
    "triplet",
    [
        (Operator.AND, "foo < 2 AND bar = 'baz'"),
        (Operator.OR, "foo < 2 OR bar = 'baz'"),
    ],
)
def test_visit_operation(triplet: Tuple[Operator, str]) -> None:
    operator, expected = triplet
    op = Operation(
        operator=operator,
        arguments=[
            Comparison(comparator=Comparator.LT, attribute="foo", value=2),
            Comparison(comparator=Comparator.EQ, attribute="bar", value="baz"),
        ],
    )
    actual = DEFAULT_TRANSLATOR.visit_operation(op)
    assert expected == actual
