from fastio_cli import __version__


class TestVersion:

    def test_version(self):
        assert __version__ == '0.1.0'
