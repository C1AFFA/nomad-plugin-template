from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field

class MPPTParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_test_parser.parsers.parser import MPPTParser

        return MPPTParser(**self.model_dump())


parser_mppt_entry_point = MPPTParserEntryPoint(
    name='MPPTParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*Tracking\.txt',
    # mainfile_name_re=r'.*\.newmainfilename',
)

class EQEParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_test_parser.parsers.parser import EQEParser

        return EQEParser(**self.model_dump())

parser_eqe_entry_point = EQEParserEntryPoint(
    name='EQEParser',
    description='EQE parser entry point configuration.',
    mainfile_name_re=r'.*_IPCE_.*\.txt',
)

class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_test_parser.parsers.parser import JVParser

        return JVParser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*JV\.txt',
    # mainfile_name_re=r'.*\.newmainfilename',
)


