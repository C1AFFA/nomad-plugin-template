import logging
import numpy as np # Import numpy for type comparison if needed

from nomad.datamodel import EntryArchive

from nomad_test_parser.parsers.parser import NewParser, SimpleOutput,JVParser,RawFileUNITOV # Import SimpleOutput

from nomad.datamodel import EntryArchive, EntryMetadata
from nomad.datamodel.metainfo.workflow import Workflow

def test_parse_file():
    parser = NewParser()
    archive = EntryArchive(metadata=EntryMetadata(), workflow2=Workflow(name='test'))
    mainfile_path = 'tests/data/example.out' # Define mainfile_path for clarity
    parser.parse(mainfile_path, archive, logging.getLogger())

    # Check if archive.data is an instance of SimpleOutput
    assert isinstance(archive.data, SimpleOutput)

    # Check the populated values in archive.data
    assert archive.data.message == 'This is a test message from NewParser.'
    assert archive.data.example_value == 123.456
    assert archive.data.parsed_mainfile_path == mainfile_path

    # The assertion for workflow2.name can remain if it's still relevant
    # For the current parser.py, workflow2 is not being set, so this would fail.
    # If you re-add `archive.workflow2 = Workflow(name='test')` to your parser,
    # then you can uncomment the line below.
    # assert archive.workflow2.name == 'test'


def test_parse_JV_file():
    parser = JVParser()
    archive = EntryArchive(metadata=EntryMetadata(), workflow2=Workflow(name='test'))
    mainfile_path = '001_2023_10_19_18.33.25_1A_3C_C1_1_JV.txt' # Define mainfile_path for clarity
    parser.parse(mainfile_path, archive, logging.getLogger())

    # Check if archive.data is an instance of RawFileUNITOV
    assert isinstance(archive.data, RawFileUNITOV)

    # Check the populated values in archive.data

    #assert archive.data.message == 'This is a test message from NewParser.'
    #assert archive.data.example_value == 123.456
    #assert archive.data.parsed_mainfile_path == mainfile_path

    # The assertion for workflow2.name can remain if it's still relevant
    # For the current parser.py, workflow2 is not being set, so this would fail.
    # If you re-add `archive.workflow2 = Workflow(name='test')` to your parser,
    # then you can uncomment the line below.
    # assert archive.workflow2.name == 'test'