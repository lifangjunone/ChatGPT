#!/usr/bin/env python
# coding=utf-8


import pytest
from flask import url_for

from tests.configtest import app


@pytest.mark.options(debug=False)
def test_app(app):
    assert not app.debug, 'Ensure the app not in debug mode'


class TestFixtures:
    def test_config_access(self, config):
        assert config['TESTING']

    def test_client(self, client):
        assert client.get('/healthcheck').status_code == 200

    def test_accept_json(self, accept_json):
        assert accept_json == [('Accept', 'application/json')]

    def test_accept_jsonp(self, accept_jsonp):
        assert accept_jsonp == [('Accept', 'application/json-p')]

    def test_request_ctx(self, app, request_ctx):
        assert request_ctx.app is app


class TestJSONResponse:
    def test_json_response(self, client, accept_json):
        res = client.get(url_for('api_v1.apiversion'), headers=accept_json)
        assert res.json['app_version'] == 'v0.0.1'


@pytest.mark.usefixtures('client_class')
class TestClientClass:
    def test_client_attribute(self):
        assert hasattr(self, 'client')
        assert self.client.get('/healthcheck').status_code == 200
