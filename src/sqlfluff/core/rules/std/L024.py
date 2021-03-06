"""Implementation of Rule L024."""


from sqlfluff.core.rules.std.L023 import Rule_L023


class Rule_L024(Rule_L023):
    """Single whitespace expected after USING in JOIN clause.

    | **Anti-pattern**

    .. code-block::

        SELECT b
        FROM foo
        LEFT JOIN zoo USING(a)

    | **Best practice**
    | The • character represents a space.
    | Add a space after USING, to avoid confusing it
    | for a function.

    .. code-block::

        SELECT b
        FROM foo
        LEFT JOIN zoo USING•(a)

    """

    expected_mother_segment_type = "join_clause"
    pre_segment_identifier = ("name", "USING")
    post_segment_identifier = ("type", "start_bracket")
    allow_newline = True
