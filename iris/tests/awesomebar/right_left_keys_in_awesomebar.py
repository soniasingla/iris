# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self, app):
        BaseTest.__init__(self, app)
        self.meta = 'This test case navigates through the awesomebar suggestions/one-offs/settings gear using the ' \
                    'right/left keys.'
        self.test_case_id = '108277'
        self.test_suite_id = '1902'
        self.locales = ['en-US']

    def run(self):
        url = LocalWeb.FIREFOX_TEST_SITE
        search_with_google_one_off_string_pattern = Pattern('search_with_Google_one_off_string.png')
        settings_gear_highlighted_pattern = Pattern('settings_gear_highlighted.png')

        region = Region(0, 0, SCREEN_WIDTH, 2 * SCREEN_HEIGHT / 3)

        navigate(url)
        expected = exists(LocalWeb.FIREFOX_LOGO, 10)
        assert_true(self, expected, 'Page successfully loaded, firefox logo found.')

        select_location_bar()

        paste('moz')

        # Wait a moment for the suggests list to fully populate before stepping down through it.
        time.sleep(Settings.UI_DELAY)

        # Without closing the autocomplete drop-down hit the arrow DOWN key until you reach the first one-off button.
        # The search suggestion list has 10 suggestions by default.
        for i in range(10):
            scroll_down()

        expected = region.exists(search_with_google_one_off_string_pattern, 10)
        assert_true(self, expected, 'The search engine in focus is \'Google\'.')

        # Once the first one-off is selected, hit the RIGHT arrow key until the first one-off is selected again.

        for i in range(7):
            type(Key.RIGHT)

        # Make sure that the settings gear gets in focus before the first one-off is focused again.
        expected = region.exists(settings_gear_highlighted_pattern, 10)
        assert_true(self, expected, 'The settings gear is in focus.')

        type(Key.RIGHT)

        expected = region.exists(search_with_google_one_off_string_pattern, 10)
        assert_true(self, expected, 'The search engine in focus is \'Google\'.')

        # Once the first one-off is selected, hit the LEFT arrow key until the first one-off is selected again.

        type(Key.LEFT)

        expected = region.exists(settings_gear_highlighted_pattern, 10)
        assert_true(self, expected, 'The settings gear is in focus.')

        for i in range(7):
            type(Key.LEFT)

        expected = region.exists(search_with_google_one_off_string_pattern, 10)
        assert_true(self, expected, 'The search engine in focus is \'Google\'.')
