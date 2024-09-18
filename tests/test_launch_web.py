from pages.search_page import SearchPage
from pages.search_result_page import SearchResultPage
from pages.video_stream_page import VideoStreamPage
from .base_test import BaseTest
from pages.home_page import HomePage


class TestLaunchTwitch(BaseTest):

    def test_launch_twitch(self, driver, config):
        home_page = HomePage(self.driver, self.config, self.environment)
        home_page.load()
        home_page.is_loaded()
        home_page.click_search_button()
        search_page = SearchPage(self.driver, self.config, self.environment)
        search_page.is_loaded()
        search_page.enter_search_text("StarCraft II")
        search_page.enter()
        search_result_page = SearchResultPage(self.driver, self.config, self.environment)
        search_result_page.is_loaded()
        search_result_page.scroll()
        search_result_page.scroll()
        if search_result_page.check_video_section_exist():
            search_result_page.click_video_by_index(1)
            video_stream_page = VideoStreamPage(self.driver, self.config, self.environment)
            video_stream_page.is_loaded()
            if video_stream_page.is_audio_muted_pop_shown():
                video_stream_page.click_close_audio_muted_pop()
            video_stream_page.is_video_loaded()
            video_stream_page.save_screenshot()
