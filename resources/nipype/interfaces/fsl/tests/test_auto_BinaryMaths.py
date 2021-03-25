# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..maths import BinaryMaths


def test_BinaryMaths_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=2,
        ),
        internal_datatype=dict(
            argstr="-dt %s",
            position=1,
        ),
        nan2zeros=dict(
            argstr="-nan",
            position=3,
        ),
        operand_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=5,
            xor=["operand_value"],
        ),
        operand_value=dict(
            argstr="%.8f",
            mandatory=True,
            position=5,
            xor=["operand_file"],
        ),
        operation=dict(
            argstr="-%s",
            mandatory=True,
            position=4,
        ),
        out_file=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            hash_files=False,
            position=-2,
        ),
        output_datatype=dict(
            argstr="-odt %s",
            position=-1,
        ),
        output_type=dict(),
    )
    inputs = BinaryMaths.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BinaryMaths_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = BinaryMaths.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value