from hydra.plugins import SearchPathPlugin
from hydra._internal.config_search_path import ConfigSearchPath


class RatingCoreLibSearchPathPlugin(SearchPathPlugin):
    def manipulate_search_path(self, search_path):
        assert isinstance(search_path, ConfigSearchPath)
        search_path.append("rating_core_lib", "pkg://rating_core_lib/config")
