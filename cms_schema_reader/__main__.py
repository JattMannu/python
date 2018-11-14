import os
from reader import Reader
from schema_manager import SchemaManager
from schema_validator import SchemaValidator
from reader_entries import ReaderEntries

#TODO Get the path to a sample schema

dir_path = '/home/manpreet/Documents/workspace/cag/refapp_1/backend/cms/util/migrate_scripts/create_fake_exports/export/external-migrate/entries/en-gb'
dir_content_types = '/home/manpreet/Documents/workspace/cag/refapp_1/backend/cms/util/migrate_scripts/create_fake_exports/export/external-migrate/content-types'
for file_name in os.listdir(dir_path):
    print(f'Processing {file_name}')
    schema_provider = os.path.join(dir_content_types,file_name)
    entries_provider = os.path.join(dir_path,file_name)
    schema_manager = SchemaManager( Reader(schema_provider).read())
    schema_validator = SchemaValidator(schema_manager.process())

    for entry in ReaderEntries(Reader(entries_provider).read()).get_entries():
        schema_validator.check(entry)
