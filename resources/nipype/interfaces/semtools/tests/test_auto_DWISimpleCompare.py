# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..converters import DWISimpleCompare


def test_DWISimpleCompare_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        checkDWIData=dict(
            argstr="--checkDWIData ",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputVolume1=dict(
            argstr="--inputVolume1 %s",
            extensions=None,
        ),
        inputVolume2=dict(
            argstr="--inputVolume2 %s",
            extensions=None,
        ),
    )
    inputs = DWISimpleCompare.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DWISimpleCompare_outputs():
    output_map = dict()
    outputs = DWISimpleCompare.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value