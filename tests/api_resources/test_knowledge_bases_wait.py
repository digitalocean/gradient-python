import types
import asyncio
import pytest

from gradient import Gradient


class DummyResp:
    def __init__(self, status=None):
        self.database_status = status


def test_wait_for_database_online_success(monkeypatch, client: Gradient):
    calls = {"n": 0}

    def fake_retrieve(uuid, **kwargs):
        calls["n"] += 1
        # become ONLINE after 3 calls
        if calls["n"] >= 3:
            return DummyResp("ONLINE")
        return DummyResp("CREATING")

    monkeypatch.setattr(client.knowledge_bases, "retrieve", fake_retrieve)

    resp = client.knowledge_bases.wait_for_database_online("kb-1", timeout=5, interval=0.01)
    assert resp.database_status == "ONLINE"
    assert calls["n"] >= 3


def test_wait_for_database_online_failed_raises(monkeypatch, client: Gradient):
    def fake_retrieve(uuid, **kwargs):
        return DummyResp("UNHEALTHY")

    monkeypatch.setattr(client.knowledge_bases, "retrieve", fake_retrieve)

    with pytest.raises(RuntimeError):
        client.knowledge_bases.wait_for_database_online("kb-2", timeout=1, interval=0.01)


def test_wait_for_database_online_timeout(monkeypatch, client: Gradient):
    def fake_retrieve(uuid, **kwargs):
        return DummyResp("CREATING")

    monkeypatch.setattr(client.knowledge_bases, "retrieve", fake_retrieve)

    with pytest.raises(TimeoutError):
        client.knowledge_bases.wait_for_database_online("kb-3", timeout=0.05, interval=0.01)


@pytest.mark.asyncio
async def test_async_wait_for_database_online_success(monkeypatch, async_client):
    calls = {"n": 0}

    async def fake_retrieve(uuid, **kwargs):
        calls["n"] += 1
        if calls["n"] >= 3:
            return DummyResp("ONLINE")
        return DummyResp("CREATING")

    monkeypatch.setattr(async_client.knowledge_bases, "retrieve", fake_retrieve)

    resp = await async_client.knowledge_bases.wait_for_database_online("kb-1", timeout=5, interval=0.01)
    assert resp.database_status == "ONLINE"


@pytest.mark.asyncio
async def test_async_wait_for_database_online_failed_raises(monkeypatch, async_client):
    async def fake_retrieve(uuid, **kwargs):
        return DummyResp("UNHEALTHY")

    monkeypatch.setattr(async_client.knowledge_bases, "retrieve", fake_retrieve)

    with pytest.raises(RuntimeError):
        await async_client.knowledge_bases.wait_for_database_online("kb-2", timeout=1, interval=0.01)


@pytest.mark.asyncio
async def test_async_wait_for_database_online_timeout(monkeypatch, async_client):
    async def fake_retrieve(uuid, **kwargs):
        return DummyResp("CREATING")

    monkeypatch.setattr(async_client.knowledge_bases, "retrieve", fake_retrieve)

    with pytest.raises(TimeoutError):
        await async_client.knowledge_bases.wait_for_database_online("kb-3", timeout=0.05, interval=0.01)
