# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import EMRegister


def test_EMRegister_inputs():
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
            position=-3,
        ),
        mask=dict(
            argstr="-mask %s",
            extensions=None,
        ),
        nbrspacing=dict(
            argstr="-uns %d",
        ),
        num_threads=dict(),
        out_file=dict(
            argstr="%s",
            extensions=None,
            hash_files=False,
            keep_extension=False,
            name_source=["in_file"],
            name_template="%s_transform.lta",
            position=-1,
        ),
        skull=dict(
            argstr="-skull",
        ),
        subjects_dir=dict(),
        template=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=-2,
        ),
        transform=dict(
            argstr="-t %s",
            extensions=None,
        ),
    )
    inputs = EMRegister.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_EMRegister_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = EMRegister.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value