# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Curvature


def test_Curvature_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        averages=dict(
            argstr="-a %d",
        ),
        copy_input=dict(),
        distances=dict(
            argstr="-distances %d %d",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            copyfile=True,
            extensions=None,
            mandatory=True,
            position=-2,
        ),
        n=dict(
            argstr="-n",
        ),
        save=dict(
            argstr="-w",
        ),
        subjects_dir=dict(),
        threshold=dict(
            argstr="-thresh %.3f",
        ),
    )
    inputs = Curvature.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Curvature_outputs():
    output_map = dict(
        out_gauss=dict(
            extensions=None,
        ),
        out_mean=dict(
            extensions=None,
        ),
    )
    outputs = Curvature.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value