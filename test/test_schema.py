# -*- coding: utf-8 -*-

"""
    @author: Hai
    @since: Jan 2017
"""
import sqlalchemy
import pytest
import blog

@pytest.fixture
def config():
    return blog.config.load_config()

def test_schema(config):
    db_config=config['database']
    connect_string="mysql+mysqldb://{0}:{1}@{2}/{3}?charset=utf8&use_unicode=0".format(db_config['username'],
            db_config['password'],db_config['hostname'],db_config['db'])
    engine=sqlalchemy.create_engine(connect_string)