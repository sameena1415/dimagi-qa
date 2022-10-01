""""Contains test data that are used as user inputs across various areass used in Case Serach"""
import os


class CaseSearchUserInput:
    """User Test Data"""

    """App Names"""
    case_search_app_name = "Music App (Case Search & Claim)"

    """Users"""
    user_1 = 'automation-user-1'
    user_2 = 'automation-user-2'

    """Menus"""
    normal_menu = "Songs (Normal)"
    search_first_menu = "Songs (Search First)"
    see_more_menu = "Songs (See More)"
    skip_default_menu = "Songs (Skip to Default Search)"
    artist_menu = "Artist"

    """Forms"""
    play_song_form = "Play Song"

    """Cases Types"""


    """Pre=Configured Cases"""
    song_case_bugs = "Bugs"

    """Case Properties"""
    # Rating
    one_star = "*"
    two_star = "**"
    three_star = "***"
    four_star = "****"
    five_star = "*****"
    ratings = {one_star: '1', two_star: '2', three_star: '3', four_star: '4', five_star: '5'}
