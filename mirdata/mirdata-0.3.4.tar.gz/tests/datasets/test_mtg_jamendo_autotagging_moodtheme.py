import numpy as np
import pytest

from mirdata.datasets import mtg_jamendo_autotagging_moodtheme
from tests.test_utils import run_track_tests


def test_track():
    default_trackid = "track_0000948"
    data_home = "tests/resources/mir_datasets/mtg_jamendo_autotagging_moodtheme"
    dataset = mtg_jamendo_autotagging_moodtheme.Dataset(data_home)
    track = dataset.track(default_trackid)

    expected_attributes = {
        "audio_path": "tests/resources/mir_datasets/mtg_jamendo_autotagging_moodtheme/audios/48/948.mp3",
        "track_id": "track_0000948",
    }

    expected_property_types = {
        "audio": tuple,
        "artist_id": str,
        "album_id": str,
        "duration": float,
        "tags": str,
    }

    run_track_tests(track, expected_attributes, expected_property_types)

    audio, sr = track.audio
    assert sr == 44100, "sample rate {} is not 44100".format(sr)
    assert audio.shape == (2, 88200), "audio shape {} was not (2, 88200)".format(
        audio.shape
    )


def test_track_properties_and_attributes():
    default_trackid = "track_0000948"
    data_home = "tests/resources/mir_datasets/mtg_jamendo_autotagging_moodtheme"
    dataset = mtg_jamendo_autotagging_moodtheme.Dataset(data_home)
    track = dataset.track(default_trackid)

    assert track.track_id == default_trackid
    assert track.artist_id == "artist_000087"
    assert track.album_id == "album_000149"
    assert track.duration == 212.7
    assert track.tags == "mood/theme---background"


def test_to_jams():
    default_trackid = "track_0000948"
    data_home = "tests/resources/mir_datasets/mtg_jamendo_autotagging_moodtheme"
    dataset = mtg_jamendo_autotagging_moodtheme.Dataset(data_home)
    track = dataset.track(default_trackid)
    jam = track.to_jams()
    assert jam["sandbox"].track_id == default_trackid
    assert jam["sandbox"].artist_id == "artist_000087"
    assert jam["sandbox"].album_id == "album_000149"
    assert jam.file_metadata.duration == 212.7
    assert jam["sandbox"].tags == "mood/theme---background"


def test_get_track_ids_for_split():
    dataset = mtg_jamendo_autotagging_moodtheme.Dataset(
        "tests/resources/mir_datasets/mtg_jamendo_autotagging_moodtheme"
    )
    assert len(dataset.get_track_ids_for_split(0)["train"]) == 1
    assert len(dataset.get_track_ids_for_split(0)["validation"]) == 1
    assert len(dataset.get_track_ids_for_split(0)["test"]) == 1
    assert len(dataset.get_track_ids_for_split(1)["train"]) == 1
    assert len(dataset.get_track_ids_for_split(1)["validation"]) == 1
    assert len(dataset.get_track_ids_for_split(1)["test"]) == 1
    assert len(dataset.get_track_ids_for_split(2)["train"]) == 1
    assert len(dataset.get_track_ids_for_split(2)["validation"]) == 1
    assert len(dataset.get_track_ids_for_split(2)["test"]) == 1
    assert len(dataset.get_track_ids_for_split(3)["train"]) == 1
    assert len(dataset.get_track_ids_for_split(3)["validation"]) == 1
    assert len(dataset.get_track_ids_for_split(3)["test"]) == 1
    assert len(dataset.get_track_ids_for_split(4)["train"]) == 1
    assert len(dataset.get_track_ids_for_split(4)["validation"]) == 1
    assert len(dataset.get_track_ids_for_split(4)["test"]) == 1

    with pytest.raises(Exception):
        dataset.get_track_ids_for_split(-1)
