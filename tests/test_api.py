"""Current HTTP API regressions using the implemented collaborator interfaces."""

from types import SimpleNamespace

from aiohttp.test_utils import TestClient, TestServer

from sentinel import __version__
from sentinel.api import SentinelAPI


async def test_status_reports_installed_version():
    integration = SimpleNamespace(is_configured=lambda: False)
    sentinel = SimpleNamespace(
        _config=SimpleNamespace(sources=[]),
        manifest=SimpleNamespace(all_entries=lambda: {}),
        incident_mgr=SimpleNamespace(get_active_incidents=lambda: []),
        fixes=[], _arbiter=integration, _stigmergy=integration, _ledger=integration,
        _contracts=SimpleNamespace(pact_configured=False),
    )
    api = SentinelAPI(sentinel)
    async with TestClient(TestServer(api._app)) as client:
        response = await client.get("/status")
        assert response.status == 200
        payload = await response.json()
        assert payload["version"] == __version__
        assert payload["sources"] == 0
        assert payload["components"] == 0
