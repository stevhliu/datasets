from datasets.features import Audio


def test_audio_instantiation():
    audio = Audio()
    assert audio.id is None
    assert audio.dtype == "dict"
    assert audio.pa_type is None
    assert audio._type == "Audio"


def test_audio_encode_example(shared_datadir):
    audio_path = str(shared_datadir / "test_audio_44100.wav")
    audio = Audio()
    encoded_example = audio.encode_example(audio_path)
    assert encoded_example.keys() == {'array', 'sample_rate'}
    assert encoded_example["array"].shape == (202311, 2)
    assert encoded_example["sample_rate"] == 44100
