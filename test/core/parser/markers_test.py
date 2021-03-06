"""The Test file for The New Parser (Marker Classes)."""

from sqlfluff.core.parser.markers import FilePositionMarker, EnrichedFilePositionMarker


def test__markers__common_marker():
    """Test construction and comparison of markers."""
    # test making one from fresh
    fp1 = FilePositionMarker()
    fp2 = fp1.advance_by("abc")
    fp3 = fp2.advance_by("def\nghi\njlk")
    fp4 = fp3.advance_by("mno", idx=1)
    # check comparisons
    assert fp1 == FilePositionMarker(1, 1, 1, 0)
    assert fp4 > fp3 > fp2 > fp1
    assert fp1 < fp2 < fp3 < fp4
    # Check advance works without newline
    assert fp2 == FilePositionMarker(1, 1, 4, 3)
    assert fp3 == FilePositionMarker(1, 3, 4, 14)
    assert fp4 == FilePositionMarker(2, 3, 7, 17)


def test__markers__common_marker_format():
    """Test formatting of markers."""
    fp1 = FilePositionMarker(1, 2, 3, 0)
    # Check Formatting Style
    assert str(fp1) == "[0](1, 2, 3)"


def test__markers__enriched_marker_format():
    """Test formatting of enriched markers."""
    fp1 = EnrichedFilePositionMarker(
        1,
        1,
        1,
        0,
        slice(0, 1),
        slice(0, 1),
        True,
        source_pos_marker=FilePositionMarker(1, 2, 3, 0),
    )
    # Check Formatting Style
    assert str(fp1) == "[0](1, 2, 3)"
