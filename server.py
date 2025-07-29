import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/therundown/api/therundown'

mcp = FastMCP('therundown')

@mcp.tool()
def affiliates() -> dict: 
    '''Get affiliates (aka sportsbooks). The `affiliate_id` value of each sportsbook is used as the key in the `lines` or `line_periods` events response. For example, `5Dimes` has an `affiliate_id` of `1`, so their lines are available with the key of `1` in the `events` endpoints responses.'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/affiliates'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sports() -> dict: 
    '''Get available sports. Sports may or may not have events depending on season and what is available on sportsbooks.'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/sports'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events(include: Annotated[Union[str, None], Field(description='(Optional) Specifies whether the response should include all available markets (halves/quarters/periods) instead of just full-game by default.')] = None,
           affiliate_ids: Annotated[Union[str, None], Field(description='')] = None,
           offset: Annotated[Union[str, None], Field(description='The offset in minutes from the provided date. The default offset is UTC.')] = None) -> dict: 
    '''The /sports/{sport-id}/events/{date} endpoint to request events for a particular sport on a particular date. The current odds and markets will be returned when available. To get historical odds for each market, use the individual `moneyline`, `spread`, and `total` endpoints in the `Lines` endpoints group. The date range defaults to UTC unless an offset query parameter is specified, which is the offset from UTC in minutes. For example, if the request is meant to be made from CDT, the offset should be offset=300 (5 hours). Specifying optional include values may be used to get lines for all markets (instead of just full-game by default) in addition to scores or the team names from specific sportsbooks. To request multiple, simply add multiple values and duplicate the include= parameter in the request like so: `?include=all_periods&include=scores`. When `include=all_periods` is used, the key for the lines changes from lines to line_periods. An optional offset in minutes from UTC may be sent in the request to group events by date with an offset. For example, if you are in CDT and want to see events grouped by date in CDT, then specify ?offset=300. Any value of 0.0001 represents the value NotPublished. This means that the sportsbook currently has not published a price or wager for this event, or that the line was removed.'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/sports/2/events/2020-09-20'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'include': include,
        'affiliate_ids': affiliate_ids,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def divisions(sportID: Annotated[str, Field(description='')]) -> dict: 
    '''Get divisions for a sport'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/sports/1/divisions'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sportID': sportID,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def conferences(sportID: Annotated[str, Field(description='')]) -> dict: 
    '''Get conferences for a sport'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/sports/1/conferences'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sportID': sportID,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams(sportID: Annotated[Union[int, float], Field(description='Default: 2')]) -> dict: 
    '''Teams provides a list of teams that are included in the `normalized_teams` attribute of the events responses.'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/sports/2/teams'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sportID': sportID,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_event_markets(participant_ids: Annotated[Union[str, None], Field(description='')] = None,
                     participant_type: Annotated[Union[str, None], Field(description='')] = None,
                     market_ids: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get markets for an event. Optionally provide participant_ids and participant_types and market_ids. If market_ids are not provided, they will default to 1,2,3.'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/v2/events/36902502fd7a5ea0d1f9fe8b5b4465de'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'participant_ids': participant_ids,
        'participant_type': participant_type,
        'market_ids': market_ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_markets(event_id: Annotated[str, Field(description='')]) -> dict: 
    '''Get available markets for an event. Optionally provide participant_type and participant_ids'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/v2/events/36902502fd7a5ea0d1f9fe8b5b4465de/markets'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_players(team_id: Annotated[str, Field(description='')]) -> dict: 
    '''Players by team'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/v2/teams/85/players'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team_id': team_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_market_participants(event_id: Annotated[str, Field(description='')],
                           market_ids: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get participants for the markets for an event. Optionally provide a list of market_ids'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/v2/markets/participants'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
        'market_ids': market_ids,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_team_season_stats(team_id: Annotated[Union[int, float], Field(description='Default: 11')]) -> dict: 
    '''Season stats for a team'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/v2/teams/11/stats'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team_id': team_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_player_season_stats(team_id: Annotated[Union[int, float], Field(description='Default: 11')]) -> dict: 
    '''Player season stats for a taem'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/v2/teams/11/players/stats'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'team_id': team_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_player_game_stats(event_id: Annotated[str, Field(description='')]) -> dict: 
    '''Player stats for the event_id'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/v2/events/39ae57a35f4a3088ddcfbd46dc66ba46/players/stats'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_team_game_stats(event_id: Annotated[str, Field(description='')]) -> dict: 
    '''Team stats for the event_id'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/v2/events/39ae57a35f4a3088ddcfbd46dc66ba46/stats'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_stats(sport_id: Annotated[Union[int, float], Field(description='Default: 2')]) -> dict: 
    '''Get all available stats. Optionally filter by sport_id'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/v2/stats'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sport_id': sport_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def schedules(_from: Annotated[Union[str, datetime, None], Field(description='Date (yyyy-mm-dd)')] = None,
              limit: Annotated[Union[int, float, None], Field(description='Max value is 500. Default is 50 Default: 100')] = None) -> dict: 
    '''Get the schedule for a sportID. Use the `from` parameter to change the starting date in the format of `yyyy-mm-dd` (ex: `2020-09-20`), which defaults to today. Use a `limit` parameter to set the number of events returned in the response. The max is `500` and the default is `50`. The schedules are ordered by `date_event` ascending, so send the largest or last `date_event` value current response to get the next available page.'''
    url = 'https://therundown-therundown-v1.p.rapidapi.com/sports/2/schedule'
    headers = {'x-rapidapi-host': 'therundown-therundown-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
