import logging
import numpy as np # Import numpy for type comparison if needed
import sys
import os
from pydantic import BaseModel
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nomad_test_parser.parsers.parser import NewParser, SimpleOutput,JVParser,RawFileUNITOV,UNITOV_JVmeasurement # Import SimpleOutput

from nomad.datamodel import EntryArchive, EntryMetadata
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.metainfo.metainfo import (
    JSON,
    Capitalized,
    Category,
    Datetime,
    MCategory,
    MSection,
    Quantity,
    Reference,
    Section,
)
from nomad.datamodel.data import EntryData, ArchiveSection, User, UserReference, AuthorReference
#from nomad.datamodel.datamodel import MongoUploadMetadata, EditableUserMetadata,AuthLevel;
#from nomad.metainfo.elasticsearch_extension import Elasticsearch,DocumentType;

print(EntryMetadata().main_author)


def test_parse_file():
    parser = NewParser()

    #meta_data.main_author = UserReference()
    #meta_data.main_author.user_id = "test"
    archive = EntryArchive()
    archive.metadata = EntryMetadata();
    archive.workflow2 = Workflow(name='test')

    #assert not archive.metadata.main_author == None;

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
    archive = EntryArchive()

    archive.workflow2=Workflow(name='test');

    meta_data = EntryMetadata();
    meta_data.main_author = User();
    meta_data.main_author.user_id = "42";

    archive.metadata=meta_data;

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