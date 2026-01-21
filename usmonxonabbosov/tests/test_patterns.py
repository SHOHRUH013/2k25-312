from core.builders import ModuleConfigBuilder
from core.adapters import LoggerAdapter, ExternalLogger
from core.proxy import ModuleProxy
from modules.lighting import LightingSubsystem

def test_builder():
    b = ModuleConfigBuilder()
    cfg = b.set_mode("eco").set_threshold("max", 100).build()
    assert cfg.params["mode"] == "eco"
    assert cfg.params["max"] == 100

def test_adapter_logs():
    adapter = LoggerAdapter(ExternalLogger())
    adapter.log("hello", "debug")  # just ensure no exception

def test_proxy_permission():
    lighting = LightingSubsystem()
    proxy = ModuleProxy(lighting, user_role="guest")
    try:
        proxy.perform("configure", "day")
        assert False, "guest shouldn't configure"
    except PermissionError:
        assert True
